from api.models import Faculty
from django.urls import path, include
from . import views
from college import views as college_views
from content import views as content_views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # college views
    path('college/', college_views.CollegeList.as_view(), name='college-list'),
    path('college/<str:college_code>/',
         college_views.CollegeDetail.as_view(), name='college-detail'),
    path('branch/',
         college_views.BranchList.as_view(), name="branch-list"),
    path('branch/<str:pk>/',
         college_views.BranchDetail.as_view(), name="branch-detail"),
    path('subject/',
         college_views.SubjectList.as_view(), name="subject-list"),
    path('subject/<str:pk>/',
         college_views.SubjectDetail.as_view(), name="subject-detail"),
    path('portion/',
         college_views.PortionList.as_view(), name="portion-list"),
    path('portion/<str:pk>/',
         college_views.PortionDetail.as_view(), name="portion-detail"),
    path('faculty/',
         college_views.FacultyList.as_view(), name='faculty-list'),
    path('faculty/<str:pk>/',
         college_views.FacultyDetail.as_view(), name='faculty-detail'),
    #     path('gtimetable/',
    #          college_views.GtimetableList.as_view(), name="gtimetable-list"),
    path('gtimetable/',
         college_views.GtimetableDetail.as_view(), name="gtimetable-detail"),

    path('contributor/', content_views.ContributorList.as_view(),
         name='contributor-list'),
    path('contributor/<slug:slug>/',
         content_views.ContributorDetail.as_view(),  name='contributor-detail'),

    path('textbook/', content_views.TextbookList.as_view(), name='textbook-list'),
    path('textbook/<str:pk>/',
         content_views.TextbookDetail.as_view(), name='textbook-detail'),
    #     path('material-list/', views.MaterialList.as_view(), name='material-list'),
    #     path('material-detail/<str:pk>/',
    #          views.MaterialDetail.as_view(), name='material-detail'),
    # path('contributor-detail/<str:pk>/', name='contributor-list'),
    #     path('material-list/', views.MaterialList.as_view(), name='material-list'),
    #     path('recommendation-list/', views.RecommendationList.as_view(),
    #          name='recommendation-list'),

    # path('branch-list/', views.BranchList.as_view(), name="branch-list"),
    # path('branch-detail/<str:pk>/', views.BranchDetail.as_view(), name="branch-detail"),
    # path('course-list/', views.CourseList.as_view(), name="course-list"),
    # path('course-detail/<str:pk>/', views.CourseDetail.as_view(), name="course-detail"),
    # path('user-list/', views.UserList, name="user-list"),
    # path('user-detail/<str:username>/', views.userDetail, name="user-detail"),
    # path('lecture-list/', views.LectureList.as_view(), name='lecture-list'),
    # path('day-list/', views.DayList.as_view(), name='day-list'),
    # path('timetable-list/', views.TimetableList.as_view(), name='timetable-list'),
    # path('portion-list/', views.PortionList.as_view(), name='portion-list'),
    # path('portion-detail/<str:pk>/', views.PortionDetail.as_view(), name='portion-detail'),
    # path('material-list/', views.MaterialList.as_view(), name='material-list'),
    # path('faculty-list/', views.FacultyList.as_view(), name='faculty-list'),
    # path('gsheettable-list/', views.GsheettableList.as_view(), name='gsheettable-list'),
]
