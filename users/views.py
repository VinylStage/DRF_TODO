from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from users.serializer import UserSerializer, UserProfileSerializer
from users.models import User
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


class ProfileView(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class UserEditView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        if request.user == user:
            user = get_object_or_404(User, id=pk)
            serializer = UserProfileSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Edit Complete": f"${serializer.data}"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You don't have andy permission to edit this user", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        if request.user == user:
            user.delete()
            return Response("deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("You don't have andy permission to delete this user", status=status.HTTP_403_FORBIDDEN)


# class LogoutView(APIView):
#     def post(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
