from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import User, Appointment
import time
import re
import datetime
from django.core.exceptions import ObjectDoesNotExist
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render (request, 'firstapp/index.html')

def register(request):
    isValid = True
    if(len(request.POST['name']) < 2):
        messages.add_message(request, messages.ERROR, "Name must be at least 2 characters!")
        isValid = False
    if(request.POST['name'].isalpha() == False): 
        messages.add_message(request, messages.ERROR, "Name must contain letters only!")
        isValid = False
    if(not EMAIL_REGEX.match(request.POST['email'])):
        messages.add_message(request, messages.ERROR, "Please enter a valid email address")
        isValid = False   
    if(len(request.POST['password']) < 8):
        messages.add_message(request, messages.ERROR, "Password must be at least 8 characters!")
        isValid = False
    if(len(request.POST['password']) > 14):
        messages.add_message(request, messages.ERROR, "Password cannot be longer than 14 characters!")
        isValid = False    
    if(request.POST['password'] != request.POST['password_conf']):
        messages.add_message(request, messages.ERROR, "Passwords must match!") 
        isValid= False  
    if(len(request.POST['dob']) < 1):
        messages.add_message(request, messages.ERROR, "Please enter a your date of birth!")     
        isValid = False
    if not isValid:
        return redirect ('/')    

    User.objects.create(name = request.POST['name'], email = request.POST['email'], password = request.POST['password'], dob=request.POST['dob'])
    request.session['current_user'] = User.objects.get(email= request.POST['email']).id
    return redirect ("/success")

def login(request):
    try:
        users = User.objects.get(email=request.POST['email'], password=request.POST['password'])
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, "Invalid username or password!")
        return redirect('/')    
    else:
        context = {}
        request.session['current_user'] = User.objects.get(email=request.POST['email'], password=request.POST['password']).id
        if "current_user" in request.session.keys():
            return redirect('/success')         

def success(request):
    if "current_user" in request.session.keys():
        context = {
            "user" : User.objects.get(pk=request.session['current_user']),
            "today" : datetime.datetime.now().date(),
            "appointments_today" : Appointment.objects.filter(user_id=User.objects.get(pk=request.session['current_user'])).filter(date=datetime.datetime.now().date()).order_by('time'),
            "appointments_future" : Appointment.objects.filter(user_id=User.objects.get(pk=request.session['current_user'])).exclude(date=datetime.datetime.now().date()).order_by('date').order_by('time'),
            "appointments" : Appointment.objects.all()
        }

    return render(request, 'firstapp/success.html', context)

def logout(request):
    request.session.clear()
    messages.add_message(request, messages.INFO, "Successfully logged out")
    return redirect('/')

def addAppointment(request):
    isValid = True 
 
   
    if len(request.POST['date']) < 6:
        messages.add_message(request, messages.ERROR, "Please enter a valid date!")
        isValid = False
    elif datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date() < datetime.datetime.now().date():
        messages.add_message(request, messages.ERROR, "Date must be current or future date!") 
        isValid = False        
    if len(request.POST['time']) < 4:
        messages.add_message(request, messages.ERROR, "Please enter a valid time!")
        isValid = False  
    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.ERROR, "Tasks cannot be blank!")
        isValid = False


  
    if not isValid:
        return redirect('/success')

    try:
        Appointment.objects.get(time=request.POST['time'], date=request.POST['date'])
    except ObjectDoesNotExist:
        newAppt = True
    else:
        messages.add_message(request, messages.ERROR, "You already have an appointment at this time!")
        return redirect('/success')   

    Appointment.objects.create(user_id=(User.objects.get(pk=request.session['current_user'])), name=request.POST['name'], status="Pending", date=request.POST['date'], time=request.POST['time'])  

    return redirect('/success')

def delete(request, id):
    Appointment.objects.get(id=id).delete()

    return redirect('/success') 

def edit(request, id):
    context = {
        "appointment" : Appointment.objects.get(id=id),
        "date" : str(Appointment.objects.get(id=id).date),
        "time" : str(Appointment.objects.get(id=id).time)
    } 
    return render(request, 'firstapp/edit.html', context)          
            
def updateAppointment(request, id):
    isValid = True
    if len(request.POST['date']) < 6:
        messages.add_message(request, messages.ERROR, "Please enter a valid date!")
        isValid = False
    elif datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date() < datetime.datetime.now().date():
        messages.add_message(request, messages.ERROR, "Date must be current or future date!") 
        isValid = False        
    if len(request.POST['time']) < 4:
        messages.add_message(request, messages.ERROR, "Please enter a valid time!")
        isValid = False    
    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.ERROR, "Tasks cannot be blank!")
        isValid = False
    if not isValid:
        return redirect('/edit/'+ str(Appointment.objects.get(id=id).id))
    try:
        Appointment.objects.exclude(id=id).get(time=request.POST['time'], date=request.POST['date'])
    except ObjectDoesNotExist:
        newAppt = True
    else:
        messages.add_message(request, messages.ERROR, "You already have an appointment at this time!")
        return redirect('/edit/'+ str(Appointment.objects.get(id=id).id))       
           
           
    appointment = Appointment.objects.get(id=id)
    appointment.name = request.POST['name']   
    appointment.status = request.POST['status']
    appointment.date = request.POST['date']
    appointment.time = request.POST['time']
    appointment.save()
    return redirect('/success')  
                      