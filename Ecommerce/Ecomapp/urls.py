from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('accounts/sign_up/',views.sign_up,name="signup"),
    path('accounts/login/',views.login_view,name="login"),  
    path('home/', views.home, name='home'),
    path('logout',views.logout_view),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('display',views.display),
    path('delete',views.delete),
    path('update',views.updateprice),
    path('placeorder/', views.placeorder, name='placeorder'),
]