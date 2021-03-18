"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from blog import views

app_name = "app"

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.reg,name="register"),
    path('otp/',views.otp_verify,name="otp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),

    path('addprofile/',views.user_profile,name="profile"),
    path('new_post/',views.PostCreateView.as_view(), name='create_post'),
    path('new_post/<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),
    path('post/drafts/',views.DarftListView.as_view(), name= 'post_draft'),
    path('post/published/',views.PostListView.as_view(), name= 'post_list'),
    path('publish/<int:pk>', views.post_publish, name= 'publish'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name= 'update'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name= 'delete'),
    path('add_comment/<int:pk>', views.addcomment, name= 'add_comment'),
]