from django.db import models

# Create your models here.
class Student_details(models.Model):
    # personal Details
    img = models.ImageField(upload_to='student_img/')
    full_name = models.CharField(max_length=60)
    father_name = models.CharField(max_length=60)
    father_occupation = models.CharField(max_length=60,null=True)
    mother_name = models.CharField(max_length=60)
    mother_occupation = models.CharField(max_length=60,null=True)
    gender = models.CharField(max_length=10,null=True)
    current_stu_address = models.TextField(max_length=300,null=True)
    permanent_stu_address = models.TextField(max_length=300,null=True)
    dob = models.DateField()
    category = models.CharField(max_length=10,null=True)
    phone_no = models.BigIntegerField(null=True)
    parent_phone = models.BigIntegerField(null=True)
    adhar_no = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)

    # Educational details
    ubter_roll_no = models.CharField(max_length=11,unique=True,null=True)
    branch = models.CharField(max_length=60)
    year = models.CharField(max_length=255)
    sem = models.CharField(max_length=255)
    
    first_sem_marks = models.CharField(max_length=4,null=True)
    second_sem_marks = models.CharField(max_length=4,null=True)
    first_year_tot_cgpa = models.CharField(max_length=4,null=True)
    first_year_tot_per = models.CharField(max_length=5,null=True)

    third_sem_marks = models.CharField(max_length=4,null=True)
    forth_sem_marks = models.CharField(max_length=4,null=True)
    second_year_tot_cgpa = models.CharField(max_length=4,null=True)
    second_year_tot_per = models.CharField(max_length=5,null=True)

    fifth_sem_marks = models.CharField(max_length=4,null=True)
    sixth_sem_marks = models.CharField(max_length=4,null=True)
    third_year_tot_cgpa = models.CharField(max_length=4,null=True)
    third_year_tot_per = models.CharField(max_length=5,null=True)
    passing_year = models.CharField(max_length=11,null=True)

    high_sc_name = models.CharField(max_length=255,null=True)
    sel_high_board = models.CharField(max_length=255,null=True)
    high_sc_pass_year = models.CharField(max_length=4,null=True)
    high_sc_per = models.CharField(max_length=5,null=True)
    inter_col_name = models.CharField(max_length=255,null=True)
    sel_inter_board = models.CharField(max_length=255,null=True)
    inter_col_pass_year = models.CharField(max_length=4,null=True)
    inter_per = models.CharField(max_length=5,null=True)
    def __str__(self):
        return self.full_name

class CV_details(models.Model):
    roll_no = models.CharField(max_length=12, unique=True)
    about_me = models.CharField(max_length=400,null=True)
    email = models.CharField(max_length=30)
    skills = models.CharField(max_length=300,null=True)
    projects = models.CharField(max_length=300, null=True)
    certificates = models.CharField(max_length=300, null=True)
    hobbies = models.CharField(max_length=300, null=True)


class News_management(models.Model):
    news_title = models.CharField(max_length=60)
    news_description = models.TextField(max_length=260)

class Event_management(models.Model):
    event_title = models.CharField(max_length=60)
    event_description = models.TextField(max_length=260)

class Notice_management(models.Model):
    notice_title = models.CharField(max_length=60)
    notice_description = models.TextField(max_length=260)

class Gallery_management(models.Model):
    image_type = models.CharField(max_length=20,null=True)
    gallery_img = models.ImageField(upload_to='gallery_img/')

class Staff_management(models.Model):
    staff_name = models.CharField(max_length=30,null=True)
    staff_role = models.CharField(max_length=30,null=True)
    staff_img = models.ImageField(upload_to='staff_img/')
