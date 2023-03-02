from django.urls import path
from todoapp import views
urlpatterns = [
    path('',views.add,name="home"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('clist/',views.TodoListview.as_view(),name="clist"),
    path('cdetail/<int:pk>/',views.Tododetail.as_view(),name="cdetail"),
    path('cupdate/<int:pk>/',views.Todoupdate.as_view(),name="cupdate"),
    path('cdelete/<int:pk>/',views.Tododelete.as_view(),name="cdelete")
]