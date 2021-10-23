from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .models import Contact, BookFirstClass, RegisteredMember, Card, authTrainer, diet, authMember
from django.contrib.auth.models import User, UserManager, auth
from django.core.mail import EmailMessage


# Create your views here.

def home(request):
    return render(request, 'saigym/index.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_pass = request.POST['password2']
        securityQue = request.POST['security']
        ans = request.POST['securityQuestion']

        # Checks password and confirm password are same
        if password == confirm_pass:
            if username == "":
                messages.error(request, "Invalid credential")

            # checks length of username is not greater than 10
            if len(username) > 10:
                messages.error(request, "username must be under 10 characters")
                return redirect('/saigym/Login/')

            # checks username is already exits
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('/saigym/Login/')

            # checks email is already exits
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
            else:
                # saving records in database
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                reg = RegisteredMember(
                    user=user, securityQue=securityQue, answer=ans)
                reg.save()
                messages.info(request, 'User Created')
                return redirect('/saigym/Login/')
        else:
            messages.error(request, 'Password Not Matching')
            return redirect('/saigym/Login/')

    return render(request, 'saigym/blog.html ')


# def registerMember(request):
#     if request.method == 'POST':
#         username = request.POST['user']
#         email = request.POST['email']
#         password = request.POST['password1']
#         confirm_pass = request.POST['password2']
#         security_question = request.POST['security']
#         answer = request.POST['securityQuestion']
#     return render(request, 'saigym/blog.html ')

def about(request):
    return render(request, 'saigym/about-us.html ')


def memberLogin(request):
    return render(request, 'saigym/blog.html')


def memberPanel(request):
    return render(request, 'saigym/memberLogin.html')


def classes(request):
    return render(request, 'saigym/classes.html')


def trainerLogin(request):
    return render(request, 'saigym/trainerDashboard.html')


def admin(request):
    result = User.objects.all()
    return render(request, 'saigym/AdminLogin.html', {'User': result})


def forgotPassword(request):
    return render(request, 'saigym/forgotPassword.html')


def adminLogout(request):
    auth.logout(request)
    return redirect('/')


def memberCard(request):
    member = Card.objects.filter(user=request.user)
    return render(request, 'saigym/memberCard.html', {"Card": member})


def memberCardAdmin(request):
    user = User.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            usr = User.objects.get(pk=request.user.id)
            name = request.POST['name']
            phone = request.POST['phone']
            address = request.POST['address']
            admissionDate = request.POST['admission']
            regNo = request.POST['reg']
            select = request.POST['batch']
            jan = request.POST['jan']
            feb = request.POST['feb']
            march = request.POST['mar']
            april = request.POST['april']
            may = request.POST['may']
            jun = request.POST['jun']
            july = request.POST['july']
            aug = request.POST['aug']
            sept = request.POST['sept']
            octt = request.POST['octt']
            nov = request.POST['nov']
            dec = request.POST['dec']

            if Card.objects.filter(name=name).exists():
                messages.error(
                    request, "This user's card is already created!!!")
                return redirect('/saigym/memberCardAdmin/')

            member = Card(user=usr, name=name, phone=phone, address=address, admission=admissionDate, regno=regNo,
                          select=select, jan=jan, feb=feb, mar=march, apr=april,
                          may=may, jun=jun, july=july, aug=aug, sept=sept, octt=octt, nov=nov, dec=dec)
            member.save()
            messages.success(request, "Card Details saved Successfully.")
    return render(request, 'saigym/memberCardAdmin.html', {'User': user})


def Login(request):
    if request.method == 'POST':
        email = request.POST['un']
        password = request.POST['pass']
        user = auth.authenticate(username=email, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect("/saigym/admin")
            if user.is_staff:
                return HttpResponseRedirect('/saigym/trainerLogin')
            if user.is_active:
                return HttpResponseRedirect('/saigym/memberPanel')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/saigym/Login')
    return render(request, 'saigym/blog.html')


def elements(request):
    return render(request, 'saigym/elements.html ')


def sendEmail(request):
    member = User.objects.all()
    context = {}
    # ch = Contact.objects.filter(user__id=request.user.id)
    # if len(ch)>0:
    #     data = Contact.objects.filter(user__id=request.user.id)
    #     context['data'] = data

    if request.method == "POST":
        rec = request.POST["to"]
        sub = request.POST["sub"]
        msz = request.POST["msz"]

        try:
            em = EmailMessage(sub, msz, to=rec)
            em.send()
            context["status"] = "Email Sent"
            context["cls"] = "alert-success"
        except:
            context["status"] = "Could not Send, Please check Internet Connection / Email Address"
            context["cls"] = "alert-danger"
    return render(request, "saigym/sendmail.html", {'User': member})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if len(name) < 5 or len(email) < 10 or len(subject) < 5 or len(message) < 10 and \
                len(name) == " " or len(email) == " " or len(subject) == " " or len(message) == "":
            messages.error(request, 'Please fill the form correctly...')
            return render(request, 'saigym/contact.html')
        else:
            contact = Contact(name=name, Email=email,
                              message=message, subject=subject)
            contact.save()
            messages.success(request, 'Submitted Successfully')
    return render(request, 'saigym/contact.html')


def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.firstname = request.POST['user']
        user.lastname = request.POST['lastName']
        user.username = request.POST['userName']
        user.email = request.POST['email']
        user.save()
        # messages.success(request, 'Record Updated Successfully')
        return redirect('/saigym/dashboard/')
    return render(request, '/saigym/edit')


def addTrainer(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.firstname = request.POST['user']
        user.lastname = request.POST['lastName']
        user.username = request.POST['userName']
        user.email = request.POST['email']
        if authTrainer.objects.filter(username=user.username).exists():
            messages.error(request, 'Trainer is already added...')
            return HttpResponseRedirect('/saigym/addTrainerDash')
        else:
            user = authTrainer(firstname=user.firstname, lastname=user.lastname,
                               username=user.username, email=user.email)
            user.save()
            # messages.success(request, 'Trainer Added Successfully')
            return redirect('/saigym/addTrainerDash/')
    return render(request, 'saigym/addTrainer.html', {'user': user})


def addMembers(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.firstname = request.POST['user']
        user.lastname = request.POST['lastName']
        user.username = request.POST['userName']
        user.email = request.POST['email']
        if authMember.objects.filter(username=user.username).exists():
            messages.error(request, '{} Member is already added...')
            return HttpResponseRedirect('/saigym/memberShow')
        else:
            user = authMember(firstname=user.firstname, lastname=user.lastname,
                               username=user.username, email=user.email)
            user.save()
            # messages.success(request, 'Trainer Added Successfully')
            return redirect('/saigym/memberShow/')
    return render(request, 'saigym/addMemberDatabase.html', {'user': user})


def updateTrainer(request, id):
    user = authTrainer.objects.get(id=id)
    
    if request.method == 'POST':
        user.firstname = request.POST['user']
        user.lastname = request.POST['lastName']
        user.username = request.POST['userName']
        user.email = request.POST['email']
        # user = authTrainer(firstname=authTrainer.firstname, lastname=authTrainer.lastname, username=authTrainer.username, email=authTrainer.email)
        user.save()
        return redirect('/saigym/updateTrainerDash/')
    return render(request, 'saigym/updateTrainer.html', {'user': user})


def updateTrainerDash(request):
    user = authTrainer.objects.all()
    return render(request, 'saigym/updateTrainerDash.html', {'authTrainer': user})


def deleteTrainer(request, id):
    delt = authTrainer.objects.get(pk=id)
    delt.delete()
    # messages.success(request, 'User deleted Successfully')
    return HttpResponseRedirect('/saigym/updateTrainerDash')


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'saigym/edit.html', {'user': user})


def delete(request, id):
    if request.method == "POST":
        delt = User.objects.get(id=id)
        delt.delete()
        # messages.success(request, 'User deleted Successfully')
        return HttpResponseRedirect('/saigym/admin')


def deleteCard(request, id):
    if request.method == "POST":
        delt = Card.objects.get(pk=id)
        delt.delete()
        # messages.success(request, 'User deleted Successfully')
        return HttpResponseRedirect('/saigym/cardDetailsShow')


def changepass(request):
    if request.method == "POST":
        current = request.POST["curpas"]
        new_pas = request.POST["npas"]

        user = User.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check:
            user.set_password(new_pas)
            user.save()
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect('/saigym/admin')
        else:
            messages.error(request, "Incorrect Current Password")
            return render(request, "saigym/changePassword.html")
    return render(request, "saigym/changePassword.html")


def changePassMember(request):
    if request.method == "POST":
        current = request.POST["curpas"]
        new_pas = request.POST["npas"]

        user = User.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check:
            user.set_password(new_pas)
            user.save()
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect('/saigym/memberPanel')
        else:
            messages.error(request, "Incorrect Current Password")
            return render(request, "saigym/changePassMember.html")
    return render(request, "saigym/changePassMember.html")


def changePassTrainer(request):
    if request.method == "POST":
        current = request.POST["curpas"]
        new_pas = request.POST["npas"]

        user = User.objects.get(id=request.user.id)
        check = user.check_password(current)
        if check:
            user.set_password(new_pas)
            user.save()
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect('/saigym/trainerDashboard')
        else:
            messages.error(request, "Incorrect Current Password")
            return render(request, "saigym/trainerDashboardChangePassword.html")
    return render(request, "saigym/changePassTrainer.html")


def uploadDietWorkout(request):
    user = User.objects.all()
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        select = request.POST['select']
        upload_diet = request.POST['upDiet']
        upload_workout = request.POST['upWork']
        if User is not None:
            user = diet(name=name, email=email, select=select,
                        upload_diet=upload_diet, upload_workout=upload_workout)
            user.save()
            return HttpResponseRedirect('/saigym/trainerLogin/')
    return render(request, 'saigym/DietWorkout.html', {'user': user})


def BookFirstCls(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        select = request.POST.get('batch', '')

        if len(name) < 2 or len(email) < 10 or len(phone) < 10 and \
                len(name) == " " or len(email) == " " or len(phone) == " " or len(select) == " ":
            messages.error(request, "Please fill the data correctly")
            return render(request, 'saigym/classes.html')
        else:
            book = BookFirstClass(name=name, email=email,
                                  phone=phone, select=select)
            book.save()
            messages.success(request,
                             "Your first demo class has been successfully Booked as per selected batch timing. Please arrive on time")
    return render(request, 'saigym/classes.html')


def dashboard(request):
    result = User.objects.all()
    return render(request, "saigym/dashboard.html", {"User": result})


def trainerDashboardChangePassword(request):
    return render(request, 'saigym/changePassTrainer.html')


def addTrainerDash(request):
    result = User.objects.all()
    return render(request, "saigym/addTrainerEdit.html", {"User": result})


def addMember(request):
    result = User.objects.all()
    return render(request, "saigym/addMember.html", {"User": result})


def showqueries(request):
    query = Contact.objects.all()
    return render(request, "saigym/showQueries.html", {"Contact": query})


def bookedClass(request):
    query = BookFirstClass.objects.all()
    return render(request, "saigym/bookedClasses.html", {"BookFirstClass": query})


def cardDetailsShow(request):
    detils = Card.objects.all()
    return render(request, 'saigym/CardShow.html', {'Card': detils})


def memberDetails(request, id):
    user = User.objects.get(id=id)
    return render(request, "saigym/memberDetails.html", {'user': user})


def showDietWorkout(request):
    display_diet = diet.objects.filter(user=request.user)
    return render(request, 'saigym/DietWorkoutShow.html', {'diet': display_diet})


def progress(request):
    return render(request, 'saigym/ProgressReport.html')


def memberShow(request):
    user = User.objects.all()
    return render(request, 'saigym/memberShow.html', {'user': user})


def cardUpdate(request, user_id):
    card = Card.objects.filter(user_id=user_id)
    return render(request, 'saigym/cardUpdate.html', {'card': card})


def updateCardAdmin(request, id):

    if request.method == 'POST':
        card = User.objects.filter(pk=id)
        form = Card(request.POST or None, instance=card)
        if form.is_valid():
            form.save()
        redirect('/saigym/admin')
        # card.phone = request.POST['phone']
        # card.address = request.POST['address']
        # # select = request.POST['batch']
        # card.jan = request.POST['jan']
        # card.feb = request.POST['feb']
        # card.march = request.POST['mar']
        # card.april = request.POST['apr']
        # card.may = request.POST['may']
        # card.jun = request.POST['jun']
        # card.july = request.POST['july']
        # card.aug = request.POST['aug']
        # card.sept = request.POST['spet']
        # card.octt = request.POST['octt']
        # card.nov = request.POST['nov']
        # card.dec = request.POST['dec']
        #
        # card = Card(phone=card.phone, address=card.address,
        #             jan=card.jan, feb=card.feb, mar=card.march, apr=card.april,
        #             may=card.may, jun=card.jun, july=card.july, aug=card.aug, sept=card.sept, octt=card.octt,
        #             nov=card.nov, dec=card.dec)
        # card.save()
        messages.success(request, "Card Details saved Successfully.")
    return render(request, '/saigym/cardUpdate')

def addMemberDatabase(request, id):
    member = User.objects.get(id=id)
    return render(request, 'saigym/addMemberDatabse.html', {'user':member})



def forgotpass(request):
    context = {}
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return HttpResponseRedirect("/admin")
        else:
            return HttpResponseRedirect("/cust_dashboard")
        # context["status"] = "Password Changed Successfully!!!"

    return render(request,"forgot_pass.html",context)

import random

def reset_password(request):
    un = request.GET["username"]
    try:
        user = get_object_or_404(User,username=un)
        otp = random.randint(1000,9999)
        msz = "Dear {} \n{} is your One Time Password (OTP) \nDo not share it with others \nThanks&Regards \nMyWebsite".format(user.username, otp)
        try:
            email = EmailMessage("Account Verification",msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            return JsonResponse({"status":"error","email":user.email})
    except:
        return JsonResponse({"status":"failed"})
