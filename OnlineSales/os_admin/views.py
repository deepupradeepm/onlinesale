from django.shortcuts import render
from django.shortcuts import redirect

from os_agent.models import Property
from os_client.models import Client
from .models import AdminLogin,Agent
from django.contrib import messages
import random
from OnlineSales import sendMessage

def adminlogincheck(request):
    if request.method == "POST":
        ausername = request.POST.get("admin_username")
        apassword = request.POST.get("admin_password")

        try:
            result = AdminLogin.objects.get(contactno=ausername,password=apassword)
            otp = random.randint(100000, 999999)
            result.otp = otp
            result.save()
            message = "Hello Admin This is Your One time Password :"+str(otp)
            d1 = sendMessage.sendACASMS(ausername,message)

            import json
            dd = json.loads(d1)
            if dd["return"]:
                return render(request,"os_admin_templates/admin_otp.html")
            else:
                return render(request, "os_admin_templates/os_admin_login.html",{"error":"Sorry Unable to send OTP"})

        except:
            messages.error(request,"Invalid user")
            return render(request,"os_admin_templates/os_admin_login.html")

    else:
        return render(request, "os_admin_templates/os_admin_login.html")


def adminotpcheck(request):
    if request.method == "POST":
        otp = request.POST.get("admin_otp")
        try:
            result = AdminLogin.objects.get(otp=otp)
            request.session['status'] = True
            return render(request, "os_admin_templates/os_admin_welcome.html")
        except:
            messages.error(request, "Invalid OTP")
            return render(request, "os_admin_templates/os_admin_login.html")
    else:
        return render(request, "os_admin_templates/os_admin_login.html")


def agenthome(request):
    qs = Agent.objects.all()
    return render(request, "os_admin_templates/os_admin_agenthome.html",{"data":qs})


def adminhome(request):
    request.session['status'] = False
    return render(request,"os_admin_templates/os_admin_login.html")


def saveAgent(request):
    if request.method == "POST":
        idno = request.POST.get("a1")
        name = request.POST.get("a2")
        contact = request.POST.get("a3")
        address = request.POST.get("a4")
        photo = request.FILES["a5"]
        username = request.POST.get("a6")
        password = request.POST.get("a7")
        otp = 123456
        Agent(no=idno,name=name,contactno=contact,address=address,photo=photo,username=username,password=password,otp=otp).save()
        #return redirect('/osadmin/agenthome/')

        qs = Agent.objects.all()
        return render(request, "os_admin_templates/os_admin_agenthome.html", {"data": qs})

    else:
        return redirect('adminhome')


def deleteview(request):
    idno = request.GET.get("idno")
    Agent.objects.filter(no=idno).delete()
    qs = Agent.objects.all()
    return render(request, "os_admin_templates/os_admin_agenthome.html", {"data": qs})


def viewallClients(request):
    qs = Client.objects.all()
    return render(request,"os_admin_templates/os_client.html",{"data":qs})


def deleteclient(request):
    uname = request.GET.get("idno")
    Client.objects.filter(username=uname).delete()
    qs = Client.objects.all()
    return render(request, "os_admin_templates/os_client.html", {"data": qs})


def propertyAll(request):
    qs = Property.objects.filter(status="post")
    return render(request, "os_admin_templates/property_all.html", {"data": qs})
