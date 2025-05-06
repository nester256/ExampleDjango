"""
URL configuration for exam_example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import views as auth_views


from . import settings

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Описание вашего API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT"),
    ),
    permission_classes=[AllowAny],
    authentication_classes=[SessionAuthentication],
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include('test_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
