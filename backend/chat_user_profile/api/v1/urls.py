from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, VerificationCodeViewSet, ContactViewSet

router = DefaultRouter()
router.register("contact", ContactViewSet)
router.register("profile", ProfileViewSet)
router.register("verificationcode", VerificationCodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
