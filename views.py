from django.contrib .auth import authenticate,logout,login
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def About(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Index(request):
        if not request.user.is_staff:
            return redirect('login')
        return render(request, 'index.html')

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'login.html')

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp= request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=c, special=sp)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_doctor.html')

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Patient.objects.all()
    d={'pat':pat}
    return render(request,'view_patient.html',d)

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a= request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m , address=a)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_patient.html')

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint=Appointment.objects.all()
    d={'appoint':appoint}
    return render(request,'view_appointment.html',d)

def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=d, patient=p, date1=d1 , time1=t)
            error='no'
        except:
            error='yes'
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html')

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')


