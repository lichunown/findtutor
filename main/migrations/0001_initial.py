# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('tag', models.CharField(max_length=3, choices=[('gc', '\u56fd\u521b'), ('yjs', '\u7814\u7a76\u751f'), ('qt', '\u5176\u4ed6')])),
                ('status', models.CharField(max_length=10, choices=[('1', '\u672a\u9605\u8bfb'), ('2', '\u5df2\u9605\u8bfb'), ('3', '\u5df2\u63a5\u53d7'), ('4', '\u672a\u63a5\u53d7'), ('a', '\u672a\u9605\u8bfb'), ('b', '\u5df2\u9605\u8bfb'), ('c', '\u5df2\u63a5\u53d7'), ('d', '\u672a\u63a5\u53d7')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('status', models.CharField(max_length=10, choices=[('1', '\u51c6\u5907\u4e2d'), ('2', '\u521d\u671f'), ('3', '\u4e2d\u671f'), ('4', '\u540e\u671f'), ('5', '\u5df2\u7ed3\u675f')])),
                ('startdate', models.DateField(verbose_name=django.utils.timezone.now)),
                ('introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.CharField(max_length=11)),
                ('truename', models.CharField(max_length=50)),
                ('birthday', models.DateField(verbose_name=django.utils.timezone.now, blank=True)),
                ('college', models.CharField(max_length=50, choices=[('tongxin', '\u901a\u4fe1\u5de5\u7a0b\u5b66\u9662'), ('dianzi', '\u7535\u5b50\u5de5\u7a0b\u5b66\u9662'), ('jisuanji', '\u8ba1\u7b97\u673a\u5b66\u9662'), ('jidian', '\u673a\u7535\u5de5\u7a0b\u5b66\u9662'), ('wuguang', '\u7269\u7406\u4e0e\u5149\u7535\u5de5\u7a0b\u5b66\u9662'), ('jingguan', '\u7ecf\u6d4e\u4e0e\u7ba1\u7406\u5b66\u9662'), ('shutong', '\u6570\u5b66\u4e0e\u7edf\u8ba1\u5b66\u9662'), ('renwen', '\u4eba\u6587\u5b66\u9662'), ('waiguoyu', '\u5916\u56fd\u8bed\u5b66\u9662'), ('ruanjian', '\u8f6f\u4ef6\u5b66\u9662'), ('weidianzi', '\u5fae\u7535\u5b50\u5b66\u9662'), ('shengke', '\u751f\u547d\u79d1\u5b66\u6280\u672f\u5b66\u9662'), ('kongjian', '\u7a7a\u95f4\u79d1\u5b66\u4e0e\u6280\u672f\u5b66\u9662'), ('cailiao', '\u5148\u8fdb\u6750\u6599\u4e0e\u7eb3\u7c73\u79d1\u6280\u5b66\u9662'), ('wangan', '\u7f51\u7edc\u4e0e\u4fe1\u606f\u5b89\u5168\u5b66\u9662')])),
                ('major', models.CharField(max_length=50, blank=True)),
                ('introduction', models.TextField(blank=True)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truename', models.CharField(max_length=50, blank=True)),
                ('college', models.CharField(blank=True, max_length=50, choices=[('tongxin', '\u901a\u4fe1\u5de5\u7a0b\u5b66\u9662'), ('dianzi', '\u7535\u5b50\u5de5\u7a0b\u5b66\u9662'), ('jisuanji', '\u8ba1\u7b97\u673a\u5b66\u9662'), ('jidian', '\u673a\u7535\u5de5\u7a0b\u5b66\u9662'), ('wuguang', '\u7269\u7406\u4e0e\u5149\u7535\u5de5\u7a0b\u5b66\u9662'), ('jingguan', '\u7ecf\u6d4e\u4e0e\u7ba1\u7406\u5b66\u9662'), ('shutong', '\u6570\u5b66\u4e0e\u7edf\u8ba1\u5b66\u9662'), ('renwen', '\u4eba\u6587\u5b66\u9662'), ('waiguoyu', '\u5916\u56fd\u8bed\u5b66\u9662'), ('ruanjian', '\u8f6f\u4ef6\u5b66\u9662'), ('weidianzi', '\u5fae\u7535\u5b50\u5b66\u9662'), ('shengke', '\u751f\u547d\u79d1\u5b66\u6280\u672f\u5b66\u9662'), ('kongjian', '\u7a7a\u95f4\u79d1\u5b66\u4e0e\u6280\u672f\u5b66\u9662'), ('cailiao', '\u5148\u8fdb\u6750\u6599\u4e0e\u7eb3\u7c73\u79d1\u6280\u5b66\u9662'), ('wangan', '\u7f51\u7edc\u4e0e\u4fe1\u606f\u5b89\u5168\u5b66\u9662')])),
                ('introduction', models.TextField(blank=True)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(to='main.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='tutors',
            field=models.ManyToManyField(to='main.Tutor', blank=True),
        ),
        migrations.AddField(
            model_name='invitation',
            name='project',
            field=models.ForeignKey(to='main.Project'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='student',
            field=models.ForeignKey(to='main.Student'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='tutor',
            field=models.ForeignKey(to='main.Tutor'),
        ),
    ]
