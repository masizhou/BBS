from django.contrib import admin
from users.models import User
# Register your models here.

admin.site.site_header = 'BBS后台管理系统'
admin.site.site_title = 'BBS后台'
admin.site.index_title = '后台管理'

# 注册模型
admin.site.register(User)
