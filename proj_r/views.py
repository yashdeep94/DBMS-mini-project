from django.shortcuts import render

def recharge(request):
    return render(request, 'proj_r/recharge.html')