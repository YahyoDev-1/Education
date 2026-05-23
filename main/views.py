import logging

from django.utils.log import log_message
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *

logger = logging.getLogger('student_logger')


# Create your views here.

class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherListCreateAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(is_active=True)


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_destroy(self, instance):
        # 1. Agar student aktiv (True) bo'lsa, o'chirishni taqiqlaymiz
        if instance.is_active:
            raise ValidationError(
                {'detail': "Aktiv holatdagi talabani o'chirish mumkin emas."}
            )

        # 2. Agar is_active False bo'lsa, xavfsiz o'chirib yuboramiz
        instance.delete()

    def perform_update(self, serializer):

        user = self.request.user

        instance = serializer.save()

        log_message = f"Student (ID: {instance.id}), Name: {instance.name} updated by {user}."

        logger.info(log_message)

class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
