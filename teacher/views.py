from authentication.utils import is_authenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class TeacherProfile(APIView):
    @is_authenticated
    def get(self, request):
        pass