from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Preference , Account , NotificationSettings , ThemeSettings , PrivacySettings
from .serializers import PreferenceSerializer , AccountSerializer , NotificationSettingsSerializer , ThemeSettingsSerializer , PrivacySettingsSerializer

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({"message": "Login successful", "user": user.username})
    return JsonResponse({"error": "Invalid credentials"}, status=400)

@api_view(["POST"])
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})

@api_view(["POST"]) 
@permission_classes([IsAuthenticated])
def user_status(request):
    # print all teh cookies 
    print(request.COOKIES)
    return JsonResponse({"authenticated": True, "user": request.user.username})


@api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
def user_preferences(request):
    # pref, created = Preference.objects.get_or_create(user=request.user)
    print(request.user)
    pref, created = Preference.objects.get_or_create(user=1)
    if request.method == 'GET':
        serializer = PreferenceSerializer(pref)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PreferenceSerializer(pref, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def account_settings(request):
    user = request.user
    # user = 1
    account, _ = Account.objects.get_or_create(user=user)

    if request.method == 'GET':
        return Response(AccountSerializer(account).data)

    if request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def notification_settings(request):
    user = request.user
    # user = 1
    notifications, _ = NotificationSettings.objects.get_or_create(user=user)

    if request.method == 'GET':
        return Response(NotificationSettingsSerializer(notifications).data)

    if request.method == 'PUT':
        serializer = NotificationSettingsSerializer(notifications, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def theme_settings(request):
    user = request.user
    # user = 1
    theme, _ = ThemeSettings.objects.get_or_create(user=user)

    if request.method == 'GET':
        return Response(ThemeSettingsSerializer(theme).data)

    if request.method == 'PUT':
        serializer = ThemeSettingsSerializer(theme, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def privacy_settings(request):
    user = request.user
    # user = 1
    privacy, _ = PrivacySettings.objects.get_or_create(user=user)

    if request.method == 'GET':
        return Response(PrivacySettingsSerializer(privacy).data)

    if request.method == 'PUT':
        serializer = PrivacySettingsSerializer(privacy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



