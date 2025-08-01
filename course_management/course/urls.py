from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, InstructorViewSet, CourseViewSet
from rest_framework.authtoken.views import obtain_auth_token  # ✅ Add this line

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('instructors', InstructorViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('login/', obtain_auth_token),  # ✅ Add this line
    path('', include(router.urls)),
]
