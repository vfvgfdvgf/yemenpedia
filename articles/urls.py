from django.urls import path, include
from . import views
from django.conf import settings             # استيراد settings
from django.conf.urls.static import static   # استيراد static

app_name = 'articles'

urlpatterns = [
    path('', views.article_list_view, name='article_list'),

    path('article/<int:pk>/', views.article_detail_view, name='article_detail'),

    path('article/<int:pk>/<slug:slug>/', views.article_detail_view, name='article_detail'),

    path('dashboard/', include('dashboard.urls')),

    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('categories/', views.categories_list_view, name='categories_list'),
    path('about/', views.about_view, name='about'),
    path('terms/', views.terms_view, name='terms'),
    path('faq/', views.faq_view, name='faq'),
    path('category/<slug:slug>/', views.category_article_list_view, name='category_articles'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
