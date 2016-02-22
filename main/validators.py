# -*- coding:utf-8 -*-
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
def validate_registername(value):
	if User.objects.filter(username=value).exists():
		raise ValidationError(("此用户已存在！"))

def validate_image(fieldfile_obj):
	filesize = fieldfile_obj.file.size
	megabyte_limit = 1.0
	if filesize > megabyte_limit*1024*1024:
		raise ValidationError("图片最大尺寸必须小于%sMB。" % str(megabyte_limit))