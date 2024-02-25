from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", login_required(views.Home.as_view()), name="home"),
    path("Register/", views.Registration.as_view(), name="register"),
    path("Login/", views.LoginV.as_view(), name="login"),
    path("Post<int:id>/", login_required(views.PostPage.as_view()), name="postt"),
    path("Postcreate/", login_required(views.PostCreate.as_view()), name="post_create"),
    path("User<int:user_id>/<name>/", login_required(views.UserProfils.as_view()), name="user_profils"),
    path("Myprofil/<name>/", login_required(views.MyProfil.as_view()), name="my_profil"),
    path("Suc/", login_required(views.UserSuc.as_view()), name="user_suc"),
    path("Usersett/", login_required(views.UserSetting.as_view()), name="user_sett"),
    path("Users/", login_required(views.UserSecurity.as_view()), name="user_secutity"),
    path("Modifikations/", login_required(views.UserMod.as_view()), name="mod_settings"),
    path("Personal/", login_required(views.UserPersonal.as_view()), name="personal_settings"),
    path("Logout/", views.Logout.as_view(), name="logout"),
    path("Rec/", views.Recomendation.as_view(), name="rec")
    ]