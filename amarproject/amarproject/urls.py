
from django.contrib import admin
from django.urls import path, include
from student.views import page1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', page1, name='page1'),
    path('blog/', include('blog_post.urls'), name='blog'),
    path('mess/', include('cost_management.urls'), name='mess'),
    path('user/', include('user_info.urls'), name='user'),
]
