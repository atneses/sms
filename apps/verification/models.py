import random
from django.db import models


# Create your models here.
def sending_verification_algorithm():
    numbers = '0123456789'
    random.choices(numbers, k=4)
    return ''.join(random.choices(numbers, k=4))


class BaseModel(models.Model):
    """
    Abstract base class to include created and modified field to all model
    that inherited from it.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VerificationCode(BaseModel):
    code = models.CharField(max_length=4, default=sending_verification_algorithm)
    valid = models.BooleanField(default=True)
    for_phone = models.CharField(max_length=20)

    class Meta:
        pass

    def __str__(self):
        return f'{self.code}'
