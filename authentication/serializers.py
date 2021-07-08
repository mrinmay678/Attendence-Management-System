from rest_framework import serializers
from .models import CustomUser
from teacher.models import Teacher
from student.models import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["jis_id","password"]

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ["name","email","phone","department"]

class MentorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ["id", "name", "email", "department"]

class StudentSerializer(serializers.ModelSerializer):
    
    # mentor = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["name","email","phone","department","batch","year","semester"]

    # def get_mentor(self, obj):
    #     return MentorSerializer(obj.mentor).data