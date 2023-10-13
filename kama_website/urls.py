"""
URL configuration for kama_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.main_page import views as main_page_views
from pages.delivery_page import views as delivery_page_views
from core.service import views as service_views
from core.catalog import views as catalog_views

admin.site.site_header = 'Панель управления сайта Кама'
admin.site.site_title = 'Кама'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/main_page/', main_page_views.aggregate_data, name='main_page'),
    path('api/v1/delivery_page/', delivery_page_views.aggregate_data, name='delivery_page'),
    path('api/v1/get_layout/', main_page_views.get_layout_data, name='get_header'),

    path('api/v1/service/', service_views.aggregate_data, name='service'),
    path('api/v1/reviews/', service_views.get_reviews, name='reviews'),


    path('api/v1/sofas/', catalog_views.SofaListView.as_view(), name='sofa_list'),
    path('api/v1/sofas/<int:pk>/', catalog_views.SofaDetailView.as_view(), name='sofa_detail'),

    path('api/v1/create_order/', service_views.create_order, name='create_order'),
    path('api/v1/create_review/', service_views.create_review, name='create_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
