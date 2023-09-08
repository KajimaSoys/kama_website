from django.db import models
from ckeditor.fields import RichTextField


class Question(models.Model):
    """
    Description of Questions Model of Service App
    """

    question = models.CharField(verbose_name='Вопрос', max_length=500)
    answer = RichTextField(verbose_name='Ответ', config_name='default')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'


class Review(models.Model):
    """
    Description of Reviews Model of Service App
    """

    author = models.CharField(verbose_name='Имя автора', max_length=500)
    review = RichTextField(verbose_name='Отзыв', config_name='default')
    author_photo = models.FileField(verbose_name='Фото автора', upload_to='core/service/reviews/', max_length=500, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewPhoto(models.Model):
    """
    Description of ReviewsPhoto Model of Service App
    """

    field = models.ForeignKey(Review, related_name='photos', on_delete=models.CASCADE)
    photo = models.FileField(verbose_name='Фото', upload_to='core/service/reviews/', max_length=500)

    def __str__(self):
        return self.field.author

    class Meta:
        verbose_name = 'Фото отзыва'
        verbose_name_plural = 'Фото отзывов'


