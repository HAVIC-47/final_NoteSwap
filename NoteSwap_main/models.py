from django.db import models

# Create your models here.
# models.py

# models.py

# models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user_role = models.CharField(
        max_length=20,
        choices=[('note_provider', 'Note Provider'), ('regular_user', 'Regular User')],
        default='regular_user'
    )
    occupation = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    is_note_provider = models.BooleanField(default=False)


class Note(models.Model):
    notesID =models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    content= models.CharField(max_length=100)
    rating=models.IntegerField(null=True)
    subject = models.CharField(max_length=100, null=True)
    university= models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class PDFUpload(models.Model):
    title = models.CharField(max_length=100)  # Optional title
    pdf_file = models.FileField(upload_to='pdfs/')  # Path to save uploaded PDFs
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='subject_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Note_2(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    note_image = models.ImageField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.subject.name} by {self.uploaded_by.username}"

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption