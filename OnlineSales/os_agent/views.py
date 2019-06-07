import random

from django.shortcuts import render,redirect
from django.views.generic import DeleteView


from os_admin.models import Agent
from .models import Property, BlockProperty,SoldProperty
from django.contrib import messages

def agentlogincheck(request):
    if request.method == "POST":
        ausername = request.POST.get("agent_username")
        apassword = request.POST.get("agent_password")

        try:
            result = Agent.objects.get(username=ausername,password=apassword)
            otp = random.randint(100000, 999999)
            result.otp = otp
            result.save()
            message = "Hello Agent This is Your One time Password :"+str(otp)
            #d1 = sendMessage.sendACASMS(ausername,message)

           # import json
            #dd = json.loads(d1)

            #if dd["return"]:
            if True:
                request.session['username'] = ausername
                return render(request,"os_agent_templates/os_agent_otp.html")
            else:
                return render(request, "os_admin_templates/os_admin_login.html",{"error":"Sorry Unable to send OTP"})

        except:
            messages.error(request,"Invalid user")
            return render(request,"os_agent_templates/os_agent_home.html")

    else:
        return render(request, "os_agent_templates/os_agent_home.html")


def agentotpcheck(request):
    if request.method == "POST":
        otp = request.POST.get("agent_otp")
        try:
            result = Agent.objects.get(otp=otp)
            request.session['status'] = True
            return render(request, "os_agent_templates/os_agent_welcome.html")
        except:
            messages.error(request, "Invalid OTP")
            return render(request, "os_agent_templates/os_agent_home.html")
    else:
        return render(request, "os_agent_templates/os_agent_home.html")


def agenthome(request):
    request.session['status'] = False
    return render(request, "os_agent_templates/os_agent_home.html")


def openproperty(request):
    agent = request.session['username']
    qs = Property.objects.filter(agent_id=agent,status="post")
    return render(request,"os_agent_templates/os_agent_property.html",{"data":qs})


def saveProperty(request):
    if request.method == "POST":
        name = request.POST.get("p2")
        location = request.POST.get("p3")
        size = request.POST.get("p4")
        price = request.POST.get("p5")
        facing = request.POST.get("p6")
        comment = request.POST.get("p7")
        photo = request.FILES["p8"]
        status = "post"
        agent = request.session['username']
        Property(name=name,location=location,size=size,price=price,facing=facing,photo=photo,status=status,comment=comment,agent_id=agent).save()
        #return redirect('/osagent/property/')
        #return redirect('property')
        qs = Property.objects.filter(agent_id=agent)
        return render(request, "os_agent_templates/os_agent_property.html", {"data": qs})


class AgentDeleteConformation(DeleteView):
    model = Property
    template_name = "os_agent_templates/os_agent_delete_conformation.html"
    success_url = '/osagent/property/'


def blockProperty(request):
    uname = request.session['username']
    qs = Property.objects.filter(agent_id=uname,status="post")
    list = []
    for x in qs:
        list.append(BlockProperty.objects.filter(property_no_id=x.no))

    return render(request,"os_agent_templates/os_agent_bocked.html",{"data":list})


def soldProperty(request):
    pno = request.GET.get("no")
    cun = request.GET.get("cun")
    SoldProperty(property_no_id=pno,client_un_id=cun).save()
    Property.objects.filter(no=pno).update(status="sold")
    return render(request,"os_agent_templates/os_agent_welcome.html")


def viewsold(request):
    agent = request.session['username']
    qs = Property.objects.filter(agent_id=agent, status="sold")
    return render(request, "os_agent_templates/os_agent_sold_property.html", {"data": qs})


# API VIEWS

from rest_framework.views import APIView
from .sample import MyPropertySerializer
from rest_framework.response import Response


class MyProduct(APIView):
    def get(self,request):
        pro = Property.objects.all()
        ms = MyPropertySerializer(pro,many=True)
        return Response(ms.data)





