
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f"Имя не может быть цифрами"),
            params={'value': value},
        )
    if not value.isalpha():
        raise ValidationError(
            _(f"Имя не может содержать цифры"),
            params={'value': value},
        )

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(_(f'Размер файла слишком большой'))
