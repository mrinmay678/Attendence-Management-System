from rest_framework.response import Response
from rest_framework.views import APIView
from utils.tools import checkFields
from utils.security import payloadGenerator
from datetime import datetime
from .models import *

class OrganizationView(APIView):

    @checkFields(["name","email","password","confirm_password"])
    def register(self, request):
        data=request.data
        if data["password"]!=data["confirm_password"]:
            raise ValueError("Password Not Matched")
        try:
            org=Organization.objects.get(email=data["email"])
        except Exception as e:
            org=None
        if org:
            raise ValueError(f"{data['name']} already exists")
        org=Organization.objects.create(name=data["name"], username=data["email"].split('@')[0]+str(datetime.utcnow()), email=data["email"], password=data["password"])
        org.save()
        return Response(data={
            "message":"Success",
            "status":True
        },status=200)

    @checkFields(["email","password"])
    def login(self, request):
        data=request.data
        
        try:
            org=Organization.objects.get(email=data["email"])
        except Exception as e:
            org=None
        
        if not org:
            raise ValueError(f"{data['name']} donot exists")
        
        if not org.password==data['password']:
            raise ValueError('Invalid Credentials')

        print(org.username)
        return Response(data={
            "message":"Success",
            "data":payloadGenerator(org.username),
            "status":True
        },status=200)

    
    def post(self, request, service_type=None):
        try:
            if service_type=="register":
                return self.register(request)
            elif service_type=="login":
                return self.login(request)
        
        except Exception as e:
            return Response(data={
                "message":"Failed",
                "error":str(e),
                "status":False
            }, status=401)

class CandidateView(APIView):
    
    @checkFields(["name","email","organization","password","confirm_password"])
    def register(self, request):
        data=request.data
        if data["password"]!=data["confirm_password"]:
            raise ValueError("Password Not Matched")
        try:
            org=Candidate.objects.get(email=data["email"])
        except Exception as e:
            org=None
        if org:
            raise ValueError(f"{data['name']} already exists")
        organization=Organization.objects.get(username=data["organization"])
        org=Candidate.objects.create(name=data["name"], username=data["organization"]+str(datetime.utcnow()), email=data["email"], password=data["password"], organization=organization)
        org.save()
        return Response(data={
            "message":"Success",
            "status":True
        },status=200)

    @checkFields(["email","password"])
    def login(self, request):
        data=request.data
        
        try:
            org=Candidate.objects.get(email=data["email"])
        except Exception as e:
            org=None
        
        if not org:
            raise ValueError(f"{data['name']} donot exists")
        
        if not org.password==data['password']:
            raise ValueError('Invalid Credentials')

        return Response(data={
            "message":"Success",
            "data":payloadGenerator(org.username),
            "status":True
        },status=200)

    
    def post(self, request, service_type=None):
        try:
            if service_type=="register":
                return self.register(request)
            elif service_type=="login":
                return self.login(request)
        
        except Exception as e:
            return Response(data={
                "message":"Failed",
                "error":str(e),
                "status":False
            }, status=401)