from django.urls import path
'''from .views import  CafeAPIView, CafeDetailAPIView, MenuAPIView, MenuDetailAPIView, FoodAPIView, FoodDetailAPIView'''
from .views import TeacherAPI, TeacherDetailAPI, StudyCenterAPI, StudyCenterDetailAPI, StudentAPI, StudentDetailAPI

urlpatterns = [
    path('teacher/', TeacherAPI.as_view()),
    path('teacher/<int:pk>/', TeacherDetailAPI.as_view()),
    path('study_center/<int:pk>/', StudyCenterDetailAPI.as_view()),
    path('study_center/', StudyCenterAPI.as_view()),
    path('student/', StudentAPI.as_view()),
    path('student/<int:pk>/', StudentDetailAPI.as_view())
]