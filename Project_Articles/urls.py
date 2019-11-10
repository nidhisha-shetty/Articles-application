"""Project_Articles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from articles.views import article_detail_display_view, article_detail_store_view, home_view, article_delete_view, article_list_view, article_list_delete_view,render_initial_data, article_list_render_data, main_home_view, guest_home_view, register, login, guest_article_list, guest_article_view, guest_article_create, guest_article_detail_display_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('article_details_display/', article_detail_display_view),
    path('article_details_display/<int:pass_id>/', article_detail_display_view, name='article-details-display-id'),
    path('article_details_create/', article_detail_store_view, name='article-detail-create'),
    path('article_details_delete/<int:pass_id>/', article_delete_view, name='article-details-delete-id'),
    path('article_list/', article_list_view, name='article-list'),
    path('article_list_delete/', article_list_delete_view, name='article-list-delete'),
    path('article_edit/<int:pass_id>/', render_initial_data, name='article-edit-id'),
    path('article_list_edit/', article_list_render_data, name='article-list-edit'),
    path("", main_home_view, name="home-page"),   
    path("admin_home_page/", home_view, name="admin_home_page"),
    path("guest_home_page/", guest_home_view, name="guest_home_view"), 
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("guest_article_view/", guest_article_view, name='guest_article_view'),
    path("guest_article_create/", guest_article_create, name="guest_article_create"),
    path("guest_article_display/<int:pass_id>/", guest_article_detail_display_view, name='guest_article-details-display-id' )
]
