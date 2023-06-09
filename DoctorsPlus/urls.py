from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('', include('Home.urls')),
    path('admin/', admin.site.urls),
    path('patient/',include('patient.urls')),
    path('doctor/', include('doctor.urls')),
    path('admins/', include('adminView.urls'))
]
