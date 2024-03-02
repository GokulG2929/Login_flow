from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Register as register
from .forms import RegisterForm
import hashlib 


@csrf_exempt
def Register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = RegisterForm(data)
        breakpoint()
        if form.is_valid():
            cleaned_data = form.cleaned_data
            data1 = form.save(commit=False)          
            password = cleaned_data.get("password") 
            pass1=hashlib.sha256(password.encode()).hexdigest()
            data1.password=pass1[:30]
            breakpoint()
            data1.save()
            return JsonResponse({"status":"success","code":200,'message': 'Data created successfully', 'id': data1.id})
        else:
            return form.errors
    return JsonResponse({"status":"failed","code":400,"message":"Method is not allowed"})


def login(request):
    if request.method == 'GET':
        data = json.loads(request.body.decode('utf-8'))
        mobile_number= data.get("mobile_number")
        password = data.get("password")
        user= register.objects.filter(mobile_number=mobile_number).last()
        breakpoint()
        if not user :
            return JsonResponse({"status":"failed","code":400,"message":"Kindly register the User"})

        try:
            if user and password:
                pass1=hashlib.sha256(password.encode()).hexdigest()
                breakpoint()
                if user.password==pass1[:30]:
                    return JsonResponse({"status":200,"message": "Successfully login"})
                else:
                    return JsonResponse({"message": "password is required "})
            else:
                return JsonResponse({"status":400,"message": "user and password is missmatch"})
        except Exception as e:
                return JsonResponse({"message": str(e)})
    else:
        return JsonResponse({"message": "Invalid request method"})



def logout(request):
    if request.method == 'GET':
        data=json.loads(request.body.decode('utf-8'))
        mobile_number=data.get('mobile_number')
        user = register.objects.get(mobile_number=mobile_number).last()
        if not user :
            return JsonResponse({"status":"failed","code":400,"message":"Kindly register the User"})
        try:
            form_data = {
                'name': user.name,
                'user_id': user.user_id,
                'location': user.location,
                'password': user.password,  # Assuming 'password' is a field in your model
                'mobile_number': user.mobile_number  # Assuming 'mobile_number' is a field in your model
            }
            form = RegisterForm(data=form_data, instance=user)

            if form.is_valid:
                user=form.save(commit=False)
                user.user_id=None
                user.save()
                return JsonResponse({"message":"logout successfully done"})
            else:
                return JsonResponse({"message": "Form is not valid"})
        except Exception as e:
            return JsonResponse({"message": str(e)})
        
    else:
        return JsonResponse({"message": "Invalid request method"})

   
