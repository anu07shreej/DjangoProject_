from . import views
from django.urls import path



app_name = 'foodapp'
urlpatterns = [
    #/food/
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),

    #/food/1
    path('<int:item_id>/', views.detail, name='detail')
    
    

]