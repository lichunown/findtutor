#encoding:utf-8
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput
from django.contrib.auth import authenticate
from models import Student, Tutor, Project, Invitation


class SigninForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20)
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(SigninForm, self).clean()
        try:
            username = User.objects.get(username=cleaned_data.get("username")).username
        except User.DoesNotExist:
            raise forms.ValidationError(("用户不存在！"))
        password = cleaned_data.get("password")
        self.user = authenticate(username=username, password=password)
        if self.user is None or not self.user.is_active:
            raise forms.ValidationError(("密码不正确！"))
        return self.cleaned_data



COLLEGES=(
    ('tongxin','通信工程学院'),
    ('dianzi','电子工程学院'),
    ('jisuanji','计算机学院'),
    ('jidian','机电工程学院'),
    ('wuguang','物理与光电工程学院'),
    ('jingguan','经济与管理学院'),
    ('shutong','数学与统计学院'),
    ('renwen','人文学院'),
    ('waiguoyu','外国语学院'),
    ('ruanjian','软件学院'),
    ('weidianzi','微电子学院'),
    ('shengke','生命科学技术学院'),
    ('kongjian','空间科学与技术学院'),
    ('cailiao','先进材料与纳米科技学院'),
    ('wangan','网络与信息安全学院'),
)

class SignupForm(forms.Form):
    global COLLEGES
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密码', max_length=20)
    passwordagain = forms.CharField(label='密码确认', max_length=20)
    sid = forms.CharField(label='学号', max_length=11)
    truename = forms.CharField(label='真实姓名', max_length=20)
    #birthday=forms.DateField(label='出生日期', timezone.now,blank=True)
    college = forms.CharField(label='学院',max_length=20,widget=forms.Select(choices=COLLEGES))
    # def clean(self):
    #     return self.cleaned_data
    # def clean(self):
    #     cleaned_data = super(SignupForm, self).clean()       
    #     if not len(User.objects.filter(username=username)):
    #         if password==passwordagain:
    #             #success
    #             return self.cleaned_data
    #         else:
    #             raise forms.ValidationError(("请确认两次密码输入相同"))
    #     else:
    #         raise forms.ValidationError(("用户名已被使用"))
class ModifyAccountForm(ModelForm):
    class Meta:
        model = Student
       # exclude = ['username','truename']
        fields = ['sid','truename','college','major','birthday','introduction']
        labels = {
            'sid':'学号',
            'truename':"真实姓名",
            'college':"学院",
            'major':'专业',
            'birthday':"生日",
            'introduction':"自我介绍",
        }
        widgets = {
            'introduction': Textarea(attrs={'cols': 50, 'rows': 5}),
        }

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','status','introduction']
        labels = {
            'name':'项目名称',
            'status':"目前状态",
            #'students':'项目成员',
            #'tutors':'导师',
            'introduction':"详细介绍",
        }
        widgets = {
            'introduction': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
class ShowStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['username','truename','college','major','introduction']
        labels={
            'username':'用户名',
            'truename':'真实姓名',
            'college':'学院',
            'major':'专业',
            'introduction':'详细介绍',
        }
        widgets = {
            'introduction': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
class ShowTutorForm(ModelForm):
    class Meta:
        model = Student
        fields = ['truename','college','major','introduction']
        labels={            
            'truename':'真实姓名',
            'college':'学院',
            'major':'专业',
            'introduction':'详细介绍',
        }
        widgets = {
            'introduction': Textarea(attrs={'cols': 50, 'rows': 5}),
        }