from django.shortcuts import render, HttpResponse,redirect
from .models import UserDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    if request.method == "POST":
        # Retrieve form data
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        # Create a new UserProfile object and save it to the database
        new_user = UserDetails(full_name=full_name, email=email, phone=phone, description=description)
        new_user.save()

        return HttpResponse("Form submitted successfully!")
    
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')  # Redirect to the user details page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_list(request):
    # Fetch all user details from the database
    users = UserDetails.objects.all()
    return render(request, 'user_list.html', {'users': users})
