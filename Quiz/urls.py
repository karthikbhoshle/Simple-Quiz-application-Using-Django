from django.urls import path
from quiz import views
urlpatterns = [
    path('',views.index,name='index'),
   path('About/',views.About,name='About'),
   path('Pythonqestion',views.Pythonqestion,name='Pythonqestion'),
   path('Javaqestion',views.Javaqestion,name='Javaqestion'),
   path('Cqestion',views.Cqestion,name='Cqestion'),
   path('quizPython/Pythonresult',views.Pythonresult,name='Pythonresult'),
   path('quizJava/Javaresult',views.Javaresult,name='Javaresult'),
   path('quizC/Cresult',views.Cresult,name='Cresult'),


    ]