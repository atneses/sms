from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.verification.models import VerificationCode
from apps.verification.serializers import PhoneSerializer


# Create your views here.
class GetVerificationCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = PhoneSerializer(data=request.data)
        if not phone.is_valid():
            raise ValidationError(self.error_message(request.data['phone']))

        self.look_for_old_codes(request.data['phone'])
        code = VerificationCode(for_phone=request.data['phone'])
        code.save()

        return Response(self.verification_message(code.code), status=status.HTTP_200_OK)

    def verification_message(self, code):
        message = f'Hi! Your verification code for Rever is <{code}>'
        return message

    def error_message(self, phone):
        message = {'message': f'"{phone}" is not a valid phone'}
        return message

    def look_for_old_codes(self, phone):
        codes = VerificationCode.objects.filter(for_phone__exact=phone).filter(valid=True).all()
        codes.update(valid=False)


class VerifyCode(APIView):
    permission_classes = [AllowAny]
    # region ERROR STRINGS
    ERROR_EMPTY_CODE = 'Code cannot be empty'
    ERROR_INVALID_CODE = 'Invalid code'
    ERROR_INVALID_FORMAT = 'Code has an invalid format'

    ERROR_NOT_SAME = 'Hi, the verification code does not match the one we sent to you. Please try again'
    # endregion

    def get(self, request, code=None):
        if not code:
            return Response(self.ERROR_EMPTY_CODE, status=status.HTTP_406_NOT_ACCEPTABLE)

        if len(code) < 4 or len(code) > 4:
            return Response(self.ERROR_INVALID_CODE, status=status.HTTP_400_BAD_REQUEST)

        vc = VerificationCode.objects.filter(code=code).filter(valid=True).first()
        if not vc:
            return Response(self.ERROR_NOT_SAME, status=status.HTTP_400_BAD_REQUEST)

        if vc and vc.valid:
            vc.valid = False
            vc.save()
            return Response('Hi, you have been verified!', status=status.HTTP_200_OK)
        else:
            return Response(self.ERROR_INVALID_CODE, status=status.HTTP_400_BAD_REQUEST)


class ResendVerificationCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = PhoneSerializer(data=request.data)
        if not phone.is_valid():
            raise ValidationError(self.error_message(request.data['phone']))

        code = VerificationCode.objects\
            .filter(for_phone=request.data['phone'])\
            .filter(valid=True)\
            .first()
        if code:
            return Response(self.verification_message(code.code), status=status.HTTP_200_OK)
        return Response('There is not a valid verification code')

    def error_message(self, phone):
        message = {'message': f'"{phone}" is not a valid phone'}
        return message

    def verification_message(self, code):
        message = f'Hi! Your verification code for Rever is <{code}>'
        return message