from django.urls import path
from accounts.views import register_view, UserDetailView, UserListView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('list/', UserListView.as_view(), name='user-list')
]