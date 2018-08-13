from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name cannot be blank"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name cannot be blank"
        if not LETTERS_REGEX.match(postData['first_name']):
            errors['name'] = "First name can only be alphabets"
        if not LETTERS_REGEX.match(postData['last_name']):
            errors['name2'] = "Last name can only be alphabets"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        if User.objects.filter(email=postData['email']):
            errors['email2'] = "Email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        if not postData['password'] == postData['confirm_password']:
            errors['password2'] = "Passwords do not match"

        return errors

    def basic_validator2(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            if bcrypt.checkpw(postData['password'].encode(), user.first().password.encode()):
                return errors
        errors['password'] = "Invalid login"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
