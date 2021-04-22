from django.urls import path
from accounts.views import register_view, UserDetailView, UserListView, UserUpdateView, UserChangePasswordView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('profile/', UserUpdateView.as_view(), name='user-update'),
    path('change_password/', UserChangePasswordView.as_view(), name='user-change-password'),
]