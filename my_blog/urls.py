

from django.contrib import admin
from django.urls import path,include
from blog.views import detail , home , test,search
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home,name="home"),
     path('article/<int:id_article>',detail,name="detail"),
     path('article/recherche',search,name="search"),
      path('auth/',include("app_auth.urls")),

     path('test/',test,name="test")
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
