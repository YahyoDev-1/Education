from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField()
    details = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class TeacherDegree(models.TextChoices):
        ASSOCIATE = 'Associate', 'Associate Degree'
        BACHELOR = 'Bachelor', 'Bachelor Degree'
        Master = 'Master', 'Master Degree'
        PhD = 'PhD', 'PhD Degree'
        Doctor = 'Doctor', 'Doctoral Degree'

    name = models.CharField(max_length=100, db_index=True)
    degree = models.CharField(
        max_length=100,
        db_index=True,
        choices=TeacherDegree.choices,
        help_text='Degree',
    )
    phone = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()
    kpi = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    course = models.ManyToManyField(Course)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['degree']),
        ]

    def __str__(self):
        courses = ", ".join(
            c.name for c in self.course.all()
        )
        return f"{self.name} - {courses}"


class Group(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(is_active=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, blank=True)

    objects = StudentManager()

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.name


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.student}-{self.group.name}:{self.amount}"
