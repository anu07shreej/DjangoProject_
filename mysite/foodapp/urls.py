from . import views
from django.urls import path




urlpatterns = [
    path('hello/', views.index, name='index'),
    path('item/', views.item, name='item')
    
    #path('admin/', admin.site.urls),

]