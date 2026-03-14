from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Slot, Booking


def home(request):
    return render(request, 'core/home.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        if User.objects.filter(username=username).exists():
            return render(request, 'core/signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        return redirect('login')

    return render(request, 'core/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user=user)

            if profile.role == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})

    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def doctor_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'doctor':
        return redirect('home')

    slots = Slot.objects.filter(doctor=request.user).order_by('date', 'time')
    bookings = Booking.objects.filter(doctor=request.user).order_by('-booked_at')

    return render(request, 'core/doctor_dashboard.html', {
        'slots': slots,
        'bookings': bookings
    })


@login_required
def add_slot(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'doctor':
        return redirect('home')

    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']

        Slot.objects.create(
            doctor=request.user,
            date=date,
            time=time
        )
        return redirect('doctor_dashboard')

    return render(request, 'core/add_slot.html')


@login_required
def patient_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'patient':
        return redirect('home')

    slots = Slot.objects.filter(is_booked=False).order_by('date', 'time')
    bookings = Booking.objects.filter(patient=request.user).order_by('-booked_at')

    return render(request, 'core/patient_dashboard.html', {
        'slots': slots,
        'bookings': bookings
    })


@login_required
def book_slot(request, slot_id):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'patient':
        return redirect('home')

    slot = get_object_or_404(Slot, id=slot_id, is_booked=False)

    Booking.objects.create(
        patient=request.user,
        doctor=slot.doctor,
        slot=slot
    )
    slot.is_booked = True
    slot.save()

    return redirect('patient_dashboard')