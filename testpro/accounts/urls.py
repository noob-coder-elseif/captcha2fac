from operator import imod
from django.urls import path, include
from .views import some_view, AjaxExampleForm, getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased

from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
# router.register(r'users', getPhoneNumberRegistered_TimeBased, basename='verify')

urlpatterns = [
    path('', include(router.urls)),
    # path('', some_view, name='some_view'),
    path('', AjaxExampleForm.as_view(), name='some_view'),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
]