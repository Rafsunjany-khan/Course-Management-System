from rest_framework import serializers
from .models import Category, Instructor, Course

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Instructor Serializer
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    # Read-only nested serializers
    category = CategorySerializer(read_only=True)
    instructors = InstructorSerializer(many=True, read_only=True)

    # Write-only fields for POST/PUT
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source='category'
    )
    instructor_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Instructor.objects.all(),
        write_only=True,
        source='instructors'
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'category',         # Read-only nested data
            'category_id',      # Write-only for incoming POST/PUT
            'instructors',      # Read-only nested data
            'instructor_ids'    # Write-only for incoming POST/PUT
        ]
