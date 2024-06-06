from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
import json

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')  # Assuming frontend sends 'email' instead of 'username'
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email or password'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'success': True, 'message': 'Logout successful'})
    else:
        return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class UserRegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'success': False, 'message': 'Email and password are required'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'Email already exists'}, status=400)

            # Create a unique username by using the email
            username = email.split('@')[0]  # Use the part before the '@' as username

            # Ensure username uniqueness by appending a number if needed
            original_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{original_username}{counter}"
                counter += 1

            user = User.objects.create_user(username=username, email=email, password=password)

            return JsonResponse({'success': True, 'message': 'Registration successful'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
