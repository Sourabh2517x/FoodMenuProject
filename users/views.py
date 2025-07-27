from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your Account Have been Successfuly Registered')
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request,'users/register.html', {'form': form})

class LogoutGetView(LogoutView):
    http_method_names = ['get', 'post', 'head', 'options']

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.get_user().username
        messages.success(self.request, f'Welcome {username}, Your Account Have been Successfully Logged In')
        return super().form_valid(form)
    
    
@login_required   
def ProfileView(request):
    return render(request,'users/profile.html')




