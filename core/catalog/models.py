from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class Sofa(models.Model):
    """
    Description of Sofa Model of Catalog App
    """

    # Первая группа полей
    name = models.CharField(max_length=255, verbose_name="Название модели")
    working_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Рабочее название")
    short_description = RichTextField(verbose_name="Короткое описание", help_text="Отображается в карточке дивана в каталоге")
    description = RichTextField(verbose_name="Описание", help_text="Отображается на странице дивана")
    active = models.BooleanField(verbose_name="Опубликовано на сайте?", default=True)

    # Вторая группа полей
    SOFA_FORM_CHOICES = [
        ('straight', 'Прямой'),
        ('corner', 'Угловой'),
        ('p-shaped', ' П-образный')
    ]

    sofa_form = models.CharField(max_length=50, choices=SOFA_FORM_CHOICES, verbose_name="Форма", blank=True)

    SOFA_TYPE_CHOICES = [
        ("folding", "Раскладной"),
        ("non_folding", "Нераскладной"),
    ]
    sofa_type = models.CharField(max_length=50, choices=SOFA_TYPE_CHOICES, verbose_name="Тип", blank=True)

    FOLDING_MECHANISM_CHOICES = [
        ('tik-tac', 'Тик-так'),
        ('dolphin', 'Дельфин'),
    ]

    folding_mechanism = models.CharField(max_length=50, choices=FOLDING_MECHANISM_CHOICES, verbose_name="Механизм раскладывания", blank=True)
    folding_size = models.FloatField(verbose_name="Размер расклада дивана", blank=True, null=True)

    color = models.CharField(max_length=50, verbose_name="Цвет", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    # Третья группа полей
    height = models.FloatField(verbose_name="Общая высота")
    width = models.FloatField(verbose_name="Общая ширина")
    depth = models.FloatField(verbose_name="Общая глубина")
    seat_depth = models.FloatField(verbose_name="Глубина посадочного места", blank=True, null=True)
    back_height = models.FloatField(verbose_name="Высота спинки", blank=True, null=True)
    armrest_height = models.FloatField(verbose_name="Высота подлокотников", blank=True, null=True)
    seat_height = models.FloatField(verbose_name="Высота посадочного места", blank=True, null=True)
    legs_height = models.FloatField(verbose_name="Высота ножек", blank=True, null=True)

    straight_module_depth = models.FloatField(verbose_name="Глубина прямого модуля", blank=True, null=True)
    corner_module_depth = models.FloatField(verbose_name="Глубина углового модуля", blank=True, null=True)
    module_depth = models.FloatField(verbose_name="Глубина модуля", blank=True, null=True)
    pouf_depth = models.FloatField(verbose_name="Глубина пуфа", blank=True, null=True)

    # Четвертая группа полей
    other_variants = models.ManyToManyField('self', blank=True, verbose_name="Другие варианты исполнения")

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name="Порядок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'диван'
        verbose_name_plural = 'Диваны'
        ordering = ['order', ]


class SofaImage(models.Model):
    """
    Description of SofaImage Model of Catalog App
    """
    sofa = models.ForeignKey(Sofa, related_name='images', on_delete=models.CASCADE, verbose_name="Диван")
    image = ResizedImageField(
        size=[1184, 620],
        quality=85,
        upload_to="core/catalog/sofas/",
        verbose_name="Изображение",
    )
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    def __str__(self):
        return f'Изображение №{self.order}'

    class Meta:
        verbose_name = 'изображение дивана'
        verbose_name_plural = 'Изображения диванов'
        ordering = ['order', ]
