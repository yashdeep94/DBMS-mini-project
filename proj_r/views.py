from django.shortcuts import render
from datetime import date, timedelta
import json

def recharge(request):
    if request.method == "POST":
        user_channels = []
        for val in request.POST:
            if val == "csrfmiddlewaretoken" or val == "Inputname" or val == "InputId":
                continue
            else:
                user_channels.append(request.POST.get(val))
        name = request.POST.get("Inputname")
        sub_id = request.POST.get("InputId")
        from_date = date.today()
        to_date = date.today() + timedelta(30)
        print(name, sub_id, from_date , to_date, json.dumps(user_channels))
        # print(user_channels)
        return render(request, 'proj_r/recharge.html')
    else:
        return render(request, 'proj_r/recharge.html')