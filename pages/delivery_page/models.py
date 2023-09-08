from django.db import models


class DeliveryBlock(models.Model):
    """
    Description of DeliveryBlock Model of Delivery Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description_first = models.CharField(verbose_name='Описание №1', max_length=500)
    description_second = models.CharField(verbose_name='Описание №2', max_length=500)

    def __str__(self):
        return 'Доставка'

    class Meta:
        verbose_name = '1 - Доставка'
        verbose_name_plural = '1 - Доставка'


class PaymentBlock(models.Model):
    """
    Description of PaymentBlock Model of Delivery Page App
    """

    title_main = models.CharField(verbose_name='Главный заголовок', max_length=500)

    title_first = models.CharField(verbose_name='Подзаголовок №1', max_length=500)
    description_first = models.CharField(verbose_name='Описание №1', max_length=500)
    payment_first = models.CharField(verbose_name='Процент оплаты №1', max_length=3)

    title_second = models.CharField(verbose_name='Подзаголовок №2', max_length=500)
    description_second = models.CharField(verbose_name='Описание №2', max_length=500)
    payment_second = models.CharField(verbose_name='Процент оплаты №2', max_length=3)

    image = models.FileField(verbose_name='Фото', upload_to='delivery_page/payment/', max_length=500)

    def __str__(self):
        return 'Оплата'

    class Meta:
        verbose_name = '2 - Порядок оплаты'
        verbose_name_plural = '2- Порядок оплаты'
