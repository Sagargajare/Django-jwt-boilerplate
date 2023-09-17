DJOSER = {
    "USER_ID_FIELD": "email",
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SITE_NAME = "django-drf-boilerplate"
