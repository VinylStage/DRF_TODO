from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializer import UserSerializer
# Create your views here.


class UserView(APIView):
    # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "welcome"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
