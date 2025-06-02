from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def userLogin(request):
    if request.method == "POST":
        alert_message = request.session.pop("alert_message", None)
        alert_type = request.session.pop("alert_type", None)
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page
            else:
                return render(request, 'accessControl/login.html', {'form': fm, 'error': 'Invalid credentials', "alert_message": alert_message,
        "alert_type": alert_type})
    else:
        fm = AuthenticationForm()
    return render(request, 'accessControl/login.html', {'form': fm})

def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('login')
