from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/blogs/',include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

#this code will handle react routing
urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]
