"""Проверка и пересохранение фото, которые присылают анонимные авторы отзывов."""
import io
import uuid

from django.core.files.base import ContentFile
from PIL import Image, ImageOps, UnidentifiedImageError

MAX_PHOTOS = 5
MAX_PHOTO_SIZE = 5 * 1024 * 1024        # как на фронте: до 5 МБ
MAX_PIXELS = 40_000_000                 # защита от «пиксельной бомбы» до декодирования
MAX_SIDE = 2560                         # больше для отзыва не нужно
ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}


class PhotoError(ValueError):
    """Ошибка с текстом, который можно показать пользователю."""


def process_photo(upload):
    """Проверяет, что файл — настоящее изображение, и пересохраняет его в JPEG.

    Пересохранение отбрасывает всё, кроме пикселей: EXIF с геолокацией, вложенные
    скрипты, полиглоты. Имя файла генерируется заново, имя от клиента не используется.
    """
    if upload.size > MAX_PHOTO_SIZE:
        raise PhotoError("Фото должно быть размером до 5 МБ")

    try:
        with Image.open(upload) as probe:
            if probe.format not in ALLOWED_FORMATS:
                raise PhotoError("Фото должно быть в формате JPG или PNG")
            width, height = probe.size
            if width * height > MAX_PIXELS:
                raise PhotoError("Слишком большое разрешение фото")
            probe.verify()

        upload.seek(0)
        with Image.open(upload) as img:
            img.load()
            img = ImageOps.exif_transpose(img)
            if img.mode != "RGB":
                # Прозрачность заливаем белым, как фон карточки отзыва.
                rgba = img.convert("RGBA")
                img = Image.new("RGB", rgba.size, (255, 255, 255))
                img.paste(rgba, mask=rgba.getchannel("A"))
            img.thumbnail((MAX_SIDE, MAX_SIDE))
            out = io.BytesIO()
            img.save(out, "JPEG", quality=85, optimize=True)
    except PhotoError:
        raise
    except (UnidentifiedImageError, OSError, SyntaxError, ValueError, Image.DecompressionBombError):
        raise PhotoError("Файл не является изображением")

    return ContentFile(out.getvalue(), name=f"{uuid.uuid4().hex}.jpg")
