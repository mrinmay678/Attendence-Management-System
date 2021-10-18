from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import Candidate
from utils.security import authenticate
from tempfile import NamedTemporaryFile
import cv2
import face_recognition as fr
from PIL import Image
import os

class AttendanceView(APIView):
    @authenticate
    def post(self, request, slot=None):
        data=request.data
        cand=Candidate.objects.get(username=request.username)
        img = Image.open(data["pic"])
        img.save("media/new_img.jpg")
        actual=fr.load_image_file(cand.pic)
        img="media/new_img.jpg"
        actual=cv2.cvtColor(actual, cv2.COLOR_BGR2RGB)
        check=fr.load_image_file(img)
        check=cv2.cvtColor(check, cv2.COLOR_BGR2RGB)
        acFL=fr.face_locations(actual)[0]
        acEN=fr.face_encodings(actual)[0]
        chFL=fr.face_locations(check)[0]
        chEN=fr.face_encodings(check)[0]
        result = fr.compare_faces([acEN],chEN)
        
        return Response(data={
            "message":"Success",
            "Attendance":result,
            "status":True
        },status=200)