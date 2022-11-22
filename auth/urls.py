from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    # path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', views.logout_view, name= "logout"),
    path('account/<int:id>', views.account, name= "account"),
    path('updaterecord/<int:id>', views.updaterecord, name= "updaterecord"),
    path('forgot', views.forgot_view, name= "forgot"),
    path('change-password/<int:id>', views.change_password, name= "change-password"),
]


