from django.shortcuts import render
from django.shortcuts import render,redirect
from quiz.models import Python,Java,C
def index(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'About.html')
def Pythonqestion(request):
    q1=Python.objects.get(pk=1)
    q2=Python.objects.get(pk=2)
    q3=Python.objects.get(pk=3)
    q4=Python.objects.get(pk=4)
    q5=Python.objects.get(pk=5)

    return render(request, 'Python.html',{'Q1':q1,'Q2':q2,'Q3':q3,'Q4':q4,'Q5':q5})
def Javaqestion(request):
    q1=Java.objects.get(pk=1)
    q2=Java.objects.get(pk=2)
    q3=Java.objects.get(pk=3)
    q4=Java.objects.get(pk=4)
    q5=Java.objects.get(pk=5)

    return render(request, 'Java.html',{'Q1':q1,'Q2':q2,'Q3':q3,'Q4':q4,'Q5':q5})
def Cqestion(request):
    q1=C.objects.get(pk=1)
    q2=C.objects.get(pk=2)
    q3=C.objects.get(pk=3)
    q4=C.objects.get(pk=4)
    q5=C.objects.get(pk=5)

    return render(request, 'C.html',{'Q1':q1,'Q2':q2,'Q3':q3,'Q4':q4,'Q5':q5})
def Pythonresult(request):
    st=0
    for i in range(1,6):
        a=Python.objects.get(pk=i)
        if request.POST[str(i)] == a.An:
            st+=1


    return render(request, 'pythonre.html',{'mt':st})
def Cresult(request):
    st=0
    for i in range(1,6):
        a=C.objects.get(pk=i)
        if request.POST[str(i)] == a.An:
            st+=1


    return render(request, 'Cre.html',{'mt':st})
def Javaresult(request):
    st=0
    for i in range(1,6):
        a=Java.objects.get(pk=i)
        if request.POST[str(i)] == a.An:
            st+=1


    return render(request, 'Javare.html',{'mt':st})

# Create your views here.
