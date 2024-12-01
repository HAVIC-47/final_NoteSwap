from django.urls import path
from . import views  # Import your views here
#
# urlpatterns = [
#     path('', views.index, name='index'),  # Example URL pattern
# ]

# from django.contrib import admin
# from django.urls import path, include
# from NoteSwap_main import views
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#                   path('admin/', admin.site.urls),  # Admin site
#                   path('', views.index, name='home'),  # Home page
#                   path('Price/', views.Price, name='Price'),  # Price page
#                   path('notes/',views.notes, name='notes'),  # Notes page
#                   path('Profile/',views.Profile, name='Profile'),  # Profile page
#                   path('upload/',views.upload, name='upload'),
#                   path('login/', views.login_user, name='login'),
#                   path('logout/', views.logout_user, name='logout'),
#                   path('upload_pdf/', views.upload_pdf, name='upload_pdf'),  # PDF Upload page
#                   path('register/', views.register_user, name='register'),
#                   path('', include('NoteSwap_main.urls'))  # Include app-specific URLs for auth
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Price/', views.Price, name='Price'),
    path('notes/', views.notes, name='notes'),
    path('Profile/', views.Profile, name='Profile'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('register/', views.register_user, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('providers/', views.providers, name='providers'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('package/', views.package, name='package'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('select-subject/', views.select_subject, name='select_subject'),
    path('subject/<int:subject_id>/', views.subject_notes, name='subject_notes'),
    path('upload-note/<int:subject_id>/', views.upload_note, name='upload_note'),
    path('course_list/', views.course_list, name='course_list'),
    path('image_view/', views.image_view, name='image_view'),
    path('topic_select/', views.topic_select, name='topic_select'),

]

