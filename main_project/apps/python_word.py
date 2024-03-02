

# import os
# from django.conf import settings
# from django.contrib.auth import authenticate

# # Use an absolute path to the settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_project.settings')

# # Ensure Django is set up
# import django
# django.setup()

# # Now you can use the authenticate function
# user = authenticate(username="gokul", password="gokul@12")


# from django.contrib.auth import authenticate
# user = authenticate(user="gokul",password="gokul@12")

# if user is not None:
#     print("succssfully login the user")
# else:
#     print("please provied the user valid user name and password")


import hashlib
name="gokul"
pass1=hashlib.sha256(name.encode()).hexdigest()
print(pass1)

# 2ce6db3d86b23e69ce4e4c892ffbe5121a0fedb7ccbb6317df15e9362cada4ba