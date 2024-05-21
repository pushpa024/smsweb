from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth import logout

# Create your views here.

def say_hello(request):
    # return HttpResponse("Say HEllo")
    # return render(request, 'homepage.html')
    return render(request, 'homepage.html',{'name':'john'})

@login_required
def home(request):
    # return HttpResponse("Say HEllo")
    # return render(request, 'homepage.html')
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def smsapi(request):
    return render(request, 'sms_api.html')

def twoway(request):
    return render(request, 'two_way_sms.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("invalid register details")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})

class SignedOutView(TemplateView):

    template_name = "registration/signed_out.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
