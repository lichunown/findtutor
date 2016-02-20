#encoding:utf-8
from django.shortcuts import render
from models import Student,Tutor,Project,Invitation
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from forms import SigninForm,SignupForm,ModifyAccountForm,CreateProjectForm,ShowStudentForm,ShowTutorForm
from django.utils import timezone
# Create your views here.
def index(request):
    projects=Project.objects.order_by('startdate').reverse()[:10]    
    tutors=Tutor.objects.order_by('?').reverse()[:10] 
    context={
        'projects':projects,
        'tutors':tutors,
    }
    return render(request,'main/index.html',context)

def signin(request,before='index'):
    if request.method=='POST':
        sf = SigninForm(request.POST)
        if sf.is_valid():
            username = sf.cleaned_data['username']
            password = sf.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return render(request,'main/signin.html',{'result':'succeed','before':before})
        #form doesn't true
            else:
                return render(request, 'main/signin.html', {'result':'error','form':sf})        
        else:
            return render(request,'main/signin.html',{'result':'error'})
            # Return an error message.
    else:
        print 'signin2'
        sf = SigninForm()
        return render(request,'main/signin.html',{'form':sf,'before':before})

def signout(request,before='index'):
    logout(request)
    return render(request,'main/signin.html',{'result':'signout','before':before})
def signup2(request):
    if request.method=='POST':
        suf = SigninForm(request.POST)
        print request.POST               
        username = request.POST['username']
        password = request.POST['password'] 
        if not len(User.objects.filter(username=username)):
            if request.POST['password']==request.POST['passwordagain']:
                user=User()
                user.username=username
                user.set_password(password)
                user.save()
                student=Student()
                student.username=user
                student.sid=request.POST['sid']
                student.truename=request.POST['truename']
                student.birthday=timezone.now()
                student.save()
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return render(request,'main/signin.html',{'result':'succeed'}) 
                else:
                    pass #something wrong
            else:
                 return render(request,'main/signup2.html',{'form':suf,'error':'passwordagain'})    
        else:
            return render(request,'main/signup2.html',{'form':suf,'error':'usernamerepeat'})                 
    else:
        suf=SignupForm()
        return render(request,'main/signup2.html',{'form':suf})

def signup(request):
    if request.method=='POST':
        suf=SignupForm()
        if suf.is_valid():
            pass
        else:
            return render(request,'main/signup.html',{'error':'1','form':suf})
    else:
        suf=SignupForm()
        return render(request,'main/signup.html',{'form':suf})

def modifyaccount(request):
    if request.user.is_authenticated():
        if request.method=='POST':
            f=ModifyAccountForm(request.POST,instance=Student.objects.get(username=request.user))           
            if f.is_valid():
                f.save()
                return render(request,'main/modifyaccount.html',{'success':'1','form':f})
            else:
                return render(request,'main/modifyaccount.html',{'error':'1','form':f})
        else:
            student=Student.objects.get(username=request.user)
            projects=student.project_set.all()
            f=ModifyAccountForm(instance=Student.objects.get(username=request.user))
            return render(request,'main/modifyaccount.html',{'projects':projects,'form':f})
    else:
        return render(request,'main/signup2.html',{'form':suf})
def showtutors(request,page):
    pass
def showtutor(request,id):
    try:
        student=Tutor.objects.get(id=id)  
    except:
        return render(request,'main/tutor.html',{'error':'none'})
    f=ShowTutorForm(instance=student)
    return render(request,'main/tutor.html',{'form':f})

def showprojects(request,page):
    page=int(page)
    projects=Project.objects.order_by('startdate').reverse()[1*page-1:30*page-1]
    return render(request,'main/projects.html',{'page':page,'projects':projects})
def showproject(request,id):
    p=Project.objects.get(id=id)
    students=p.students.all()
    tutors=p.tutors.all()
    allstudents=p.students.all()
    for s in allstudents:#应该可以优化一下
        if request.user==s.username:
            return render(request,'main/project.html',{'project':p,'students':students,'tutors':tutors,'edit':'1'})
    return render(request,'main/project.html',{'project':p,'students':students,'tutors':tutors})

def createproject(request):
    if request.user.is_authenticated():        
        if request.method=='POST':
            f=CreateProjectForm(request.POST)
            if f.is_valid():
                stu=Student.objects.get(username=request.user)  
                project=Project()
                project.name=f.cleaned_data['name']                
                allprojects=stu.project_set.all()  
                for p in allprojects:
                    if p.name==project.name:
                        return render(request,'main/createproject.html',{'error':'repeat','form':f})
                project.status=f.cleaned_data['status']
                project.introduction=f.cleaned_data['introduction']
                project.startdate=timezone.now()                     
                project.save()  
                project.students.add(stu)    
                project.save()  
                return showproject(request,project.id)      #why this doesn't work!!!!

            else:
                return render(request,'main/createproject.html',{'error':'1','form':f})
        else:
            f=CreateProjectForm()
            return render(request,'main/createproject.html',{'form':f})
    else:
        return signin(request)


def showstudent(request,id):
    try:
        student=Student.objects.get(id=id)  
    except:
        return render(request,'main/student.html',{'error':'none'})
    f=ShowStudentForm(instance=student)
    return render(request,'main/student.html',{'form':f})


def invitetutor(request):
    pass
def invitestudent(request):
    pass