from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import token_decoder, payload
from .serializers import UserSerializer, CustomUser, Teacher, TeacherSerializer, StudentSerializer, Student
from django.contrib.auth.hashers import make_password

class Registration(APIView):
    def post(self, request):
        try:
            token=request.data.get('token')
            user_data=token_decoder(token)
            assert (user_data["jis_id"]!=None or user_data["password"]!=None), "Invalid ID or Password"
            userSerial = UserSerializer(data=user_data)
        
            if userSerial.is_valid():
                userSerial.save()
                
                del request.data["token"]
                if request.data.get("category")=='teacher':
                    del request.data["category"]
                    userSerial = TeacherSerializer(data=request.data)

                    if userSerial.is_valid():
                        userSerial.save()
                        obj1=Teacher.objects.get(email=request.data.get("email"))
                        obj1.user=CustomUser.objects.get(jis_id=user_data["jis_id"])
                        obj1.save()
                        
                else:
                    del request.data["category"]
                    mentor=CustomUser.objects.get(jis_id=request.data["mentor"])
                    del request.data["mentor"]
                    userSerial = StudentSerializer(data=request.data)

                    if userSerial.is_valid():
                        userSerial.save()
                        obj1=Student.objects.get(email=request.data.get("email"))
                        obj1.user=CustomUser.objects.get(jis_id=user_data["jis_id"])
                        obj1.mentor=Teacher.objects.get(user=mentor)
                        obj1.save()
                    
            return Response({"message":"Success", "status":True}, status=200)
            
        except Exception as e:
            return Response({"message":str(e), "status":False}, status=400)

class Login(APIView):
    def post(self, request):
        try:
            token=request.data.get('token')
            user_data=token_decoder(token)
            assert (user_data["jis_id"]!=None or user_data["password"]!=None), "Invalid ID or Password"
            if c:=CustomUser.objects.get(jis_id=user_data["jis_id"]):
                assert c["password"]==make_password(user_data["password"]), "Invalid ID or Password"
                if Teacher.objects.get(user=c):
                    user_data["category"]="teacher"
                else:
                    user_data["category"]="student"
                del user_data["password"]
                access, refresh = payload(user_data)
                data={
                    "access_token":access,
                    "refresh_token":refresh
                }
                return Response({"message":"Success", "data":data, "status":True}, status=200)
            return Response({"message":"Invalid ID or Password", "status":True}, status=401)

        except Exception as e:
            return Response({"message":str(e), "status":False}, status=400)
            