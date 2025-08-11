from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # المهام - اذا عندك مهام تواصل على نفس الخط
    path('tasks/', views.task_list, name='task_list'),

    # المقالات
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/edit/<int:pk>/', views.article_edit, name='article_edit'),
    path('articles/delete/<int:pk>/', views.article_delete, name='article_delete'),

    # التصنيفات
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # المستخدمين
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/edit/<int:pk>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),

    # ملف البروفايل مثلاً
    path('profile/', views.profile_view, name='profile'),
]
