from django.urls import path

from users.views import UserPageGuest

urlpatterns = [
    path('profile/<int:pk>', UserPageGuest.as_view(), name='profile-info'),
]
