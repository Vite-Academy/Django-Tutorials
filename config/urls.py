from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('paginations.urls'))
    # path('', include('models.urls'))
    # path('', include('forms.urls'))
    path('', include('todo.urls'))
]
