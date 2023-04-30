from rest_framework.views import APIView
from rest_framework import serializers
from users.models import User
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "gender", "age", "introduction", "date_of_birth")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # 회원가입시 암호화
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        birth = str(user.date_of_birth)[:4]
        nowtime = str(timezone.now())[:4]
        agenow = int(nowtime) - int(birth)
        user.age = +agenow
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        token["gender"] = user.gender
        token["age"] = user.age

        return token
