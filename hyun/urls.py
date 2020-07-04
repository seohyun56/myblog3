from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name = 'index'),
    path('music/', blog.views.music, name = 'music'),
    path('photo/', blog.views.photo, name='photo'),
    path('visitors/', blog.views.visitors, name='visitors'),
    path('sns/', blog.views.sns, name='sns'),
    path('timetable/', blog.views.timetable, name='timetable'),
    path('visitors/createBlog/', blog.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('signup/', blog.views.signup, name='user_signup'),
    path('login/', blog.views.signin, name='user_login'),
    path('logout/', blog.views.signout, name='user_logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

