from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class SendingVerificationAlgorithmTest(APITestCase):
    sending_url = reverse('sms:sending-verification-algorithm')

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
            response = self.client.post(self.sending_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_phones(self):
        invalid_phone = ['I’m a phone number', '123123', '551049abcd']
        url = reverse('sms:sending-verification-algorithm')
        for phone in invalid_phone:
            data = {'phone': f'{phone}'}
            response = self.client.post(self.sending_url, data, formar='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)