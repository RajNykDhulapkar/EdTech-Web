from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from college.models import *


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                '   must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # college details
    college = models.ForeignKey(
        College, on_delete=models.DO_NOTHING, related_name="students", blank=True, null=True)
    branch = models.ForeignKey(
        Branch, on_delete=models.DO_NOTHING, related_name="students", blank=True, null=True)
    year = models.ForeignKey(
        Year, on_delete=DO_NOTHING, related_name="students", blank=True, null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if not self.branch is None and not self.college in self.branch.colleges.all():
            raise Exception(
                "You must select one of the branch from your own college")
        super(User, self).save(force_insert, force_update, *args, **kwargs)

    def __str__(self):
        return self.username
