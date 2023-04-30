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
        birth = str(user.date_of_birth)[:4]  # 생일에서 연도만 추출
        nowtime = str(timezone.now())[:4]  # 현재 날짜에서 연도만 추출
        agenow = int(nowtime) - int(birth)  # 정수변환 후 나이계산
        user.age = agenow  # 나이 저장
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
