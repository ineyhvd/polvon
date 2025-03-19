from rest_framework import permissions
from django.utils import timezone
from datetime import timedelta , datetime
from polvon import models
from polvon.models import Comment


class DistrictPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        current_day = datetime.today().weekday()
        if current_day < 5:
            return True
        return False



class TimeDistrictPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            current_time = timezone.now()
            if obj.created_at + timedelta(minutes=2) > current_time:
                return False
            return True
        return True