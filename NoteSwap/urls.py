# from django.contrib import admin
# from django.urls import path, include
# from NoteSwap_main import views as noteswap
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin site
#     path('', noteswap.index, name='home'),  # Home page
#     path('Price/', noteswap.Price, name='Price'),  # Price page
#     path('notes/', noteswap.notes, name='notes'),  # Notes page
#     path('Profile/', noteswap.Profile, name='Profile'),  # Profile page
#     path('upload/', noteswap.upload, name='upload'),
#     path('login/', noteswap.login_user, name='login'),
#     path('logout/', noteswap.logout_user, name='logout'),
#     path('upload_pdf/', noteswap.upload_pdf, name='upload_pdf'),  # PDF Upload page
#     path('register/', noteswap.register_user, name='register'),
#     path('', include('NoteSwap_main.urls'))  # Include app-specific URLs for auth
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# from django.urls import path
# from . import views  # Import your views here
#
# urlpatterns = [
#     path('', views.index, name='index'),  # Example URL pattern
# ]
from django.contrib import admin
from django.urls import path, include
from NoteSwap_main import views  # Import views from the correct app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', views.index, name='home'),  # Home page
    path('Price/', views.Price, name='Price'),  # Price page
    path('notes/', views.notes, name='notes'),  # Notes page
    path('Profile/', views.Profile, name='Profile'),  # Profile page
    path('upload/', views.upload, name='upload'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),  # PDF Upload page
    path('register/', views.register_user, name='register'),
    path("image",include("NoteSwap_main.urls")),
    # path('/<str:id>', s_views.product_details, name='product_details'),

                  # Do not redundantly include 'NoteSwap_main.urls' as you've already defined views here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NoteSwap_main.urls')),  # Include app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
