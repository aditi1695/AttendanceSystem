from django.shortcuts import render
import os
# Create your views here.

from .models import Student, Teacher, Course, Lecture
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lecture,Course,Student,Teacher
from django.http import HttpResponseRedirect,request, HttpResponse
from .forms import Lectureform

def viewatt(request,pk):
    students = Student.objects.filter(course_id=pk)
    student_data=[]

    for student in students:
        stu_d=[]
        stu_d.append(student.first_name)
        stu_d.append(student.roll_number)
        num_lec = Lecture.objects.filter(course_id=pk,student_roll_no=student.roll_number).count()
        stu_d.append(num_lec)
        student_data.append(stu_d)
    return render(
        request,
        'view_attendance.html',
        context={'student_data': student_data},
    )

def homepage(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_students = Student.objects.all().count()

    num_teachers = Teacher.objects.all().count()
    # Available books (status = 'a')
    num_lectures = Lecture.objects.count()
    num_course = Course.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'num_students': num_students, 'num_teachers': num_teachers,
                 'num_lectures': num_lectures, 'num_courses': num_course},
    )


class StudentView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student



class CourseListView(generic.ListView):
    model = Course #to add a lecture first course list has to be shown

class CourseDetailView(generic.DetailView):
    model = Course


def LectureCreate(request):
    if request.method == 'POST':
        form1 = Lectureform(request.POST, request.FILES)
        if form1.is_valid():
            course_id = form1.cleaned_data['course_id']
            lecture_image = form1.cleaned_data['lecture_image']
            lecture_id = form1.cleaned_data['lecture_id']
            lecture_date_time = form1.cleaned_data['lecture_date_time']
            student_roll_no = form1.cleaned_data['student_roll_no']
            t = Lecture(course_id = course_id, lecture_image=lecture_image, lecture_id=lecture_id, lecture_date_time = lecture_date_time,student_roll_no = student_roll_no)
            t.save()
            image_name=str(lecture_image)
            here = Lecture.objects.get(lecture_id = lecture_id )
            str_path = "projectBTP/media/lectures/"+image_name
            os.chdir("..")
            os.system("python ./demos/classifier.py infer --multi ./face_rec/generated-embeddings/classifier.pkl "+str_path)
            os.chdir("/root/openface/projectBTP")
            f = open("/root/openface/face_rec/output.txt")
            for line in iter(f):
                line = line.replace("\n", "")
                here.student_roll_no.add(Student.objects.get(roll_number=line))
            f.close()
              #mahak = "140001017"
              #aditi = "140001002"
              #here.student_roll_no.add(Student.objects.get(roll_number = mahak))
              #here.student_roll_no.add(Student.objects.get(roll_number=aditi))

            return HttpResponseRedirect('/image/')

    else:
        form1 = Lectureform()

    return render(request,'image/lecture_form.html', {'form1' : form1})

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

class TeacherCreate(CreateView):
    model = Teacher
    fields = '__all__'
