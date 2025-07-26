from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Category, Instructor, Course
from .serializers import CategorySerializer, InstructorSerializer, CourseSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAdminUser]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Public access to list and detail views
        return [IsAdminUser()]  # Admin only for create, update, delete
