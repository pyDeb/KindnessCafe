from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if (post_data['first_name'].isalpha()) == False:
            if len(post_data['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (post_data['last_name'].isalpha()) == False:
            if len(post_data['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(post_data['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(post_data['password']) < 8:
            errors['password'] = "Password is too short!"
        if User.objects.filter(email=post_data['email']).count() > 0:
            errors['email'] = "The email address exists. If you are a user please log in!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()