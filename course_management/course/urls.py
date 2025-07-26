from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, InstructorViewSet, CourseViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('instructors', InstructorViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
