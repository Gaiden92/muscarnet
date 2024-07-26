from django.shortcuts import render, redirect

from .models import User
from .form import CustomUserCreation


# Create your views here
def user_index(request):
    users = User.objects.all()

    return render(request, "users-index.html", {"users": users})

def inscription(request):
    if request.method == "POST":
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user-index")
    else:
        form = CustomUserCreation()


    return render(request, "inscription.html", {"form": form})
