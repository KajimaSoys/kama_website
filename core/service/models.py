from django.db import models
from ckeditor.fields import RichTextField
from core.catalog.models import Sofa


class Question(models.Model):
    """
    Description of Questions Model of Service App
    """

    question = models.CharField(verbose_name='Вопрос', max_length=500)
    answer = RichTextField(verbose_name='Ответ', config_name='default')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name="Порядок")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'
        ordering = ['order', ]


class Review(models.Model):
    """
    Description of Reviews Model of Service App
    """

    author = models.CharField(verbose_name='Имя автора', max_length=500)
    review = RichTextField(verbose_name='Отзыв', config_name='default')
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")
    sofa = models.ForeignKey(Sofa, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews', verbose_name="Диван")
    author_photo = models.FileField(verbose_name='Фото автора', upload_to='core/service/reviews/', max_length=500, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['order', ]


class ReviewPhoto(models.Model):
    """
    Description of ReviewsPhoto Model of Service App
    """

    field = models.ForeignKey(Review, related_name='photos', on_delete=models.CASCADE)
    photo = models.FileField(verbose_name='Фото', upload_to='core/service/reviews/', max_length=500)
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    def __str__(self):
        return self.field.author

    class Meta:
        verbose_name = 'Фото отзыва'
        verbose_name_plural = 'Фото отзывов'
        ordering = ['order', ]


class PopularModel(models.Model):
    """
    Description of PopularModel Model of Service App
    """

    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")
    sofa = models.ForeignKey(Sofa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Диван")

    def __str__(self):
        return self.sofa.name

    class Meta:
        verbose_name = 'популярная модель'
        verbose_name_plural = 'Популярные модели'
        ordering = ['order', ]


class Order(models.Model):
    """
    Description of Order Model of Service App
    """

    name = models.CharField(verbose_name='Имя', max_length=250)
    number = models.CharField(verbose_name='Номер телефона', max_length=40)
    message = models.TextField(verbose_name='Какая мебель нужна?', blank=True)

    project_version = models.CharField(verbose_name='Версия приложения', blank=True, max_length=10)
    created = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    user_agent = models.CharField(verbose_name='UserAgent', blank=True, max_length=2000)
    screen_resolution = models.CharField(verbose_name='Разрешение экрана', blank=True, max_length=100)
    browser_language = models.CharField(verbose_name='Язык браузера', blank=True, max_length=100)
    timezone = models.CharField(verbose_name='Временная зона', blank=True, max_length=100)
    cookie = models.TextField(verbose_name='Cookie', blank=True, max_length=5000)

    def __str__(self):
        return f'{self.name} - {self.message} - {self.created}'

    class Meta:
        verbose_name = 'заявка с сайта'
        verbose_name_plural = 'Заявки с сайта'
