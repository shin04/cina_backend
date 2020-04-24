from django.contrib import admin
from .models import User, Workspace, WorksapeTable
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

admin.site.register(User)
admin.site.register(Workspace)
admin.site.register(WorksapeTable)
