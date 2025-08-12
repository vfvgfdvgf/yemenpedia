from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps import views
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article, Category


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.pub_date


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            'article_list',      # الصفحة الرئيسية للمقالات
            'categories_list',   # قائمة التصنيفات
            'about',             # صفحة "عن الموقع"
            'privacy_policy',    # سياسة الخصوصية
            'terms',             # شروط الاستخدام
            'faq',               # الأسئلة الشائعة
            'contact',           # اتصل بنا
        ]

    def location(self, item):
        return reverse(item)


# دمج جميع الـ Sitemaps
sitemaps = {
    'articles': ArticleSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
}
