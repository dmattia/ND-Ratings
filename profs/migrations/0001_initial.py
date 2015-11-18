# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=255, choices=[(b'Accounting', b'Accounting'), (b'Administrative and Commercial Studies', b'Administrative and Commercial Studies'), (b'Aerospace & Mechanical Engineering', b'Aerospace & Mechanical Engineering'), (b'Airforce Aerospace Studies', b'Airforce Aerospace Studies'), (b'American Studies', b'American Studies'), (b'Anaesthesia & Perioperative Medicine', b'Anaesthesia & Perioperative Medicine'), (b'Anatomy and Cell Biology', b'Anatomy and Cell Biology'), (b'Anthropology', b'Anthropology'), (b'Anthropology', b'Anthropology'), (b'Applied Mathematics', b'Applied Mathematics'), (b'Arabic Language/Literature', b'Arabic Language/Literature'), (b'Architecture', b'Architecture'), (b'Art, Art History, & Design', b'Art, Art History, & Design'), (b'Arts & Letters Departments', b'Arts & Letters Departments'), (b'Biochemistry', b'Biochemistry'), (b'Biological Sciences', b'Biological Sciences'), (b'Biology', b'Biology'), (b'Business Administration', b'Business Administration'), (b'Chemical and Biochemical Engineering', b'Chemical and Biochemical Engineering'), (b'Chemical Engineering', b'Chemical Engineering'), (b'Chemistry', b'Chemistry'), (b'Chemistry & Biochemistry', b'Chemistry & Biochemistry'), (b'Civil and Environmental Engineering', b'Civil and Environmental Engineering'), (b'Civil Engineering', b'Civil Engineering'), (b'Classic Literature/Ancient History', b'Classic Literature/Ancient History'), (b'Classical Studies', b'Classical Studies'), (b'Clinical Neurological Sciences', b'Clinical Neurological Sciences'), (b'Communication Sciences and Disorders', b'Communication Sciences and Disorders'), (b'Computer Applications', b'Computer Applications'), (b'Computer Engineering', b'Computer Engineering'), (b'Computer Science', b'Computer Science'), (b'Dentistry', b'Dentistry'), (b'Diagnostic Radiology and Nuclear Medicine', b'Diagnostic Radiology and Nuclear Medicine'), (b'Dummy', b'Dummy'), (b'Earth Sciences', b'Earth Sciences'), (b'East Asian Languages & Literature', b'East Asian Languages & Literature'), (b'Economics', b'Economics'), (b'Economics', b'Economics'), (b'Electrical and Computer Engineering', b'Electrical and Computer Engineering'), (b'Electrical Engineering', b'Electrical Engineering'), (b'Engineering Departments', b'Engineering Departments'), (b'English', b'English'), (b'English', b'English'), (b'Epidemiology and Biostatistics', b'Epidemiology and Biostatistics'), (b'Faculty of Education', b'Faculty of Education'), (b'Family Medicine', b'Family Medicine'), (b'Film Studies', b'Film Studies'), (b'Film, Television, & Theatre', b'Film, Television, & Theatre'), (b'Finance & Business Economics', b'Finance & Business Economics'), (b'First Year Writing Program', b'First Year Writing Program'), (b'French', b'French'), (b'French', b'French'), (b'Gender Studies', b'Gender Studies'), (b'Geography', b'Geography'), (b'German Language & Literature', b'German Language & Literature'), (b'Government', b'Government'), (b'History', b'History'), (b'History', b'History'), (b'Institute for International Peace Studies', b'Institute for International Peace Studies'), (b'Irish Language & Literature', b'Irish Language & Literature'), (b'Italian', b'Italian'), (b'Japanese', b'Japanese'), (b'Kinesiology', b'Kinesiology'), (b'Law', b'Law'), (b'Liberal Studies', b'Liberal Studies'), (b'Management & Administrative Sciences', b'Management & Administrative Sciences'), (b'Marketing', b'Marketing'), (b'Mathematics', b'Mathematics'), (b'Mathematics', b'Mathematics'), (b'MBA', b'MBA'), (b'MBA Program', b'MBA Program'), (b'Mechanical and Materials Engineering', b'Mechanical and Materials Engineering'), (b'Medical Biophysics', b'Medical Biophysics'), (b'Medicine', b'Medicine'), (b'Microbiology and Immunology', b'Microbiology and Immunology'), (b'Modern Languages and Literatures', b'Modern Languages and Literatures'), (b'Music', b'Music'), (b'Naval Science', b'Naval Science'), (b'Nursing', b'Nursing'), (b'Obstetrics and Gynaecology', b'Obstetrics and Gynaecology'), (b'Occupational Therapy', b'Occupational Therapy'), (b'Oncology', b'Oncology'), (b'Ophthalmology', b'Ophthalmology'), (b'Otolaryngology', b'Otolaryngology'), (b'Paediatrics', b'Paediatrics'), (b'Pathology', b'Pathology'), (b'Philosophy', b'Philosophy'), (b'Philosophy', b'Philosophy'), (b'Phsiology and Pharmacology', b'Phsiology and Pharmacology'), (b'Phys. Ed.', b'Phys. Ed.'), (b'Physical Education', b'Physical Education'), (b'Physical Medicine and Rehabilitation', b'Physical Medicine and Rehabilitation'), (b'Physical Therapy', b'Physical Therapy'), (b'Physics', b'Physics'), (b'Physics and Astronomy', b'Physics and Astronomy'), (b'Political Science', b'Political Science'), (b'Preprofessional Studies', b'Preprofessional Studies'), (b'Psychatry', b'Psychatry'), (b'Psychology', b'Psychology'), (b'Psychology', b'Psychology'), (b'Richard Ivey School of Business', b'Richard Ivey School of Business'), (b'Romance Language & Literature', b'Romance Language & Literature'), (b'Russian Languages & Literature', b'Russian Languages & Literature'), (b"Saint Mary's Art", b"Saint Mary's Art"), (b"Saint Mary's Education", b"Saint Mary's Education"), (b"Saint Mary's Mathematics", b"Saint Mary's Mathematics"), (b"Saint Mary's Religious Studies", b"Saint Mary's Religious Studies"), (b'Science (Non-Departmental)', b'Science (Non-Departmental)'), (b'Science, Technology, and Values', b'Science, Technology, and Values'), (b'Sociology', b'Sociology'), (b'Sociology', b'Sociology'), (b'Spanish', b'Spanish'), (b'Statistical and Actuarial Sciences', b'Statistical and Actuarial Sciences'), (b'Surgery', b'Surgery'), (b'Theology', b'Theology'), (b'Visual Arts', b'Visual Arts')])),
                ('college', models.CharField(max_length=64, choices=[(b'Arch', b'Architecture'), (b'AnL', b'Arts & Letters'), (b'Business', b'College of Business'), (b'EG', b'Engineering'), (b'Law', b'Law School'), (b'SMC', b"Saint Mary's"), (b'Science', b'Science')])),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('humor', models.CharField(max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('difficulty', models.CharField(max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('availability', models.CharField(max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('overall', models.CharField(max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('professor', models.ForeignKey(to='profs.Professor', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=64)),
                ('year_taken', models.IntegerField()),
                ('review', models.TextField(max_length=2048)),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(to='profs.Professor')),
            ],
        ),
    ]
