from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança - variáveis de ambiente
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Render adiciona o host automaticamente, mas você pode colocar o domínio fixo depois
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meuapp',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Necessário para servir estáticos no Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # Cuidado ao desativar CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meuprojeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'meuapp', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meuprojeto.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'

# Aqui é seguro apontar para uma pasta "static" na raiz
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'meuapp','static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise: compressão e cache para produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSRF confiáveis - adicione depois a URL final do Render
CSRF_TRUSTED_ORIGINS = [
    'https://8024575c-bbe4-44bd-953e-0e428f28b7c2-00-2kzb45teblkn7.riker.replit.dev',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://seuapp.onrender.com',
]

# Configurações PWA
PWA_APP_NAME = 'Meu Sistema de Vendas'
PWA_APP_DESCRIPTION = "Sistema de Vendas Django - PWA"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {'src': '/static/icons/icon-192x192.png', 'sizes': '192x192'},
    {'src': '/static/icons/icon-512x512.png', 'sizes': '512x512'}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'pt-BR'
