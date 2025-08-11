from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ArticleForm, CategoryForm, UserForm
from articles.models import Article, Category
from core.models import Task

def is_owner_user(user):
    return user.groups.filter(name='Owner').exists()

@login_required
def article_list(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية للدخول لهذه الصفحة.")
        return redirect('dashboard:task_list')
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'dashboard/article_list.html', {'articles': articles})

@login_required
def article_create(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إنشاء المقال بنجاح.")
            return redirect('dashboard:article_list')
    else:
        form = ArticleForm()
    return render(request, 'dashboard/article_form.html', {'form': form, 'title': 'إضافة مقال جديد'})

@login_required
def article_edit(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')

    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل المقال.")
            return redirect('dashboard:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'dashboard/article_form.html', {'form': form, 'title': 'تعديل مقال'})

@login_required
def article_delete(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')

    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "تم حذف المقال.")
        return redirect('dashboard:article_list')
    return render(request, 'dashboard/article_confirm_delete.html', {'article': article})

# --- نفس الشيء للتصنيفات ---

@login_required
def category_list(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إنشاء التصنيف.")
            return redirect('dashboard:category_list')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category_form.html', {'form': form, 'title': 'إضافة تصنيف جديد'})

@login_required
def category_edit(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل التصنيف.")
            return redirect('dashboard:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/category_form.html', {'form': form, 'title': 'تعديل تصنيف'})

@login_required
def category_delete(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "تم حذف التصنيف.")
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/category_confirm_delete.html', {'category': category})

# --- إدارة المستخدمين ---

@login_required
def user_list(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    users = User.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})

@login_required
def user_create(request):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "تم إنشاء المستخدم.")
            return redirect('dashboard:user_list')
    else:
        form = UserForm()
    return render(request, 'dashboard/user_form.html', {'form': form, 'title': 'إضافة مستخدم جديد'})

@login_required
def user_edit(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل المستخدم.")
            return redirect('dashboard:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'dashboard/user_form.html', {'form': form, 'title': 'تعديل مستخدم'})

@login_required
def user_delete(request, pk):
    if not is_owner_user(request.user):
        messages.error(request, "ليس لديك صلاحية.")
        return redirect('dashboard:task_list')
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "تم حذف المستخدم.")
        return redirect('dashboard:user_list')
    return render(request, 'dashboard/user_confirm_delete.html', {'user': user})


from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    # لو عندك موديل Task مثلا
    tasks = Task.objects.all()  # لازم تستورد موديل Task
    return render(request, 'dashboard/task_list.html', {'tasks': tasks})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'dashboard/profile.html', {'user': user})
