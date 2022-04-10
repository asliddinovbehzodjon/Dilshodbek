from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('owner/dilshod/', admin.site.urls),
    path('api/v1/',include('app.urls'))
]
