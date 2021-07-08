from LMS.local_settings import AUTH
from datetime import datetime
import jwt

def token_decoder(token):
    try:
        payload = jwt.decode(token, algorithms =["HS256"], key=AUTH.FRONTEND_SECRET_KEY)
        print(payload)
        return payload

    except Exception as e:
        raise e

def payload(data):
    try:
        present_time=datetime.utcnow()
        data["typ"]="access"
        data["exp"] = (present_time+AUTH.ACCESS_TOKEN_EXPIRY).timestamp()
        access_token = jwt.encode(payload = data, algorithm ="HS256", key = AUTH.BACKEND_SECRET_KEY)
        data["typ"] = "refresh"
        data["exp"] = (present_time+AUTH.REFRESH_TOKEN_EXPIRY).timestamp()
        data["iat"] = present_time.timestamp()
        refresh_token = jwt.encode(payload = data, algorithms =["HS256"], key = AUTH.BACKEND_SECRET_KEY)
        return access_token, refresh_token
    
    except Exception as e:
        raise e

def generate_access_from_refresh_token(token):
    try:
        present_time=datetime.utcnow()
        data=jwt.decode(token, algorithm ="HS256", key = AUTH.BACKEND_SECRET_KEY)
        assert data["typ"] == "refresh", "Invalid Token"
        assert present_time.timestamp() < data["exp"], "Token Expired"
        data["exp"]=(present_time+AUTH.ACCESS_TOKEN_EXPIRY).timestamp()
        data["typ"]="access"
        return jwt.encode(payload = data, algorithm ="HS256", key = AUTH.BACKEND_SECRET_KEY) 
    
    except Exception as e:
        raise e

def verify_access_token(token):
    try:
        present_time=datetime.utcnow()
        data = jwt.decode(token, algorithms =["HS256"], key = AUTH.BACKEND_SECRET_KEY)
        assert data["typ"] == "access", "Invalid Token"
        assert present_time.timestamp() < data["exp"], "Token Expired"
        return data["jis_id"]
    
    except Exception as e:
        raise e

def is_authenticated(func):
    def inner(self, request, *args, **kwargs):
        request["user_id"] = verify_access_token(request.headers['authorization'].split(" ")[1])
        if not request["user_id"]:
            raise "Invalid Token"
        func(self, request, *args, **kwargs)
    return inner