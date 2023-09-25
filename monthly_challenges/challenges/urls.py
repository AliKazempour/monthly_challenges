from django.urls import path
from . import views
urlpatterns = [
    path('january/', views.january),
    path('February/',views.february)
]
