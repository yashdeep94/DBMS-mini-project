from django.shortcuts import render
from datetime import date, timedelta
import json
import mysql.connector

def recharge(request):
    if request.method == "POST":
        mydb = mysql.connector.connect(host="localhost",user="root",password="yash@1412",database="tv_network")
        mycursor = mydb.cursor()
        user_channels = []
        for val in request.POST:
            if val == "csrfmiddlewaretoken" or val == "Inputname" or val == "InputId" or val == "total":
                continue
            else:
                user_channels.append(request.POST.get(val))
        name = request.POST.get("Inputname")
        sub_id = request.POST.get("InputId")
        from_date = date.today()
        to_date = date.today() + timedelta(30)
        total = request.POST.get("total")
        mycursor.execute(f"insert into customer values({int(sub_id)},'{name}');")
        mydb.commit()

        mycursor.execute(f"insert into recharge values('{from_date}','{to_date}','{json.dumps(user_channels)}',{int(total)},{int(sub_id)});")
        mydb.commit()
        return render(request, 'proj_r/recharge.html')
    else:
        return render(request, 'proj_r/recharge.html')