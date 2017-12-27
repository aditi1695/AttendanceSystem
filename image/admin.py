from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Lecture, Course
#from .models import Student, Teacher, Course

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lecture)
admin.site.register(Course)
