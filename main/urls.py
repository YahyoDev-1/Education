from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view()),

    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view()),

    path('teachers/', TeacherListCreateAPIView.as_view()),

    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view()),

    path('groups/', GroupListCreateAPIView.as_view()),

    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),

    path('students/', StudentListCreateAPIView.as_view()),

    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('payments/', PaymentListCreateAPIView.as_view()),

    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view()),
]
