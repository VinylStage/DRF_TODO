from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users import views
urlpatterns = [
    path('signup/', views.UserView.as_view(), name="signup"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', views.ProfileView.as_view(), name='ProfileView'),
    path('edit/<int:pk>/', views.UserEditView.as_view(), name='UserEditView'),

]
