"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import posts_view, main_page, posts_text_view, post_detail_view, post_create_view, TestView, PostListView, PostDetailView, PostCreateView
from user.views import register_view, login_view, logout_view, profile_view, profiles_view, profile_detail_view

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('posts/', posts_view, name = "posts"),
    path('posts2/', PostListView.as_view()),
    path('test/',TestView.as_view(), name = 'test' ),
    path('posts/', posts_text_view, name = 'text'),
    path('', main_page, name= 'main'),
    path('posts2/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:post_id>/', post_detail_view, name = 'post_detail'),
    path('posts2/create/', PostCreateView.as_view()),
    path('posts/create/', post_create_view, name = 'post_create'),
    path('register/', register_view, name = 'register_view'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/', profile_view, name = 'profile'),
    path('profiles/', profiles_view('user.urls')),
    path('profiles/<int:profile_id>/', profile_detail_view, name = "profiles")
])

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
