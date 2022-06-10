from django.db import models

# Create your models here.

class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.EmailField(max_length=128, null=False)
    password = models.CharField(max_length=256, null=False)