from . import views
from django.urls import  path

app_name = 'food'

urlpatterns = [
    path('',views.IndexClassView.as_view() ,name='index'),   #  <---   http://localhost:8000/food/
    path('<int:pk>/', views.fooddetail.as_view(), name='detail'),                                     # -->  http://localhost:8000/food/1/
    
    # add item
    path('add/' , views.CreateItem.as_view(),name='create_item'),
    
    # update item
    path('update/<int:item_id>' , views.update_item,name='update_item'),
    
    #delete item
    path('delete/<int:item_id>/' , views.delete_item,name='delete_item'),
]