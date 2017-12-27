from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^students/$', views.StudentView.as_view(), name='students'),
    url(r'^student/(?P<pk>\w+)$', views.StudentDetailView.as_view(), name='student-detail'),
    url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
    url(r'^course/(?P<pk>[\w ]+)$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^lecture/create/$', views.LectureCreate, name='lecture_create'),
    url(r'^course/create/$', views.CourseCreate.as_view(), name='course_create'),
    url(r'^student/create/$', views.StudentCreate.as_view(), name='student_create'),
    url(r'^teacher/create/$', views.TeacherCreate.as_view(), name='teacher_create'),
    url(r'^course/viewatt/(?P<pk>[\w ]+)/$', views.viewatt, name='viewatt'),

]