from django.shortcuts import render, redirect
from django.template.context_processors import request

from .forms import PDFUploadForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm
from .models import Subject, Note
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,template_name='index.html')

def Price(request):
    return render(request,template_name='Price.html')

def notes(request):
    return render(request,template_name='notes.html')

@login_required
def Profile(request):
    # Get the logged-in user
    user = request.user
    # You can add any other user-related data here as well
    return render(request, 'Profile.html', {'user': user})

def upload(request):
    return render(request,template_name='upload.html')

def user_profile(request):
    return render(request,template_name='user_profile.html')

def providers(request):
    return render(request,template_name='providers.html')

def contact_us(request):
    return render(request,template_name='contact_us.html')

def package(request):
    return render(request,template_name='package.html')

def coming_soon(request):
    return render(request,template_name='coming_soon.html')

def course_list(request):
    return render(request,template_name='course_list.html')

def topic_select(request):
    return render(request,template_name='topic_select.html')

def provider_profile(request):
    return render(request,template_name='provider_profile.html')

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to the list of PDFs
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to the list of PDFs
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
             messages.success(request, 'there was an error')
        return redirect('login')
    else:

        return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserChangeForm
from .forms import UserProfileForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

def select_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'select_subject.html', {'subjects': subjects})

def subject_notes(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    notes = Note.objects.filter(subject=subject)
    return render(request, 'subject_notes.html', {'subject': subject, 'notes': notes})

@login_required
def upload_note(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if not request.user.is_note_provider:
        return redirect('subject_notes', subject_id=subject_id)  # Restrict access

    if request.method == 'POST':
        note_image = request.FILES.get('note_image')
        Note.objects.create(subject=subject, uploaded_by=request.user, note_image=note_image)
        return redirect('subject_notes', subject_id=subject_id)

    return render(request, 'upload_note.html', {'subject': subject})

from .forms import ImageForm
from .models import Image

# @login_required
def image_view(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "image_view.html", {"obj": obj})
    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request,"image_view.html",{"img": img, "form": form})

# def product_details(request,id):
#     product = Product.objects.get(pk = id)
#     context = {
#         'product':product,
#     }
#     return render(request,template_name = 'product_details.html',context = context)
