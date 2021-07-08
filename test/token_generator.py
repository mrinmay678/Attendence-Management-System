from datetime import datetime, timedelta
import jwt

class AUTH:
    FRONTEND_SECRET_KEY ="hfijvb&kjvf&(4v5dvfdf#dbf/dbfd())5bf4d6njd6b4f6*b165'fdf1v5+6f"
    BACKEND_SECRET_KEY = "mklmjvb&kjvf&(4v5jbhjbhj&*&TF%&*Tdbf/dbfd())5bf%^%(HHJK6*b165'fdflkfvmlfd+__)_++"
    ACCESS_TOKEN_EXPIRY=timedelta(days=1)
    REFRESH_TOKEN_EXPIRY=timedelta(days=3)

def payload(data):
    try:
        present_time=datetime.utcnow()
        data["typ"]="access"
        data["exp"] = (present_time+AUTH.ACCESS_TOKEN_EXPIRY).timestamp()
        access_token = jwt.encode(payload = data, algorithm ="HS256", key = AUTH.BACKEND_SECRET_KEY)
        data["typ"] = "refresh"
        data["exp"] = (present_time+AUTH.REFRESH_TOKEN_EXPIRY).timestamp()
        data["iat"] = present_time.timestamp()
        refresh_token = jwt.encode(payload = data, algorithm ="HS256", key = AUTH.BACKEND_SECRET_KEY)
        print(f"Access Token - {access_token}\nRefresh Token - {refresh_token}")
    
    except Exception as e:
        print(str(e))

def frontend_token(data):
    try:
        present_time=datetime.utcnow()
        token = jwt.encode(payload = data, algorithm ="HS256", key = AUTH.FRONTEND_SECRET_KEY)
        print(f"Token - {token}")
    
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    data={
        "jis_id":input("Enter ID: "),
        "password":input("Enter Password: ")
    }
    print("Enter 1 for frontend_token\nEnter 2 for access_key")
    if(input()=="1"):
        frontend_token(data)
    else:
        payload(data)