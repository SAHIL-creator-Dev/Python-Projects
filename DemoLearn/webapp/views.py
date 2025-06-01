from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from webapp.models import Student_details
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as student_teach_login,logout
import templates
import os
from datetime import datetime
from .models import Student_details,CV_details,News_management,Event_management,Notice_management,Gallery_management, Staff_management
from .pdf import html2pdf,html2pdf2
# Create your views here.

def splesh_scr(request):
    return render(request,"Splesh_scr.html")
def home(request):
    news_management = News_management.objects.all()
    event_management = Event_management.objects.all()
    notice_management = Notice_management.objects.all()
    return render(request,'home.html',{'news_management':news_management,'event_management':event_management,'notice_management':notice_management})

def staff(request):
    staff_all_data = Staff_management.objects.all()
    return render(request,"staff_member.html",{'staff_all_data':staff_all_data})

def register(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        student_name = student_name.upper()
        student_email=request.POST.get('student_email')
        stu_password=request.POST.get('stu_password')
        confirm_stu_password=request.POST.get('confirm_stu_password')
        if stu_password!=confirm_stu_password:
            messages.error(request,"Please Enter Same Password!")
            return render(request,'register.html')
        try:
            user_student=User.objects.create_user(student_name,student_email,stu_password)
            user_student.save()
            messages.success(request, "Thank you! you are successully signed in.")
            return render(request,'register.html')
        except Exception as e:
            return HttpResponse(e)
    return render(request,'register.html')

def teacher_register(request):
    branch = ['12','05']
    if request.method=='POST':
        faculty_id=request.POST.get('faculty_id')
        branch_id=request.POST.get('branch_id')
        if branch_id in branch:
            pass
        else:
            messages.error(request,"Please Enter valid Branch ID!")
            return render(request,'teacher_register.html')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            messages.error(request,"Please Enter Same Password!")
            return render(request,"teacher_register.html")
        try:
            user_teacher=User.objects.create_user(faculty_id,branch_id,password)
            user_teacher.save()
        except Exception as e:
            return HttpResponse(e)
        messages.success(request, "Thank you! you are successully signed in.")
    return render(request,'teacher_register.html')

def teacher_login(request):
    if request.method=='POST':
        branch_id=request.POST.get('branch_id')
        faculty_id=request.POST.get('faculty_id')
        password=request.POST.get('password')
        user_teacher = authenticate(request,username=faculty_id,password=password)
        teacher_detail = User.objects.all()
        validate = 1
        try:
            if user_teacher is not None:
                for teacher in teacher_detail:
                    if branch_id == teacher.email:
                        validate = 0
                        student_teach_login(request,user_teacher)
                        return render(request,'teacher_student_select.html',{'branch_id':branch_id})
                if validate == 1:
                    messages.error(request,"Please Enter correct BRANCH ID!")
                    return render(request,'teacher_login.html')
            else:
                messages.error(request,'please Enter correct ID or Password!')
                return render(request,'teacher_login.html')
        except Exception as e:
            return HttpResponse(e)
    return render(request,'teacher_login.html')

def login(request):
    if request.method=='POST':
        student_detail = Student_details.objects.all()
        student_login_username = request.POST.get('student_login_username')
        student_login_password = request.POST.get('student_login_password')
        stu_roll_no = request.POST.get('stu_roll_no')
        if student_login_username != student_login_username.upper():
            messages.error(request,"Username must be in UPPER case!")
            return render(request,'login.html')
        valid_roll_no = 1
        for student in student_detail:
            if student.full_name == student_login_username and student.ubter_roll_no == stu_roll_no:
                valid_roll_no = 0
        if valid_roll_no !=0:
            messages.error(request,"Please Enter valid roll no.")
            return render(request,'login.html')
        user_student = authenticate(request,username=student_login_username,password=student_login_password)
        
        try:
            if user_student is not None:
                student_teach_login(request,user_student)
                if(student.branch=="Information Technology"):
                    branch_id = '12'
                elif(student.branch=="Computer Science and Engineering"):
                    branch_id = '05'
                return render(request,'student_view_page.html',{'student_login_username':student_login_username,'student_detail':student_detail,'stu_roll_no':stu_roll_no,'branch_id':branch_id})
            else:
                messages.error(request,"You Entered wrong Username or password!")
        except Exception as e:
            return HttpResponse(e)
    return render(request,'login.html')

# Admin Login
def admin_login(request):
    gallery_data = Gallery_management.objects.all()
    if request.method=='POST':
        admin_username = request.POST.get('admin_username')
        admin_password = request.POST.get('admin_password')
        if admin_username != "InfoNest" or admin_password != "SA44H@il":
            messages.error(request,"You Entered Wrong username or password!")
            return render(request,"Admin_login_page.html",{'gallery_data':gallery_data})
        Admin_user = authenticate(request,username=admin_username,password=admin_password)
        
        try:
            if Admin_user is not None:
                return redirect("admin_panel")
            else:
                return HttpResponse("You are not an Administrator, Please leave this page!")
        except Exception as e:
            return HttpResponse(e)
    return render(request,"Admin_login_page.html")

def admin_panel(request):
    gallery_data = Gallery_management.objects.all()
    return render(request,"Admin_panel.html",{'gallery_data':gallery_data})
# news management
def news_management(request):
    news_management = News_management.objects.all()
    if request.method=='POST':
        news_title = request.POST.get("news-title") 
        news_description = request.POST.get("news-description")
        if news_title=="" and news_description=="":
            messages.error(request,"Please enter both the news title and news description!")
            return render(request,"News_management.html",{'news_management':news_management})
        elif news_title=="":
            messages.error(request,"Please enter a news title!")
            return render(request,"News_management.html",{'news_management':news_management}) 
        elif news_description=="":
            messages.error(request,"Please enter a news discription!")
            return render(request,"News_management.html",{'news_management':news_management})
        news_content = News_management(
            news_title=news_title,
            news_description=news_description
        )
        news_content.save()
        messages.success(request,"News has been successfully Added!")
    return render(request,"News_management.html",{'news_management':news_management})   

def delete_news(request,id):
    if News_management.objects.filter(id=id).exists():
        news = News_management.objects.get(id=id)
        news.delete()
        return redirect('news_management')
    
# Events management
def event_management(request):
    event_management = Event_management.objects.all()
    if request.method=='POST':
        event_title = request.POST.get("event-title") 
        event_description = request.POST.get("event-description")
        if event_title=="" and event_description=="":
            messages.error(request,"Please enter both the event title and event description!")
            return render(request,"Events_managements.html",{'event_management':event_management})
        elif event_title=="":
            messages.error(request,"Please enter a event title!")
            return render(request,"Events_managements.html",{'event_management':event_management}) 
        elif event_description=="":
            messages.error(request,"Please enter a event discription!")
            return render(request,"Events_managements.html",{'event_management':event_management})
        event_content = Event_management(
            event_title=event_title,
            event_description=event_description
        )
        event_content.save()
        messages.success(request,"News has been successfully Added!")
    return render(request,"Events_managements.html",{'event_management':event_management})

def delete_event(request,id):
    event_management = Event_management.objects.all()
    if Event_management.objects.filter(id=id).exists():
        event = Event_management.objects.get(id=id)
        event.delete()
    return redirect('event_management')
# Notice management
def notice_management(request):
    notice_management = Notice_management.objects.all()
    if request.method=='POST':
        notice_title = request.POST.get("notice-title") 
        notice_description = request.POST.get("notice-description")
        if notice_title=="" and notice_description=="":
            messages.error(request,"Please enter both the notice title and notice description!")
            return render(request,"Notice_management.html",{'notice_management':notice_management})
        elif notice_title=="":
            messages.error(request,"Please enter a notice title!")
            return render(request,"Notice_management.html",{'notice_management':notice_management}) 
        elif notice_description=="":
            messages.error(request,"Please enter a notice discription!")
            return render(request,"Notice_management.html",{'notice_management':notice_management})
        notice_content = Notice_management(
            notice_title=notice_title,
            notice_description=notice_description
        )
        notice_content.save()
        messages.success(request,"notice has been successfully Added!")
    return render(request,"Notice_management.html",{'notice_management':notice_management})

def delete_notice(request,id):
    if Notice_management.objects.filter(id=id).exists():
        notice = Notice_management.objects.get(id=id)
        notice.delete()
    return redirect('notice_management')

def gallery_management(request):
    if request.method=="POST":
        image_type=request.POST.get('image_type')
        gallery_img=request.FILES['gallery_img']
        gallery_data = Gallery_management(
            image_type=image_type,
            gallery_img=gallery_img
        )
        gallery_data.save()
        return redirect("admin_panel")
    return redirect("admin_panel")

def remove_gallery_img(request,id):
    if Gallery_management.objects.filter(id=id).exists():
        img = Gallery_management.objects.get(id=id)
        img.delete()
    return redirect("admin_panel")

def staff_management(request):
    if request.method=="POST":
        teacher_name=request.POST.get('teacher_name')
        teacher_role=request.POST.get('teacher_role')
        staff_img=request.FILES['staff_img']
        staff_data = Staff_management(
            staff_name=teacher_name,
            staff_role=teacher_role,
            staff_img=staff_img
        )
        staff_data.save()
    staff_all_data = Staff_management.objects.all()
    return render(request,"staff_management.html",{'staff_all_data':staff_all_data})

def remove_staff_img(request,id):
    if Staff_management.objects.filter(id=id).exists():
        img = Staff_management.objects.get(id=id)
        img.delete()
    return redirect("staff_management")

def student_teacher_logout(request):
    logout(request)
    return redirect('login')

def student_view_page(request):
    return render(request,'student_view_page.html')

def progress_report(request,stu_roll):
    student_details = Student_details.objects.filter(
        ubter_roll_no=stu_roll
    )
    for student in student_details:
        if student.first_year_tot_cgpa == '':
            student.first_year_tot_cgpa = 0
        else:
            student.first_year_tot_cgpa = float(student.first_year_tot_cgpa)

        if student.second_year_tot_cgpa == '':
            student.second_year_tot_cgpa = 0
        else:
            student.second_year_tot_cgpa = float(student.second_year_tot_cgpa)

        if student.third_year_tot_cgpa == '':
            student.third_year_tot_cgpa = 0
        else:
            student.third_year_tot_cgpa = float(student.third_year_tot_cgpa)

        if student.first_sem_marks == '':
            student.first_sem_marks = 0
        else:
            student.first_sem_marks = float(student.first_sem_marks)

        if student.second_sem_marks == '':
            student.second_sem_marks = 0
        else:
            student.second_sem_marks = float(student.second_sem_marks)

        if student.third_sem_marks == '':
            student.third_sem_marks = 0
        else:
            student.third_sem_marks = float(student.third_sem_marks)

        if student.forth_sem_marks == '':
            student.forth_sem_marks = 0
        else:
            student.forth_sem_marks = float(student.forth_sem_marks)

        if student.sixth_sem_marks == '':
            student.sixth_sem_marks = 0
        else:
            student.sixth_sem_marks = float(student.sixth_sem_marks)

        if student.first_year_tot_per == '':
            student.first_year_tot_per = 0
        else:
            student.first_year_tot_per = float(student.first_year_tot_per)

        if student.second_year_tot_per == '':
            student.second_year_tot_per = 0
        else:
            student.second_year_tot_per = float(student.second_year_tot_per)

        if student.third_year_tot_per == '':
            student.third_year_tot_per = 0
        else:
            student.third_year_tot_per = float(student.third_year_tot_per)

        if student.first_year_tot_cgpa!=0 and student.second_year_tot_cgpa!=0 and student.third_year_tot_cgpa!=0:
            avg_cgpa = (student.first_year_tot_cgpa+student.second_year_tot_cgpa+student.third_year_tot_cgpa)/3
        elif student.second_year_tot_cgpa!=0 and student.third_year_tot_cgpa!=0:
            avg_cgpa = (student.second_year_tot_cgpa+student.third_year_tot_cgpa)/2
        elif student.first_year_tot_cgpa!=0 and student.second_year_tot_cgpa!=0:
            avg_cgpa = (student.first_year_tot_cgpa+student.second_year_tot_cgpa)/2
        elif student.first_year_tot_cgpa!=0:
            avg_cgpa = student.first_year_tot_cgpa
        elif student.second_year_tot_cgpa!=0:
            avg_cgpa = student.second_year_tot_cgpa
        else:
            avg_cgpa = student.third_year_tot_cgpa
        high_sem_marks = max(student.first_sem_marks,student.second_sem_marks,student.third_sem_marks,student.forth_sem_marks,student.forth_sem_marks,student.sixth_sem_marks)
        if student.first_year_tot_per!=0 and student.second_year_tot_per!=0 and student.third_year_tot_per !=0:
            avg_year_per = (student.first_year_tot_per+student.second_year_tot_per+student.third_year_tot_per)/3
        elif student.second_year_tot_per!=0 and student.third_year_tot_per !=0:
            avg_year_per = (student.second_year_tot_per+student.third_year_tot_per)/2
        elif student.first_year_tot_per!=0 and student.second_year_tot_per!=0:
            avg_year_per = (student.first_year_tot_per+student.second_year_tot_per)/2
        elif student.first_year_tot_per!=0:
            avg_year_per = student.first_year_tot_per
        elif student.second_year_tot_per!=0:
            avg_year_per =student.second_year_tot_per
        else:
            avg_year_per = student.third_year_tot_per
    return render(request,"Progress_report.html",{'student_details':student_details,'avg_cgpa':avg_cgpa,'high_sem_marks':high_sem_marks,'avg_year_per':avg_year_per})

def teacher_view_page(request,sel_b,branch_id):
    sel_batch = sel_b
    if(branch_id=='12'):
        branch_id="Information Technology"
    elif(branch_id=='05'):
        branch_id="Computer Science and Engineering"
    # Filter students based on the selected criteria
    student_detail = Student_details.objects.filter(
            passing_year=sel_batch,
            branch=branch_id
        )
    if(branch_id=="Information Technology"):
        branch_id='12'
    elif(branch_id=="Computer Science and Engineering"):
        branch_id='05'
    return render(request,'teacher_view_page.html',{'sel_batch':sel_batch,'student_detail':student_detail,'branch_id':branch_id})

def pdf(request,branch_id, sel_b):
    if(branch_id=='12'):
        branch_id="Information Technology"
    elif(branch_id=='05'):
        branch_id="Computer Science and Engineering"
    sel_batch = sel_b

    # Filter students based on the selected criteria
    student_detail = Student_details.objects.filter(
        branch=branch_id,
        passing_year=sel_batch
    )

    pdf_response = html2pdf2('all_student_pdf1.html', {
        'branch_id':branch_id,
        'sel_batch': sel_batch,
        'student_detail': student_detail
    })

    if isinstance(pdf_response, HttpResponse):
        return pdf_response
    else:
        return HttpResponse("Error generating PDF", content_type="text/plain")


def stu_det_pdf(request, roll_no):
    student_detail = Student_details.objects.filter(ubter_roll_no=roll_no)

    # Generate PDF
    response = html2pdf('stu_det_pdf1.html', {'student_detail': student_detail})
    
    # Return as a file
    response['Content-Disposition'] = 'inline; filename="student_details.pdf"'
    return response

def dashboard_student_data(request):
    if request.method=='POST':
        ubter_roll_no = request.POST.get('student_roll_no')
        student_detail = Student_details.objects.all()
        return render(request,'dashboard_student_data.html',{'ubter_roll_no':ubter_roll_no,'student_detail':student_detail})
    return render(request,'teacher_view_page.html')

def teacher_student_select(request,branch_id):
    if request.method=='POST':
        sel_batch = request.POST.get('sel_batch')
        branch_id=branch_id
        return redirect('teacher_view_page',sel_batch,branch_id)
    return render(request,'teacher_student_select.html', {'branch_id': branch_id})


def delete_user(request, roll_no,branch_id):
    if request.method=='POST':
        sel_stu_data = Student_details.objects.get(ubter_roll_no=roll_no)
        batch = sel_stu_data.passing_year
        sel_stu_data.delete()
        branch_id=branch_id
        return render(request,'delete_message_page.html',{'branch_id':branch_id,'batch':batch})
def student(request):
    if request.method=='POST':
        Student_img = request.FILES['student_img']
        full_name = request.POST.get('full_name')
        full_name = full_name.upper()
        father_name = request.POST.get('fathers_name')
        father_occupation = request.POST.get('father_occupation')
        mother_name = request.POST.get('mothers_name')
        mother_occupation = request.POST.get('mother_occupation')
        gender = request.POST.get('gender')
        current_address = request.POST.get('current_address')
        permanent_address = request.POST.get('permanent_address')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        phone_no = request.POST.get('phone')
        parent_phone = request.POST.get('parent_phone')
        adhar_no = request.POST.get('adhar_no')
        email = request.POST.get('email')
        ubter_roll_no = request.POST.get('ubter_roll_no')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        sem = request.POST.get('semester')
        first_sem_marks = request.POST.get('first_sem_marks')
        second_sem_marks = request.POST.get('second_sem_marks')
        first_year_tot_cgpa = request.POST.get('first_year_tot_cgpa')
        first_year_tot_per = request.POST.get('first_year_tot_per')
        third_sem_marks = request.POST.get('third_sem_marks')
        forth_sem_marks = request.POST.get('forth_sem_marks')
        second_year_tot_cgpa = request.POST.get('second_year_tot_cgpa')
        second_year_tot_per = request.POST.get('second_year_tot_per')
        fifth_sem_marks = request.POST.get('fifth_sem_marks')
        sixth_sem_marks = request.POST.get('sixth_sem_marks')
        third_year_tot_cgpa = request.POST.get('third_year_tot_cgpa')
        third_year_tot_per = request.POST.get('third_year_tot_per')
        passing_year = request.POST.get('passing_year')
        high_sc_name = request.POST.get('high_sc_name')
        sel_high_board = request.POST.get('sel_high_board')
        high_sc_pass_year = request.POST.get('high_sc_pass_year')
        high_sc_per = request.POST.get('high_sc_per')
        inter_col_name = request.POST.get('inter_col_name')
        sel_inter_board = request.POST.get('sel_inter_board')
        inter_col_pass_year = request.POST.get('inter_col_pass_year')
        inter_per = request.POST.get('inter_per')
        student_details = Student_details(
            img=Student_img,
            full_name=full_name,
            father_name=father_name,
            father_occupation=father_occupation,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            gender=gender,
            current_stu_address=current_address,
            permanent_stu_address=permanent_address,
            dob=dob,
            category=category,
            phone_no=phone_no,
            parent_phone=parent_phone,
            adhar_no=adhar_no,
            email=email,
            ubter_roll_no=ubter_roll_no,
            branch=branch,
            year=year,
            sem=sem,
            first_sem_marks=first_sem_marks,
            second_sem_marks=second_sem_marks,
            first_year_tot_cgpa=first_year_tot_cgpa,
            first_year_tot_per=first_year_tot_per,
            third_sem_marks=third_sem_marks,
            forth_sem_marks=forth_sem_marks,
            second_year_tot_cgpa=second_year_tot_cgpa,
            second_year_tot_per=second_year_tot_per,
            fifth_sem_marks=fifth_sem_marks,
            sixth_sem_marks=sixth_sem_marks,
            third_year_tot_cgpa=third_year_tot_cgpa,
            third_year_tot_per = third_year_tot_per,
            passing_year=passing_year,
            high_sc_name=high_sc_name,
            sel_high_board=sel_high_board,
            high_sc_pass_year=high_sc_pass_year,
            high_sc_per=high_sc_per,
            inter_col_name=inter_col_name,
            sel_inter_board=sel_inter_board,
            inter_col_pass_year=inter_col_pass_year,
            inter_per=inter_per
        )
        student_details.save()
        messages.success(request, f"Thank you {full_name}! Your details have been successfully submitted. We appreciate your cooperation!.")
    return render(request,'student_details.html')

def student_cv(request,roll):
    cv_details = CV_details.objects.filter(roll_no = roll)
    skill=""
    project=""
    certificate=""
    hobby=""
    skills = []
    projects = []
    certificates = []
    hobbies = []
    for cv in cv_details:
        skill = cv.skills
        project = cv.projects
        certificate = cv.certificates
        hobby = cv.hobbies
    skills=skill.split("$")
    projects=project.split("$")
    certificates=certificate.split("$")
    hobbies=hobby.split("$")
    student_details = Student_details.objects.filter(ubter_roll_no=roll)
    return render(request,"cv.html", {'student_details':student_details,'cv_details':cv_details,'skills':skills,'projects':projects,'certificates':certificates,'hobbies':hobbies,'roll':roll})

def update_cv(request, roll_no):
    student_details = Student_details.objects.filter(ubter_roll_no=roll_no)
    cv_details = CV_details.objects.filter(
        roll_no = roll_no
    )
    skill=""
    project=""
    certificate=""
    hobby=""
    skills = []
    projects = []
    certificates = []
    hobbies = []
    for cv in cv_details:
        skill = cv.skills
        project = cv.projects
        certificate = cv.certificates
        hobby = cv.hobbies
    skills=skill.split("$")
    projects=project.split("$")
    certificates=certificate.split("$")
    hobbies=hobby.split("$")
    return render(request,"cv_update.html",{'student_details':student_details,'cv_details':cv_details,'skills':skills,'projects':projects,'certificates':certificates,'hobbies':hobbies,'roll':roll_no})

def cv_update_logic(request,roll):
    cv_detail = CV_details.objects.get(roll_no=roll)
    if request.method=='POST':
        cv_detail.about_me = request.POST.get('about_me')
        cv_detail.email = request.POST.get('email')
        cv_detail.skills = request.POST.get('about_me')
        skills = request.POST.getlist('skills[]')
        skills_str=""
        for skill in skills:
            if skill==skills[len(skills)-1]:
                skills_str+=skill
            else:
                skills_str += skill+"$"
        projects = request.POST.getlist('projects[]')
        projects_str=""
        for project in projects:
            if project==projects[len(projects)-1]:
                projects_str+=project
            else:
                projects_str += project+"$"
        certificates = request.POST.getlist('certificates[]')
        certificates_str=""
        for certificate in certificates:
            if certificate==certificates[len(certificates)-1]:
                certificates_str+=certificate
            else:
                certificates_str += certificate+"$"
        hobbies = request.POST.getlist('hobbies[]')
        hobbies_str=""
        for hobby in hobbies:
            if hobby==hobbies[len(hobbies)-1]:
                hobbies_str+=hobby
            else:
                hobbies_str += hobby+"$"
        cv_detail.skills = skills_str
        cv_detail.projects = projects_str
        cv_detail.certificates = certificates_str
        cv_detail.hobbies = hobbies_str
        cv_detail.save()
        return redirect("student_cv",roll)
        
def cv_form(request,stu_roll):
    cv_details = CV_details.objects.filter(
        roll_no = stu_roll
    )
    if cv_details.exists():
        for cv in cv_details:
            if cv.roll_no==stu_roll:
                messages.error(request,"Data already exist!")
                return render(request,"cv_form.html")
    if request.method=='POST':
        about_me = request.POST.get('about_me')
        email = request.POST.get('email')
        skills = request.POST.get('about_me')
        skills = request.POST.getlist('skills[]')
        skills_str=""
        for skill in skills:
            if skill==skills[len(skills)-1]:
                skills_str+=skill
            else:
                skills_str += skill+"$"
        projects = request.POST.getlist('projects[]')
        projects_str=""
        for project in projects:
            if project==projects[len(projects)-1]:
                projects_str+=project
            else:
                projects_str += project+"$"
        certificates = request.POST.getlist('certificates[]')
        certificates_str=""
        for certificate in certificates:
            if certificate==certificates[len(certificates)-1]:
                certificates_str+=certificate
            else:
                certificates_str += certificate+"$"
        hobbies = request.POST.getlist('hobbies[]')
        hobbies_str=""
        for hobby in hobbies:
            if hobby==hobbies[len(hobbies)-1]:
                hobbies_str+=hobby
            else:
                hobbies_str += hobby+"$"
        
        all_cv_details = CV_details(
            roll_no=stu_roll,
            about_me=about_me,
            email=email,
            skills=skills_str,
            projects=projects_str,
            certificates=certificates_str,
            hobbies=hobbies_str
        )
        all_cv_details.save()
        messages.success(request,"Your data has been Saved!")
        return render(request,"cv_form.html")
    
    return render(request,"cv_form.html",{'roll':stu_roll})
def update_student_details(request, roll_no, full_name, side,branch_id):
    student_detail = Student_details.objects.filter(
        ubter_roll_no=roll_no,
        full_name=full_name
    )
    if side=='student_side':
        return render(request,'student_update_detail.html',{'student_detail':student_detail,'branch_id':branch_id})
    elif side=='teacher_side':
        return render(request,'update_student_details.html',{'student_detail':student_detail,'branch_id':branch_id})

def update(request,id,side,branch_id):
    student_details = Student_details.objects.get(id=id)
    batch=student_details.passing_year
    if request.method=='POST':
        if 'student_img' in request.FILES :
            if student_details.img and os.path.exists(student_details.img.path):
                os.remove(student_details.img.path)
            student_details.img = request.FILES['student_img']
        student_details.full_name = request.POST.get('full_name').upper()
        student_details.father_name = request.POST.get('fathers_name')
        student_details.father_occupation = request.POST.get('father_occupation')
        student_details.mother_name = request.POST.get('mothers_name')
        student_details.mother_occupation = request.POST.get('mother_occupation')
        student_details.current_stu_address = request.POST.get('current_address')
        student_details.permanent_stu_address = request.POST.get('permanent_address')

        dob_str = request.POST.get('dob')
        format1 = "%b. %d, %Y"
        format2 = "%d/%m/%Y"
        formatted_date = None
        try:
            # Convert to datetime object
            date_obj = datetime.strptime(dob_str, format1)
            # Convert back to string in the required format
            formatted_date = date_obj.strftime("%Y-%m-%d")
            student_details.dob = formatted_date
        except ValueError:
            try:
                date_obj = datetime.strptime(dob_str, format2)
                formatted_date = date_obj.strftime("%Y-%m-%d")
                student_details.dob = formatted_date
            except ValueError:
                messages.error(request,"The date you entered is not in the correct format. Please use the following format: YYYY-MM-DD")
                return render(request,'message_page.html')
        
        student_details.category = request.POST.get('category')
        student_details.phone_no = request.POST.get('phone')
        student_details.parent_phone = request.POST.get('parent_phone')
        student_details.adhar_no = request.POST.get('adhar_no')
        student_details.email = request.POST.get('email')
        student_details.ubter_roll_no = request.POST.get('ubter_roll_no')
        student_details.branch = request.POST.get('branch')
        student_details.year = request.POST.get('year')
        student_details.sem = request.POST.get('semester')
        student_details.first_sem_marks = request.POST.get('first_sem_marks')
        student_details.second_sem_marks = request.POST.get('second_sem_marks')
        student_details.first_year_tot_cgpa = request.POST.get('first_year_tot_cgpa')
        student_details.first_year_tot_per = request.POST.get('first_year_tot_per')
        student_details.third_sem_marks = request.POST.get('third_sem_marks')
        student_details.forth_sem_marks = request.POST.get('forth_sem_marks')
        student_details.second_year_tot_cgpa = request.POST.get('second_year_tot_cgpa')
        student_details.second_year_tot_per = request.POST.get('second_year_tot_per')
        student_details.fifth_sem_marks = request.POST.get('fifth_sem_marks')
        student_details.sixth_sem_marks = request.POST.get('sixth_sem_marks')
        student_details.third_year_tot_cgpa = request.POST.get('third_year_tot_cgpa')   
        student_details.third_year_tot_per = request.POST.get('third_year_tot_per')
        student_details.passing_year = request.POST.get('passing_year')
        student_details.high_sc_name = request.POST.get('high_sc_name')
        student_details.sel_high_board = request.POST.get('sel_high_board')
        student_details.high_sc_pass_year = request.POST.get('high_sc_pass_year')
        student_details.high_sc_per = request.POST.get('high_sc_per')
        student_details.inter_col_name = request.POST.get('inter_col_name')
        student_details.sel_inter_board = request.POST.get('sel_inter_board')
        student_details.inter_col_pass_year = request.POST.get('inter_col_pass_year')
        student_details.inter_per = request.POST.get('inter_per')
        
        student_details.save()
        if side=='student_side':
            messages.success(request,"Your changes have been saved and are now effective.")
            return render(request,'message_page.html',{'side':side,'branch_id':branch_id,'batch':batch})
        elif side=='teacher_side':
            messages.success(request,"Your changes have been saved and are now effective.")
            return render(request,'message_page.html',{'side':side,'branch_id':branch_id,'batch':batch})

# about us page
def about_us(request):
    return render(request,'about_us.html')

# Caurses pages
def course_detail_cse(request):
    return render(request,"course_detail_cse.html")

def course_detail_it(request):
    return render(request,"course_detail_it.html")

# Gallery page
def gallery(request):
    gallery_data = Gallery_management.objects.all()
    return render(request,"photo_gall.html",{'gallery_data':gallery_data})

# Addmission page
def addmission(request):
    return render(request,"addmission_page.html")

# Books
def books_page(request):
    return render(request,"Books_page.html")


# chatbot code
from django.shortcuts import render

# In your views.py

from django.http import JsonResponse

import random

def get_bot_reply(user_message):
    user_message = user_message.lower()
    
    if "hello" in user_message or "hi" in user_message:
        responses = ["Hi! How can I help you today?", "Hello! What can I do for you?", "Hey there! How can I assist you?"]
        return random.choice(responses)
    elif "how are you" in user_message:
        return "I'm doing great, thank you for asking! How can I assist you?"
    elif "bye" in user_message:
        return "Goodbye! Have a wonderful day!"
    elif "thank you" in user_message or "thanks" in user_message:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"

# Chat view to display chat page and handle user input
def chat_view(request):
    chat_history = request.session.get('chat_history', [])
    
    if request.method == 'POST':
        # Get user input
        user_message = request.POST.get('message', '')
        if user_message:
            # Store the user message
            chat_history.append({'sender': 'You', 'message': user_message})
            request.session['chat_history'] = chat_history
            
            # Get bot reply based on user message
            bot_reply = get_bot_reply(user_message)
            chat_history.append({'sender': 'Bot', 'message': bot_reply})
            request.session['chat_history'] = chat_history
    
    return render(request, 'chatbot.html', {'chat_history': chat_history})

# Clear chat history
def clear_chat_history(request):
    if request.method == 'POST':
        # Clear the session data for chat history
        if 'chat_history' in request.session:
            del request.session['chat_history']
        return JsonResponse({'status': 'success'})
