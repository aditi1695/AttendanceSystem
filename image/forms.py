from django import forms
from .models import Lecture,Course, Student
import datetime


import uuid # Required for unique lecture instances

class Lectureform(forms.Form):
    course_id = forms.ModelChoiceField(queryset=Course.objects.all() ,help_text="Enter Course_ID")
    lecture_image = forms.ImageField(help_text = "Upload Image")
    lecture_id = forms.UUIDField( initial=uuid.uuid4,help_text="Unique ID for each and every Lecture")
    lecture_date_time = forms.DateTimeField(help_text="Date of the Lecture", initial=datetime.datetime.now)
    student_roll_no = forms.ModelMultipleChoiceField(queryset=Student.objects.all() ,required=False, help_text="Enter Course_ID")