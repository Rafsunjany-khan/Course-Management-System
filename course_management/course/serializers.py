from rest_framework import serializers
from .models import Course, Category, Instructor

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email']

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    instructors = InstructorSerializer(many=True, read_only=True)
    instructor_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Instructor.objects.all(), source='instructors', write_only=True
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'category',
            'category_id',
            'instructors',
            'instructor_ids',
        ]
