from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')) #todas as urls do todo serão incluidos no todo/
]
