#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from getpass import getpass

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1]=="createadmin":
        try:
            name=input("Enter Name: ")
            email=input("Enter Email: ")
            if "@" not in email or ".com" not in email:
                raise ValueError("Invalid Email")
            password=getpass("Enter Password: ")
            if len(password)<8:
                raise ValueError("Password too short")
            confirm_password=getpass("Confirm Your Password: ")
            if confirm_password==password:
                # user = AdminUser(name=name,email=email,password=password)
                # user.save()
                print("Success!")
            else:
                raise ValueError("Password and Confirm Password not Matched!")
        except Exception as e:
            print(str(e))
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
