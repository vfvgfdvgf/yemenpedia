from django.contrib.sitemaps import Sitemap
from .models import Article, Category

class ArticleSitemap(Sitemap):
    changefreq = "daily"   # أو weekly حسب التحديث
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return obj.get_absolute_url()

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return f'/category/{obj.slug}/'
