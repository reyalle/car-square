from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data["username"], password=data["password"])
    if user:
        login(request,user)
        return JsonResponse({"message": "Login Successful"}, status=200)
    return JsonResponse({"message": "Invalid Credentials"}, status=400)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged Out Successfully"})
