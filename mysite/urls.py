"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import main_view, rate_image

=======
from django.urls import path,include
>>>>>>> 9502574 (retake)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
<<<<<<< HEAD
    path('rate/', rate_image, name='rate-view'),
=======
>>>>>>> 9502574 (retake)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)