import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

#! ========== STATIC FILES ==========
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
STATIC_URL = "static/"
MEDIA_URL = "media/"
STATIC_ROOT = BASE_DIR / STATIC_URL
MEDIA_ROOT = BASE_DIR / MEDIA_URL

#!============ EMAIL =============
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_EMAIL")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS", True))
EMAIL_USE_SSL = bool(os.getenv("EMAIL_USE_SSL", False))
EMAIL_TOKEN_EXPIRE_MINUTES = int(os.environ.get("EMAIL_TOKEN_EXPIRE_MINUTES", 5))


#! ========== ENV VARIABLES ==========

#! ENVIRONMENT = development | testing | production

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ENVIRONMENT = os.getenv("ENVIRONMENT")
DEBUG = ENVIRONMENT in ["development", "testing"]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

#! ========== LOCALIZATION ==========

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


#! ========== CORS ==========
# CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS").split(",")
CORS_ALLOW_ALL_ORIGINS = True

# CSRF_TRUSTED_ORIGINS = [
#     "http://62.113.110.170:8090",
#     "http://62.113.110.170.7000",
#     "http://localhost:8090",
#     "http://localhost:80",
#     "http://localhsot",
# ]


#! ========== DJANGO SETTINGS ==========
WSGI_APPLICATION = "src.config.wsgi.application"
ASGI_APPLICATION = "src.config.asgi.application"
ROOT_URLCONF = "src.config.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "authorization.User"

#! ========== APPLICATIONS ==========


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "drf_spectacular",
    "django",
    "rest_framework_simplejwt",
    "corsheaders",
    # Local apps
    "src.apps.auth",
    "src.apps.api",
    "src.apps.gallery",
    "src.apps.common",
    "src.apps.category",
    "src.apps.product",
]


#! ========== MIDDLEWARE ==========


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


#! ========== DATABASES ==========


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


#! ========== INTERNATIONALIZATION ==========


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


#! ========== AUTHENTICATION ==========


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "TOKEN_OBTAIN_SERIALIZER": None,
    "TOKEN_REFRESH_SERIALIZER": None,
    "TOKEN_VERIFY_SERIALIZER": None,
    "TOKEN_BLACKLIST_SERIALIZER": None,
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": None,
    "SLIDING_TOKEN_REFRESH_SERIALIZER": None,
    "ISSUER": "http://localhost:8080/realms/master",
}


#! ========== DOCS ==========


SPECTACULAR_SETTINGS = {
    "TITLE": "Your API",
    "DESCRIPTION": "API schema",
    "VERSION": "1.0.0",
    "SERVE_PUBLIC": True,
}
