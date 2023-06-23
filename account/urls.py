from django.urls import path
from account import views


urlpatterns = [
    path('api/register/',views.UserRegisterView.as_view(),name="register"),
    path('api/login/',views.UserLoginView.as_view(),name="login"),
    path('api/profile/',views.UserProfileView.as_view(),name="profile"),
    path('api/changepassword/',views.UserChangePasswordView.as_view(),name="changepassword"),
    # path('api/logout/',views.UserLogoutView.as_view(),name="logout")

]