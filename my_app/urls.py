"""django_intermediario_rev2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('teste/', views.ProtectedView.as_view()),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.LoginView.as_view(
    #     template_name='my_app/home.html',
    #     nome='luiz carlos'
    # )),
    #path('login/', views.login),
    path('logout/', views.LogoutRedirectView.as_view()),
    #path('logout/', views.logout),
    path('home/', views.HomeView.as_view()),
    #path('home/', views.home),
    path('addresses/', views.AddressListView.as_view(), name='address_list'),
    #path('addresses/', views.address_list, name='address_list'),
    path('addresses/<int:pk>/detail', views.AddressDetailView.as_view(), name='address_detail'),
    path('addresses/create/', views.AddressCreateView.as_view(), name='address_create'),
    #path('addresses/create/', views.address_create, name='address_create'),
    path('addresses/<int:pk>/update/', views.AddressUpdateView.as_view(), name='address_update'),
    #path('addresses/<int:id>/update/', views.address_update, name='address_update'),
    path('addresses/<int:pk>/destroy/', views.AddressDeleteView.as_view(), name='address_destroy'),
    #path('addresses/<int:id>/destroy/', views.address_destroy, name='address_destroy'),
]

#id or pk
#Address.objects.get(id=1)