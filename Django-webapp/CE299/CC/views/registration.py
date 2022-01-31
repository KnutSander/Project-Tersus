from django.shortcuts import render


def reset(request):
    return render(request,"registration/password_reset.html")

def create_acc(request):
    return render(request,"registration/create_account.html")