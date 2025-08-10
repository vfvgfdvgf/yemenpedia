from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from articles.sitemaps import ArticleSitemap, CategorySitemap

sitemaps = {
    'articles': ArticleSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),  # لوحة الإدارة

    path('', include(('articles.urls', 'articles'), namespace='articles')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),

    # رابط خريطة الموقع
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  