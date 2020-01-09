import random

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class SendingVerificationAlgorithmTest(APITestCase):
    getting_url = reverse('sms:get-verification-code')

    def test_sending_verification_code(self):
        phones = [
            '12-3456-7890',
            '1234567890',
            '12 3456 7890',
            '+52-12-3456-7890',
            '+521234567890',
            '+52 12 3456 7890'
        ]
        for phone in phones:
            data = {'phone': f'{phone}'}
            response = self.client.post(self.getting_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_phones(self):
        invalid_phone = ['I’m a phone number', '123123', '551049abcd']
        for phone in invalid_phone:
            data = {'phone': f'{phone}'}
            response = self.client.post(self.getting_url, data, formar='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VerifyCode(APITestCase):
    getting_url = reverse('sms:get-verification-code')

    def test_random_short_codes(self):
        # region Test empty verification code
        short_codes = [random.randint(a=100, b=999) for x in range(1, 10)]

        for code in short_codes:
            verify_code_url = reverse('sms:verify-code', kwargs={'code': f'{code}'})
            response = self.client.get(verify_code_url, None, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # region

    def test_random_long_codes(self):
        # region Test empty verification code
        short_codes = [random.randint(a=10000, b=99999) for x in range(1, 10)]

        for code in short_codes:
            verify_code_url = reverse('sms:verify-code', kwargs={'code': f'{code}'})
            response = self.client.get(verify_code_url, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # region

    def test_get_and_validate_code(self):
        response = self.client.post(self.getting_url, {'phone': '+523334958746'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.data)
        code = response.data
        start = code.find('<') + 1
        code = code[start: start + 4]

        verify_code_url = reverse('sms:verify-code', kwargs={'code': f'{code}'})
        response = self.client.get(verify_code_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
