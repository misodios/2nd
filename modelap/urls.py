from django.urls import path

from modelap import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:course_id>',views.content,name='content'),

]
