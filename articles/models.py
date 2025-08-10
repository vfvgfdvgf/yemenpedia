from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم التصنيف")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="المعرف (Slug)")

    class Meta:
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="اسم الوسم")
    slug = models.SlugField(max_length=60, unique=True, verbose_name="المعرف (Slug)")

    class Meta:
        verbose_name_plural = "الوسوم"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقالة")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="المعرف (Slug)")
    content = models.TextField(verbose_name="محتوى المقالة")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True, verbose_name="صورة المقالة")
    is_published = models.BooleanField(default=True, verbose_name="منشور")
    views = models.PositiveIntegerField(default=0, verbose_name="عدد المشاهدات")
    author_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="اسم المؤلف")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="التصنيف")
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name="الوسوم")

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "مقالة"
        verbose_name_plural = "المقالات"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.pk, 'slug': self.slug})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="المقالة")
    name = models.CharField(max_length=80, verbose_name="الاسم")
    email = models.EmailField(blank=True, null=True, verbose_name="البريد الإلكتروني")
    body = models.TextField(verbose_name="التعليق")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    active = models.BooleanField(default=True, verbose_name="نشط")

    class Meta:
        ordering = ['created']
        verbose_name = "تعليق"
        verbose_name_plural = "التعليقات"

    def __str__(self):
        return f"تعليق بواسطة {self.name} على {self.article.title}"