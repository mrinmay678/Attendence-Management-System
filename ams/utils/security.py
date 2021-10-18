from jwt import encode, decode
from .secrets import FRONTEND_KEY, BACKEND_KEY
from datetime import datetime, timedelta
from authentication.models import Candidate
from rest_framework.authentication import get_authorization_header

def payloadGenerator(username):
    
    access_key_payload=dict(
        username=username,
        exp=datetime.utcnow()+timedelta(days=1),
        iat= datetime.utcnow()
    )
    refresh_key_payload=dict(
        username=username,
        exp=datetime.utcnow()+timedelta(days=2),
        iat= datetime.utcnow()
    )
    token = dict(
        access_key=encode(access_key_payload,BACKEND_KEY,algorithm="HS256"),
        refresh_key=encode(refresh_key_payload,BACKEND_KEY,algorithm="HS256")
    )

    return token


def verify_access_key(key):
    payload=decode(key, BACKEND_KEY, algorithms=["HS256"])

    try:
        if Candidate.objects.get(username=payload['username']):
            flag=True
    except Exception as e:
        flag=False
    if(payload.get('exp')<datetime.utcnow().timestamp() and flag):
        return False, None
    return True, payload["username"]

def authenticate(endpoint):
    def inner(self, request, *args, **kwargs):
        key = get_authorization_header(request).split()[1]
        state, username = verify_access_key(key)
        if not state:
            raise ValueError("Invalid Token")
        request.username=username
        return endpoint(self, request, *args, **kwargs)
    return inner            