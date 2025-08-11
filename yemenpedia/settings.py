from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mb)@-w@en50p52b4qjj4(v(7=5*6jr5mt4$&bemzolla*+1#w-'
DEBUG = False
ALLOWED_HOSTS = ['yemenpedia-4.onrender.com']

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',                # تفعيل لوحة الإدارة
    'django.contrib.auth',                 # مطلوب لنظام المستخدمين
    'django.contrib.sessions',             # ضروري لدعم الجلسات
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',             # لدعم خريطة الموقع sitemap
    'articles.apps.ArticlesConfig',
    'contact.apps.ContactConfig',
    'core',
    'dashboard',
]

LOGIN_REDIRECT_URL = '/dashboard/profile/'  # مسار صفحة البروفايل الجديدة

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # يجب أن يكون قبل MessageMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # مهم للادمن والمصادقة
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yemenpedia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',       # ضروري للادمن
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'articles.context_processors.categories_processor',
                'core.context_processors.unread_notifications_count',  # جديد
            ],
        },
    },
]

WSGI_APPLICATION = 'yemenpedia.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# إعدادات الملفات الثابتة (Static files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]   # مجلد ملفات static في المشروع
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')     # المجلد الذي سيجمع فيه collectstatic كل ملفات static

# إعدادات ملفات الوسائط (Media files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'halax.7y7@gmail.com'
EMAIL_HOST_PASSWORD = 'yqvw ahpp bavg pwvl'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
