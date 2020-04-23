from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
import uuid as uuid_lib

class Workspace(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    name = models.CharField(_('workspace'), max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('workspace')
        verbose_name_plural = _('workspace')

class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)

    email = models.EmailField(_('email'), 
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    username = models.CharField(_('username'), max_length=150, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []