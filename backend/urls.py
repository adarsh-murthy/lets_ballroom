"""Define the backend routes."""
from django.conf.urls import url
from .views.auth_views import RegisterView, SignInView


urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register_view'),
    url(r'^sign_in/$', SignInView.as_view(), name='sign_in_view'),
]
