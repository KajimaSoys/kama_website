from django.db import models


class HeaderBlock(models.Model):
    """
    Description of HeaderBlock Model of Main Page App
    """

    logo = models.FileField(verbose_name='Логотип - темный', upload_to='main_page/header/', max_length=500)
    logo_light = models.FileField(verbose_name='Логотип - светлый', upload_to='main_page/header/', max_length=500)

    number = models.CharField(verbose_name='Номер компании', max_length=255)

    def __str__(self):
        return 'Навигационная панель'

    class Meta:
        verbose_name = '1 - Навигационная панель'
        verbose_name_plural = '1 - Навигационная панель'


class MainBlock(models.Model):
    """
    Description of MainBlock Model of Main Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)

    image = models.FileField(verbose_name='Фото', upload_to='main_page/main/', max_length=500)

    def __str__(self):
        return 'Главный блок'

    class Meta:
        verbose_name = '2 - Главный блок'
        verbose_name_plural = '2 - Главный блок'


# class CatalogTeaserBlock(models.Model):
#     """
#     Description of CatalogTeaserBlock Model of Main Page App
#     """
#
#     image = models.FileField(verbose_name='Изображение тизера каталога', upload_to='main_page/catalog_teaser/', max_length=500)
#     description = models.CharField(verbose_name='Подпись тизера', max_length=500)
#
#     def __str__(self):
#         return 'Тизер  каталога'
#
#     class Meta:
#         verbose_name = '3 - Тизер каталога'
#         verbose_name_plural = '3 - Тизер каталога'


class AboutBlock(models.Model):
    """
    Description of AboutBlock Model of Main Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)

    image_first = models.FileField(verbose_name='Фото №1', upload_to='main_page/about/', max_length=500)
    image_second = models.FileField(verbose_name='Фото №2', upload_to='main_page/about/', max_length=500)
    image_third = models.FileField(verbose_name='Фото №3', upload_to='main_page/about/', max_length=500)

    def __str__(self):
        return 'Тизер компании'

    class Meta:
        verbose_name = '3 - Краткий тизер компании'
        verbose_name_plural = '3 - Краткий тизер компании'


class WhyBlock(models.Model):
    """
    Description of Block Model of Main Page App
    """

    title_first = models.CharField(verbose_name='Заголовок', max_length=500)
    description_first = models.CharField(verbose_name='Описание', max_length=500)

    title_second = models.CharField(verbose_name='Заголовок', max_length=500)
    description_second = models.CharField(verbose_name='Описание', max_length=500)

    title_third = models.CharField(verbose_name='Заголовок', max_length=500)
    description_third = models.CharField(verbose_name='Описание', max_length=500)

    title_fourth = models.CharField(verbose_name='Заголовок', max_length=500)
    description_fourth = models.CharField(verbose_name='Описание', max_length=500)

    title_fifth = models.CharField(verbose_name='Заголовок', max_length=500)
    description_fifth = models.CharField(verbose_name='Описание', max_length=500)

    title_sixth = models.CharField(verbose_name='Заголовок', max_length=500)
    description_sixth = models.CharField(verbose_name='Описание', max_length=500)

    def __str__(self):
        return 'Блок "Почему мы?"'

    class Meta:
        verbose_name = '4 - Почему мы?'
        verbose_name_plural = '4 - Почему мы?'


class RequestBlock(models.Model):
    """
    Description of RequestBlock Model of Main Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)

    image = models.FileField(verbose_name='Фото', upload_to='main_page/request/', max_length=500)

    def __str__(self):
        return 'Блок заявки'

    class Meta:
        verbose_name = '5 - Блок заявки'
        verbose_name_plural = '5 - Блок заявки'


