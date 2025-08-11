from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponsePermanentRedirect
from .forms import CommentForm
from .models import Article, Category, Comment

def article_list_view(request):
    articles = Article.objects.filter(is_published=True).order_by('-pub_date')

    # جلب كلمة البحث من الرابط
    search_query = request.GET.get('q', '')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        ).distinct()

    # الفلترة حسب التصنيف (اختياري)
    category_slug = request.GET.get('category')
    if category_slug:
        articles = articles.filter(category__slug=category_slug)

    # تقسيم المقالات لصفحات
    paginator = Paginator(articles, 10)  # 10 مقالات في كل صفحة
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'categories': Category.objects.all(),
        'current_category': category_slug
    }
    return render(request, 'articles/article_list.html', context)


def article_detail_view(request, pk, slug=None):
    article = get_object_or_404(Article, pk=pk, is_published=True)

    # إعادة التوجيه إذا السلاج غير صحيح
    if slug and article.slug != slug:
        return HttpResponsePermanentRedirect(article.get_absolute_url())

    # معالجة التعليقات
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            if request.user.is_authenticated:
                new_comment.user = request.user
            new_comment.save()
            return redirect(article.get_absolute_url())
    else:
        comment_form = CommentForm()

    # زيادة المشاهدات
    article.views += 1
    article.save()

    context = {
        'article': article,
        'related_articles': Article.objects.filter(
            category=article.category,
            is_published=True
        ).exclude(pk=article.pk)[:3],
        'comments': article.comments.filter(active=True),
        'comment_form': comment_form
    }
    return render(request, 'articles/article_detail.html', context)


def categories_list_view(request):
    categories = Category.objects.all()
    return render(request, 'articles/categories_list.html', {'categories': categories})


def category_article_list_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, is_published=True).order_by('-pub_date')

    # البحث داخل التصنيف
    search_query = request.GET.get('q', '')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'page_obj': page_obj,
        'search_query': search_query,
        'categories': Category.objects.all(),
        'subcategories': category.children.all() if hasattr(category, 'children') else None
    }
    return render(request, 'articles/category_articles.html', context)


def privacy_policy_view(request):
    return render(request, 'static_pages/privacy_policy.html')


def about_view(request):
    return render(request, 'static_pages/about.html')


def terms_view(request):
    return render(request, 'static_pages/terms.html')


def faq_view(request):
    return render(request, 'static_pages/faq.html')


# تسجيل دخول/خروج تجريبي (غير رسمي)
def fake_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        request.session['user'] = username  # حفظ اسم المستخدم في الجلسة
        return redirect('articles:article_list')
    return render(request, 'fake_login.html')

def fake_logout_view(request):
    request.session.pop('user', None)
    return redirect('articles:article_list')

from django.shortcuts import render

def custom_page_not_found(request, exception=None):
    return render(request, "404.html", status=404)
