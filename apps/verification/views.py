from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.verification.serializers import PhoneSerializer


# Create your views here.
class SendingVerificationAlgorithm(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = PhoneSerializer(data=request.data)
        if not phone.is_valid():
            raise ValidationError(self.error_message(request.data['phone']))
        return Response(self.verification_message(1000))

    def verification_message(self, code):
        message = f'Hi! Your verification code for Rever is <{code}>'
        return message

    def error_message(self, phone):
        message = {
            'message': f'"{phone}" is not a valid phone'
        }
        return message
