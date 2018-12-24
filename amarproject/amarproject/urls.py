
from django.contrib import admin
from django.urls import path, include
from student.views import page1
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('page1/', page1, name='page1'),
    ##all user_details
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

    path('blog/', include('blog_post.urls'), name='blog'),

    path('mess/', include('cost_management.urls'), name='mess'),

    path('info/', include('information.urls'), name='info'),

    path('user/', include('user_info.urls'), name='user'),
]
