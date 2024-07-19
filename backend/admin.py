from django.contrib import admin
from backend.models import (
    CustomUser,
)

admin.site.register([
   CustomUser,
])