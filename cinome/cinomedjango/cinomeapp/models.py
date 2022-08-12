from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=100)

    def _str_(self):
        return self.title


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    username = models.CharField(max_length=32, validators=[MinLengthValidator(4)], unique=True)
    image_url = models.FilePathField(blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    friends = models.ManyToManyField("User")


class ListType(models.Model):
    name = models.CharField(max_length=255)


class VisibilityType(models.Model):
    name = models.CharField(max_length=255)


class List(models.Model):
    list_type = models.ForeignKey(ListType, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    visibility_type = models.ForeignKey(VisibilityType, on_delete=models.RESTRICT)


class ElementType(models.Model):
    name = models.CharField(max_length=255)


class Element(models.Model):
    element_api = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    element_type = models.ForeignKey(ElementType, on_delete=models.RESTRICT)


class UserElement(models.Model):
    element = models.ForeignKey(Element, on_delete=models.RESTRICT)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    is_favorite = models.BooleanField(default=False)
    visibility_type = models.ForeignKey(VisibilityType, on_delete=models.RESTRICT)
    list = models.ForeignKey(List, on_delete=models.RESTRICT)


class TagItem(models.Model):
    user_element = models.ForeignKey(UserElement, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
