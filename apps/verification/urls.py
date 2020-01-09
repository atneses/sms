# -*- coding: utf-8 -*-
from django.urls import path

from apps.verification.views import SendingVerificationAlgorithm

urlpatterns = [
    path(
        'sending-verification-algorithm/',
        SendingVerificationAlgorithm.as_view(),
        name='sending-verification-algorithm'
    )
]
