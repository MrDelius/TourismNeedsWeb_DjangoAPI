from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Need)
admin.site.register(UserProfile)
admin.site.register(UserCommentedNeed)
admin.site.register(UserSawNeed)
admin.site.register(UserLikedNeed)
