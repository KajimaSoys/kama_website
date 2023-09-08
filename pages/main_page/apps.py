from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages.main_page'
    verbose_name = 'Главная страница'

    # def ready(self):
    #     from django.contrib import admin
    #     from django.contrib.admin import sites
    #
    #     # FIXME Сделать так, чтобы модели не объединялись
    #     class MyAdminSite(admin.AdminSite):
    #         def get_app_list(self, request, app_label=None):
    #             all_list = super().get_app_list(request)
    #             """
    #             Return a sorted list of all the installed apps that have been
    #             registered in this site.
    #             """
    #             ordering = {
    #                 "1 - Навигационная панель": 1,
    #                 "2 - Главный блок": 2,
    #                 "3 - Тизер каталога": 3,
    #                 "4 - Популярные модели": 4,
    #                 "5 - Преимущество": 5,
    #                 "6 - Почему мы?": 6,
    #                 "7 - Блок заявки": 7,
    #                 "8 - Этапы создания мебели": 8,
    #                 "9 - Доставка": 9,
    #                 "10 - Решения наших клиентов": 10,
    #                 "11 - Отзывы": 11,
    #                 "12 - Частые вопросы": 12,
    #                 "13 - Блок \"Остались вопросы?\"": 13,
    #                 "14 - Контакты": 14,
    #                 "Группы": 15,
    #                 "Пользователи": 16
    #             }
    #             app_dict = self._build_app_dict(request)
    #             # a.sort(key=lambda x: b.index(x[0]))
    #             # Sort the apps alphabetically.
    #             app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    #
    #             # Sort the models alphabetically within each app.
    #             for app in app_list:
    #                 app['models'].sort(key=lambda x: ordering[x['name']])
    #
    #             return app_list
    #
    #     mysite = MyAdminSite()
    #     admin.site = mysite
    #     sites.site = mysite
