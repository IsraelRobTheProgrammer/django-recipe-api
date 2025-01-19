"""
All DB Models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifiers
    for authentication instead of usernames"""

    def create_user(self, email, password=None, **extra_field):
        """create,save and return a new user"""
        if not email:
            raise ValueError(("Users must have an email address."))
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_field):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        # extra_field.setdefault("is_staff", True)
        # extra_field.setdefault("is_superuser", True)
        # extra_field.setdefault("is_active", True)

        # if extra_field.get("is_staff") is not True:
        #     raise ValueError(("Superuser must have is_staff=True."))
        # if extra_field.get("is_superuser") is not True:
        #     raise ValueError(("Superuser must have is_superuser=True."))
        # return self.create_user(email, password, **extra_field)


class User(AbstractBaseUser, PermissionsMixin):
    """Our custome user in the system"""

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.name} email is {self.email}"
