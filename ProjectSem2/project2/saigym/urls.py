from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="Saigym"),
   path("Register/", views.Register, name="Register"),
   path("addMemberDatabase/<int:id>", views.addMemberDatabase, name="addMemberDatabase"),
   path("showqueries/", views.showqueries, name="showqueries"),
   path("bookedClass/", views.bookedClass, name="bookedClass"),
   path("about/", views.about, name="AboutUs"),
   path("forgotpass/", views.forgotpass, name="forgotpass"),
   path("reset_password/", views.reset_password, name="reset_password"),

   path("cardUpdate/<int:user_id>", views.cardUpdate, name="cardUpdate"),
   path("updateCardAdmin/<int:id>", views.updateCardAdmin, name="updateCardAdmin"),
   path("addMember/", views.addMember, name="addMember"),
   path("memberShow/", views.memberShow, name="memberShow"),
   path("addTrainer/<int:id>", views.addTrainer, name="addTrainer"),
   path("addMembers/<int:id>", views.addMembers, name="addMembers"),
   path("addTrainerDash/", views.addTrainerDash, name="addTrainerDash"),
   path("memberCard/", views.memberCard, name="memberCard"),
   path("deleteCard/<int:id>", views.deleteCard, name="deleteCard"),
   path("deleteTrainer/<int:id>", views.deleteTrainer, name="deleteTrainer"),

   path("cardDetailsShow/", views.cardDetailsShow, name="cardDetailsShow"),
   path("memberCardAdmin/", views.memberCardAdmin, name="memberCardAdmin"),
   path("memberDetails/<int:id>", views.memberDetails, name="memberDetails"),
   path("forgotPassword/", views.forgotPassword, name="forgotPassword"),
   path("updateTrainer/<int:id>", views.updateTrainer, name="updateTrainer"),
   path("updateTrainerDash/", views.updateTrainerDash, name="updateTrainerDash"),

   path("dashboard/", views.dashboard, name="dashboard"),
   path("uploadDietWorkout/", views.uploadDietWorkout, name="uploadDietWorkout"),
   path("changepass/", views.changepass, name="changePassword"),
   path("trainerDashboardChangePassword/", views.trainerDashboardChangePassword, name="trainerDashboardChangePassword"),
   path("sendEmail/", views.sendEmail, name="sendEmail"),
   path("changePassMember/", views.changePassMember, name="changePassMember"),
   path("classes/", views.classes, name="classes"),
   path("memberLogin/", views.memberLogin, name="memberLogin"),
   path("memberPanel/", views.memberPanel, name="memberPanel"),
   path("Login/", views.Login, name="Login"),
   path("elements/", views.elements, name="elements"),
   path("contact/", views.contact, name="Contact us"),
   path("admin/", views.admin, name="AdminLogin"),
   path("progress/", views.progress, name="progress"),
   path("trainerLogin/", views.trainerLogin, name="Trainer Dashboard"),
   path("BookFirstCls/", views.BookFirstCls, name="BookFirstClass"),
   path("uploadDietWorkout/<int:id>", views.uploadDietWorkout, name="uploadDietWorkout"),
   path("adminLogout/", views.adminLogout, name="AdminLogout"),
   path("delete/<int:id>/", views.delete, name="delete"),
   path("edit/<int:id>", views.edit, name="edit"),
   path("update/<int:id>", views.update, name="update"),
   path("showDietWorkout/", views.showDietWorkout, name="showDietWorkout"),


]
