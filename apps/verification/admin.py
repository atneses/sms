from django.contrib import admin

from apps.verification.models import VerificationCode


# Register your models here.
@admin.register(VerificationCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid', 'for_phone', 'created', 'modified']
