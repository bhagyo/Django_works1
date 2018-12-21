
from django.contrib import admin
from django.urls import path, include
from student.views import page1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_post.urls'), name='home'),
    path('page1/', page1, name='page1'),
]
