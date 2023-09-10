from django.db import models
from ckeditor.fields import RichTextField


class Sofa(models.Model):
    """
    Description of Sofa Model of Catalog App
    """

    # Первая группа полей
    name = models.CharField(max_length=255, verbose_name="Название модели")
    working_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Рабочее название")
    short_description = RichTextField(verbose_name="Короткое описание", help_text="Отображается в карточке дивана в каталоге")
    description = RichTextField(verbose_name="Описание", help_text="Отображается на странице дивана")

    # Вторая группа полей
    SOFA_TYPE_CHOICES = [
        ('straight', 'Прямой'),
        ('corner', 'Угловой'),
        ('folding', 'Раскладной'),
        ('non_folding', 'Нераскладной'),
    ]
    sofa_type = models.CharField(max_length=50, choices=SOFA_TYPE_CHOICES, verbose_name="Тип")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    # Третья группа полей
    height = models.FloatField(verbose_name="Высота")
    width = models.FloatField(verbose_name="Ширина")
    depth = models.FloatField(verbose_name="Глубина")
    seat_depth = models.FloatField(verbose_name="Глубина посадочного места")
    back_height = models.FloatField(verbose_name="Высота спинки")
    armrest_height = models.FloatField(verbose_name="Высота подлокотников")

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
    image = models.ImageField(upload_to='core/catalog/sofas/', verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    def __str__(self):
        return f'Изображение №{self.order}'

    class Meta:
        verbose_name = 'изображение дивана'
        verbose_name_plural = 'Изображения диванов'
        ordering = ['order', ]
