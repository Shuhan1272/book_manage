from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('update/<int:std_id>/',views.update,name='update'),
    path('delete/<int:std_id>/',views.delete,name='delete'),
    path('search/',views.search_by_name,name='search_by_name'),
]