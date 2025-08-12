from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from articles.sitemaps import ArticleSitemap, CategorySitemap

# **هنا أضف السطر التالي لاستيراد auth_views**
from django.contrib.auth import views as auth_views

sitemaps = {
    'articles': ArticleSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),  # لوحة الإدارة
    path('', include(('articles.urls', 'articles'), namespace='articles')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
  
    path('dashboard/', include('dashboard.urls')),  # لوحة التحكم

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
