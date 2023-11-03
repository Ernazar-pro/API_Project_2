from rest_framework import serializers
from app.models import StudyCenter, Student, Teacher

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudyCenterSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudyCenter
        fields = '__all__'