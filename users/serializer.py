from rest_framework.views import APIView
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # 비밀번호 암호화
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


# 회원가입
# 로그인
# 회원정보수정
# 팔로우
