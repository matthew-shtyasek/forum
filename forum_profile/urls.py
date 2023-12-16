from django.urls import path

from forum_profile.views import ProfileCreateView

app_name = 'forum_profile'


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]