class StagesBlock(models.Model):
    """
    Description of StagesBlock Model of Main Page App
    """

    title_first = models.CharField(verbose_name='Заголовок', max_length=500)
    description_first = models.CharField(verbose_name='Описание', max_length=500)

    title_second = models.CharField(verbose_name='Заголовок', max_length=500)
    description_second = models.CharField(verbose_name='Описание', max_length=500)

    title_third = models.CharField(verbose_name='Заголовок', max_length=500)
    description_third = models.CharField(verbose_name='Описание', max_length=500)

    title_fourth = models.CharField(verbose_name='Заголовок', max_length=500)
    description_fourth = models.CharField(verbose_name='Описание', max_length=500)

    title_fifth = models.CharField(verbose_name='Заголовок', max_length=500)
    description_fifth = models.CharField(verbose_name='Описание', max_length=500)

    image_first = models.FileField(verbose_name='Фото №1', upload_to='main_page/stages/', max_length=500)
    image_second = models.FileField(verbose_name='Фото №2', upload_to='main_page/stages/', max_length=500)

    def __str__(self):
        return 'Этапы создания мебели'

    class Meta:
        verbose_name = '6 - Этапы создания мебели'
        verbose_name_plural = '6 - Этапы создания мебели'


class DeliveryBlock(models.Model):
    """
    Description of DeliveryBlock Model of Main Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description_first = models.CharField(verbose_name='Описание №1', max_length=500)
    description_second = models.CharField(verbose_name='Описание №2', max_length=500)

    def __str__(self):
        return 'Доставка'

    class Meta:
        verbose_name = '7 - Доставка'
        verbose_name_plural = '7 - Доставка'


# class SolutionsBlock(models.Model):
#     """
#     Description of SolutionsBlock Model of Main Page App
#     """
#
#     image = models.FileField(verbose_name='Фото', upload_to='main_page/solutions/', max_length=500)
#
#     order = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#     )
#
#     def __str__(self):
#         return 'Решения наших клиентов'
#
#     class Meta:
#         verbose_name = '10 - Решения наших клиентов'
#         verbose_name_plural = '10 - Решения наших клиентов'


# class ReviewsBlock(models.Model):
#     """
#     Description of Block Model of Main Page App
#     """
#
#     name = models.CharField(verbose_name='Имя автора', max_length=500)
#     review = models.CharField(verbose_name='Отзыв', max_length=5000)
#     image = models.FileField(verbose_name='Фото автора', upload_to='main_page/reviews/', max_length=500, blank=True)
#
#     order = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#     )
#
#     def __str__(self):
#         return 'Отзывы'
#
#     class Meta:
#         verbose_name = '8 - Отзывы'
#         verbose_name_plural = '8 - Отзывы'


# class QuestionsBlock(models.Model):
#     """
#     Description of QuestionsBlock Model of Main Page App
#     """
#
#     question = models.CharField(verbose_name='Вопрос', max_length=500)
#     answer = models.CharField(verbose_name='Ответ', max_length=5000)
#
#     order = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#     )
#
#     def __str__(self):
#         return 'Частые вопросы'
#
#     class Meta:
#         verbose_name = '12 - Частые вопросы'
#         verbose_name_plural = '12 - Частые вопросы'


# class AddQuestionBlock(models.Model):
#     """
#     Description of AddQuestionBlock Model of Main Page App
#     """
#
#     title = models.CharField(verbose_name='Заголовок', max_length=500)
#     description = models.CharField(verbose_name='Описание', max_length=5000)
#
#     def __str__(self):
#         return 'Блок "Остались вопросы?"'
#
#     class Meta:
#         verbose_name = '13 - Блок "Остались вопросы?"'
#         verbose_name_plural = '13 - Блок "Остались вопросы?"'


class ContactsBlock(models.Model):
    """
    Description of ContactsBlock Model of Main Page App
    """

    number = models.CharField(verbose_name='Номер телефона', max_length=255)
    mail = models.CharField(verbose_name='Почта', max_length=255)
    whatsapp_link = models.CharField(verbose_name='ссылка на Whatsapp', max_length=255)
    tg_link = models.CharField(verbose_name='ссылка на Telegram', max_length=255)

    image_first = models.FileField(verbose_name='Фото №1', upload_to='main_page/contacts/', max_length=500)
    image_second = models.FileField(verbose_name='Фото №2', upload_to='main_page/contacts/', max_length=500)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = '8 - Контакты'
        verbose_name_plural = '8 - Контакты'
