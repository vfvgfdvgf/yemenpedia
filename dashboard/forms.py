from django import forms
from articles.models import Article, Category
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # حذف 'pub_date' لأنه غير قابل للتعديل في الموديل
        fields = ['title', 'slug', 'content', 'category', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
            # حذفت 'pub_date' من الويجت لأنه غير موجود في الحقول
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'groups')
