from django.urls import path, re_path

from . import views

urlpatterns = [
    path("ShardList/", views.shardList, name="shardlist"),
    path("AuthLogin", views.login, name="authlogin"),
    path("", views.index, name="index"),
]
