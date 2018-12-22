
from django.contrib import admin
from django.urls import path, include
from student.views import page1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_post.urls'), name=''),
    path('mess/', include('cost_management.urls'), name=''),
    path('page1/', page1, name='page1'),

]
