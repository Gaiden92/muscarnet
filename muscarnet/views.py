from django.shortcuts import render
from authentication.models import User


def dashboard_view(request, user_id):
    user = request.user
    return render(request, "dashboard.html", {"user": user})