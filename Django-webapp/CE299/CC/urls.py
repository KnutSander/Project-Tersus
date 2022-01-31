# links
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from CC import views
from django.views.generic import TemplateView

admin.site.site_header = 'Project Tersus'

# all urls must be included here
urlpatterns = [
    path('riskgroups/', views.showRiskGroups, name="show risk groups"),
    path('add/', views.addRFIDConnection, name="Add RFID Connection"),
    path('reset/', views.resetDB, name="Fully reset database"),
    path('', views.index, name="home"),
    path('analytics/', views.analytics, name="analytics"),
    path('table/', views.table, name="table"),
    path('simulation/', views.runSimulation, name="Simulation"),
    path('simulation/update', views.updateSimulation, name="Simulation"),
    path('getSimData/', views.getSimulationData, name="Get Simulation Data"),
    path('getSanVol/<int:id>', views.getSanitizerVolume, name="Get Sanitizer Volume"),
    path('refillSan/<int:id>', views.refillSanitizer, name="Refill sanitizer"),
    path('updateScore/<int:id>', views.updateScore, name="Update score"),
    path('reset_password/', views.registration.reset, name="reset_password"),
    path('create/', views.registration.create_acc, name="create_acc"),
    path('user/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls,name="site admin"),
    path('admin/home', TemplateView.as_view(template_name='admin/home.html'), name='Admin Home'),
    path('pdf/', views.generatePDFReport, name="Generate pdf report"),
    path('genSick/', views.generateSickDays, name="Generate users from employees"),
    path('genUsers/', views.generateUsers, name="Generate users from employees"),
    path('genEmails/', views.generateEmails, name="Generate users from employees"),

]
