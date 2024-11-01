import os
from pathlib import Path
import dj_database_url  # Verifique se esta biblioteca está instalada

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta (mantenha-a segura em produção)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-mlds^g_)x*t1&a^jeb6n!-x)uyngnkk1btdn=yxp$%-w7&&716')

# Modo de depuração (não use DEBUG=True em produção)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = ['*']  # Qualquer host para desenvolvimento

# Configurações dos aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'barbara_app',  # Seu aplicativo
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração das URLs principais
ROOT_URLCONF = 'barbara.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Aplicação WSGI
WSGI_APPLICATION = 'barbara.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Adicione esta linha
        'NAME': os.environ.get('DB_NAME', 'railway'),  # O nome do seu banco de dados
        'USER': os.environ.get('DB_USER', 'postgres'),  # Seu usuário
        'PASSWORD': os.environ.get('DB_PASSWORD', 'zXlnsaSBPTswuernHFrjqvOuKgHsMFSE'),  # Sua senha
        'HOST': os.environ.get('DB_HOST', 'postgres.railway.internal'),  # O host do seu banco
        'PORT': os.environ.get('DB_PORT', '5432'),  # A porta do seu banco
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Tipo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
