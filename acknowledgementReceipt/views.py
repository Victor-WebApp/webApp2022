from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Application, registration,status
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration, ReceiverRegistration, thesisApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None and user.userType == 'ADMIN':
            login(request, user)
            return redirect('admin')
        
        elif user is not None and user.userType != 'student':
            login(request, user)
            return redirect('receiver')

        elif user is not None and user.userType == 'student' :
            login(request, user)
            return redirect ('home')

        else:
           return redirect('index')

    return  render(request, 'Login.html')

def studentRegistration(request):
    form = StudentRegistration()
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # userType = form.cleaned_data.get('student')
            form.instance.userType = 'student'
            form.save()
            return redirect ('index')
    
    context = { 'form': form
    }
    return render(request, 'Registration.html', context)

def receiver(request):
    searchNumber = 0
    officeStatus = {}
    if request.method=='POST':
        searchNumber = request.POST.get('search')
        application = registration.objects.filter(idNumber = searchNumber, userType = 'student')
        if application.count() != 0:
            applicationStatus = Application.objects.filter(studentId_id = application[0].pk)
            if applicationStatus.count() != 0:
                officeStatus = status.objects.filter(proponents_id = applicationStatus[0].pk)
                                
    totalApplicants = Application.objects.all().count()
    context = { 'form': totalApplicants,
                'officeStatus' : officeStatus}
    return render(request, 'Receive.html', context)

@login_required(login_url='index')
def admin(request):
    # if request.user.is_authenticated and request.user.userType == 'ADMIN':
        idNumber = 0
        noOfApplicants = {}
        if request.method=='POST':
            idNumber = request.POST.get('number')
        userId = registration.objects.filter(idNumber = idNumber)
        if userId.count() != 0:
            noOfApplicants = Application.objects.filter(studentId_id = userId[0].pk)
        totalApplicants = Application.objects.all().count()
        context = {'noOfApplicants': noOfApplicants,
                    'totalApplicants' : totalApplicants}
        return  render(request, 'admin.html', context)
    # return redirect ('index')

@login_required(login_url='index')
def addSignatories(request):
    if request.user.is_authenticated and request.user.userType == 'ADMIN':
        form = ReceiverRegistration()
        if request.method == "POST":
            form = ReceiverRegistration(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('index')
        
        context = { 'form': form
        }
        return render(request, 'addSignatories.html', context)
    return redirect('index')

@login_required(login_url='index')
def home(request):
    
    if request.user.is_authenticated and request.user.userType == 'student':
        context = {}

        application = Application.objects.filter(studentId_id = request.user.pk)
        if len(application) == 0:
            return  render(request, 'Home.html', context)
        applicationStatus = status.objects.filter(proponents_id = application[0].pk)
        context = {'applicationStatus': applicationStatus,
                    'application' : application}
        print(context)
        return  render(request, 'Home.html', context)
    return redirect ('index')

@login_required(login_url='index')
def application(request):

    # if request.method=='POST':
    #     title = request.POST.get('title')
    #     proponents = request.POST.get('proponents')
    #     idNumber = request.POST.get('idNumber')
    #     print (title, proponents, idNumber)
    #     newThesis = Application(thesisTitle=title, proponents=proponents,
    #                 studentId_id=idNumber)
    #     newThesis.save()
    #     # newThesis = Application.objects.create(thesisTitle=title, proponents=proponents,
    #     #     studentId_id=idNumber)
    #     proponentId =  Application.objects.get(studentId_id = idNumber)
    #     applicationStatus = status.objects.create(proponents_id = proponentId.pk, dit = False, oaa = False,
    #                 ocl = False, ore = False,  adviser = False, fic = False)
    #     return  redirect('home')
    # return render(request, 'Application.html')

    form = thesisApplication()
    if request.method == "POST":
        form = thesisApplication(request.POST)
        if form.is_valid():
            idNumber = request.POST.get('number')
            form.instance.studentId_id = idNumber
            form.save()

            proponentId =  Application.objects.get(studentId_id = idNumber)
            applicationStatus = status.objects.create(proponents_id = proponentId.pk, dit = False, oaa = False,
                    ocl = False, ore = False,  adviser = False, fic = False)
            return redirect ('home')        
    context = {'form':form}
    return render(request, 'Application.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')


def update(request, id):
    if request.method == "POST":
        updateApplication = request.POST.get('status')
        saveData = status.objects.get(id = id)
        saveData.dit = updateApplication
        saveData.save()
        return redirect ('receiver')     

    updateStatus = status.objects.get(id = id)
    context = {'status' : updateStatus}
    return render(request, 'update.html', context)

@login_required(login_url='index')
def editProfile(request,id):
    data = registration.objects.get(id=id)
    print(data.first_name)
    information = StudentRegistration(instance=data)
    # form = StudentRegistration()
    if request.method == "POST":
        form = StudentRegistration(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect ('index')
    
    context = { 'form': information
    }
    return render(request, 'EditProfile.html', context)
