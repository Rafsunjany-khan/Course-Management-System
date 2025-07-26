from rest_framework import serializers
from .models import Category, Instructor, Course

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested category for read
    instructors = InstructorSerializer(many=True, read_only=True)  # Nested instructors for read
    instructor_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Instructor.objects.all(),
        write_only=True,
        source='instructors'
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructors', 'instructor_ids']
