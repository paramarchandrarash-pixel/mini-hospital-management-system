from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/add-slot/', views.add_slot, name='add_slot'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book-slot/<int:slot_id>/', views.book_slot, name='book_slot'),
]