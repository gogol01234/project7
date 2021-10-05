
from django.urls import path, include
from app1 import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("register/", views.user_register, name = "register"),
    path("accounts/login/", views.user_login, name = "login"),
    path("practice/", views.practice, name = "practice"),
    path("logout/", views.user_logout, name = "logout" ),
    path("post_blog/", views.post_blog, name = "post_blog"),
    path("blog_detail/<int:id>", views.blog_detail, name = "blog_detail"),
    path("delete_post/<int:id>", views.delete_post, name = "delete_post"),
    path("edit/<int:id>", views.edit , name = "edit")
]
