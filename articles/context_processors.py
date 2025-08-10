# articles/context_processors.py
from .models import Article, Category

def categories_processor(request):
    return {
        'articles': Article.objects.all(),
        'categories': Category.objects.all(),
    }
