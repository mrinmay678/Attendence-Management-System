from rest_framework import serializers
from .models import Teacher
from authentication.models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["jis_id"]

class TeacherSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["id", "user", "name","email","phone","department"]

    def get_user(self, obj):
        return UserSerializer(obj.jis_id).data