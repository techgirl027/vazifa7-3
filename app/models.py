from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    comment = models.TextField()

    def __str__(self) -> str:
        return self.name
