from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list_view, name='article_list'),

    # رابط لعرض تفاصيل المقالة بـ pk فقط
    path('article/<int:pk>/', views.article_detail_view, name='article_detail'),

    # رابط لعرض تفاصيل المقالة بـ pk و slug (لتحسين SEO)
    path('article/<int:pk>/<slug:slug>/', views.article_detail_view, name='article_detail'),

  

    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('categories/', views.categories_list_view, name='categories_list'),
    path('about/', views.about_view, name='about'),
    path('terms/', views.terms_view, name='terms'),
    path('faq/', views.faq_view, name='faq'),
    path('category/<slug:slug>/', views.category_article_list_view, name='category_articles'),
]
