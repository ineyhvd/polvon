from rest_framework import permissions
from datetime import datetime
from polvon import models
from polvon.models import Comment


class DistrictPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        current_day = datetime.today().weekday()
        if current_day < 5:
            return True

class TimeDistrictPermission(permissions.BasePermission):
    class Meta:
        model=Comment
        def has_permission(self, request, view ):
