from django.urls import path, include
from . import views


urlpatterns = [
    path('<username>/', include(), namespace="home")
    path('<username>/post', include(), namespace="post")
    path('<username>/book', include(), namespace="book")
    path('<username>/literacy', include(), namespace="literacy")
    path('<username>/feeding', include(), namespace="feeding")
    path('<username>/appraisal', include(), namespace="appraisal")
    path('<username>/attendance', include(), namespace="attendance")
]
