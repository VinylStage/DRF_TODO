from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(
        self, username, introduction, email, date_of_birth, gender, password=None
    ):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            introduction=introduction,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, date_of_birth, gender, introduction, password=None
    ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            introduction=introduction,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"
        TRANSMSCULINE = "TMC", "트랜스매스큘린"
        TRANSFEMININE = "TFM", "트랜스페미닌"
        ANDROGYNE = "ANG", "안드로진"
        BIGENDER = "BIG", "바이젠더"
        DEMIGENDER = "DEMG", "데미젠더"
        AGENDER = "AG", "에이젠더"
        GENDERLESS = "GL", "젠더리스"
        NEUTROIS = "NT", "뉴트로이스"
        TRIGENDER = "TG", "트라이젠더"
        POLYGENDER = "PG", "폴리젠더"
        PANGENDER = "PNG", "펜젠더"
        GENDERFLUID = "GF", "젠더플루이드"
        GENDERFLUX = "GFX", "젠더플럭스"
        ECT = "ECT", "기타"
        REFUSAL_TO_RESPOND = "RTR", "응답거부"

    username = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255, blank=True)
    gender = models.CharField(choices=GenderChoices.choices, max_length=255, blank=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "date_of_birth", "gender", "introduction"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
