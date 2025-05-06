from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, BookViewSet
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
