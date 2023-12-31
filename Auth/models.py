from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email doit être spécifié.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Le superutilisateur doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Level(models.Model):
    slug = models.CharField(max_length=100)
    total_students = models.IntegerField(default=200)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.slug

    def serialize(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'total_students': self.total_students
        }


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_num = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_online = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_two_factor = models.BooleanField(default=False)
    two_factor_code = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    reset_token = models.CharField(max_length=255, null=True, blank=True)
    reset_token_expiration = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def is_reset_token_valid(self, token):
        return self.reset_token == token

    def is_reset_token_expired(self):
        return self.reset_token_expiration is not None and self.reset_token_expiration < timezone.now()

    def serialize(self):
        if not self.avatar:
            avatar = '/assets/avatars/blank.png'
        else:
            avatar = self.avatar.url

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_num': self.phone_num,
            'email': self.email,
            'avatar': avatar,
            'is_online': self.is_online,
        }
