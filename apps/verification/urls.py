# -*- coding: utf-8 -*-
from django.urls import path

from apps.verification.views import GetVerificationCode, VerifyCode, ResendVerificationCode

urlpatterns = [
    path(
        'get-verification-code/',
        GetVerificationCode.as_view(),
        name='get-verification-code'
    ),
    path('verify-code/<str:code>/', VerifyCode.as_view(), name='verify-code'),
    path('resend-code/', ResendVerificationCode.as_view(), name='resend-code')
]
