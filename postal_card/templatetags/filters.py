from django import template

register = template.Library()

EN_TO_FA_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

@register.filter
def en2fa_digits(value):
    """تبدیل ارقام انگلیسی به فارسی در یک رشته"""
    if not isinstance(value, str):
        value = str(value)
    return value.translate(EN_TO_FA_DIGITS)