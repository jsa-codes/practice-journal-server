"""practicejournal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from practicejournalapi.views import register_user, login_user
from practicejournalapi.views import UserView
from practicejournalapi.views import StudentView
from practicejournalapi.views import InstructorView
from practicejournalapi.views import CommentView
from practicejournalapi.views import GuitarTypeView
from practicejournalapi.views import JournalEntryView
from practicejournalapi.views import AudioView
from practicejournalapi.views import ImageView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'students', StudentView, 'student')
router.register(r'instructors', InstructorView, 'instructor')
router.register(r'comments', CommentView, 'comment')
router.register(r'guitartypes', GuitarTypeView, 'guitartype')
router.register(r'journalentries', JournalEntryView, 'journalentry')
router.register(r'audio', AudioView, 'audio')
router.register(r'images', ImageView, 'image')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('', include(router.urls)),
    path('login', login_user),
    path("admin/", admin.site.urls),
]
