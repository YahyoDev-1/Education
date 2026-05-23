from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(
        slug_field='name',
        queryset=Course.objects.all(),
        many=True,
    )
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'degree', 'phone', 'birth_date', 'kpi', 'course')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    groups = SlugRelatedField(
        slug_field='name',
        queryset=Group.objects.all(),
        many=True,
    )
    class Meta:
        model = Student
        fields = ('id', 'name', 'birth_date', 'phone', 'is_active', 'created_at', 'groups' )

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
