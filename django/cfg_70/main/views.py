from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from main.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from tkinter.filedialog import askopenfilename
from sqlalchemy import create_engine
from django.db import models

class batch(Model):
    region = CharField(max_length=50)
    center_name = CharField(max_length=50)
    ldcm_name = CharField(max_length=50)
    reportee = CharField(max_length=50)
    batch_type = CharField(max_length=50)
    batch_code = CharField(max_length=50)
    course_name = CharField(max_length=50)
    course_name2 = CharField(max_length=50)
    region = CharField(max_length=50)
    status = CharField(max_length=50)
    date = DateField()
    class Meta:
      db_table = "For Batches"

# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request,"Username or Password Incorrect!")
                return render(request,'forms/login.html',context)

        return render(request,'forms/login.html',context)

def DragAndDrop1(request):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filelocation = askopenfilename() # open the dialog GUI
    if file_name.endswith('.csv'):
        df = pd.read_csv(input_file, skiprows = skip_rows)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(input_file, skiprows = skip_rows)
    elif file_name.endswith('.psv'):
        df = pd.read_csv(input_file, sep = "|", skiprows = skip_rows)
    else: 
        print('file format not supported')
        
    #use df to update values in the database
    engine = create_engine('sqlite:///save_pandas.db', echo=True)
    sqlite_connection = engine.connect()

    sqlite_table = df
    save_df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
    sqlite_connection.close()
    sqlite3

def SaveProfileForBatches(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         profile = batch()
         profile.region = MyProfileForm.cleaned_data["Region"]
         profile.centrename = MyProfileForm.cleaned_data["Center Name"]
         profile.ldcmname = MyProfileForm.cleaned_data["LDCM Name"]
         profile.reportee = MyProfileForm.cleaned_data["Reportee"]
         profile.batchtype = MyProfileForm.cleaned_data["Batch Type"]
         profile.coursename = MyProfileForm.cleaned_data["Course Name"]
         profile.coursename2 = MyProfileForm.cleaned_data["Course Name2"]
         profile.status = MyProfileForm.cleaned_data["Status"]
         profile.startdate = MyProfileForm.cleaned_data["Start Date"]
         
         profile.save()
         saved = True
   else:
      MyProfileForm = Profileform()
		
   return render(request, 'saved.html', locals())



def DragAndDrop1(request):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filelocation = askopenfilename() # open the dialog GUI
    if file_name.endswith('.csv'):
        df = pd.read_csv(input_file, skiprows = skip_rows)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(input_file, skiprows = skip_rows)
    elif file_name.endswith('.psv'):
        df = pd.read_csv(input_file, sep = "|", skiprows = skip_rows)
    else: 
        print('file format not supported')
        
    #use df to update values in the database
    engine = create_engine('sqlite:///save_pandas.db', echo=True)
    sqlite_connection = engine.connect()
    

def admin_forBatch(request):
    allBatches = forbatches.obejct.all()
    return render(request,"forBatch/admin.html",{'forBatches': allBatches})

def adminForPassout(request):
    allPassout = ForPassout.obejct.all()
    return render(request,"forPassout/admin.html",{'forPassout': allPassout})

def adminPlacement(request):
    allPlacement = Placement.obejct.all()
    return render(request,"Placement/admin.html",{'Placement': allPlacement})



def Register(request):
    if request.user.is_authenticated:
        return redirect('Home')
    
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,user + "  Your account has been created successfully! ")

                return redirect('Login')

        context = {'form':form}
        return render(request,'forms/register.html',context)

@login_required(login_url='Login')
def Home(request):
    user = request.user.username

    context = {'user':user}
    return render(request,'forms/home.html',context)

def Logout(request):
    logout(request)
    return redirect('Login')