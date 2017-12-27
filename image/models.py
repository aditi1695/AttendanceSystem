from django.db import models
from django.urls import reverse
# Create your models here.
import datetime
from django.utils import timezone

import uuid # Required for unique book instances


class Student(models.Model):


    roll_number = models.CharField(primary_key=True, max_length=25, help_text="Enter Roll Number")
    first_name = models.CharField(max_length=100, help_text="Enter First Name",null=True)
    last_name = models.CharField(max_length=100,help_text="Enter Second Name",null=True)
    student_image = models.ImageField(verbose_name=roll_number, help_text="Student Image",upload_to='media/students')
    course_id = models.ManyToManyField('Course',blank=True)
    #lecture_id = models.ManyToManyField('Lecture',blank=True)

    class Meta:
        ordering = ["roll_number"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.roll_number

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('student-detail', args=[str(self.roll_number)])




class Teacher(models.Model):
    first_name = models.CharField(max_length=100, help_text="Enter First Name")
    last_name = models.CharField(max_length=100, help_text="Enter Second Name")
    course_id = models.ManyToManyField('Course',blank=True)

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s %s' % (self.first_name, self.last_name)



class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10, help_text="Course")
    course_name = models.CharField(max_length=100, help_text="Course Name", blank=True)
    Teacher_name = models.ManyToManyField(Teacher,blank=True)
    student_roll_no = models.ManyToManyField(Student,blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.course_id

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """

        return reverse('course-detail',args= [str(self.course_id)])


class Lecture(models.Model):
    lecture_id = models.UUIDField(primary_key=True,default = uuid.uuid4,help_text="Unique ID for each and every Lecture")
    lecture_date_time = models.DateTimeField(help_text="Date of the Lecture",default=datetime.datetime.now)
    #student_name = models.ForeignKey(Student.first_name,blank=True,help_text="After a while")
    student_roll_no = models.ManyToManyField(Student,blank=True)
    course_id = models.ForeignKey(Course)
    lecture_image = models.ImageField(help_text="Image of Lecture",upload_to='media/lectures/')

    class Meta:
        ordering = ["-lecture_date_time"]

    def __str__(self):

        return '%s %s ' % (self.lecture_date_time, self.course_id)



