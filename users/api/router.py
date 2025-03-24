from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.view import RegisterView, UserProfileUpdateView, UserView,UserListView
from users.api.view import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [
    #path('auth/register', RegisterView.as_view()),
    path('auth/login', CustomTokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),

   # path('user', UserApiViewSet.as_view(), name='user',basename='user'),
]
