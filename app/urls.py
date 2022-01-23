from django.urls import path

from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-patient',views.createPatient,name="createPatient"),
    path('create-locality',views.createLocality,name="createLocality"),
    path('create-closecontact',views.createCloseContact,name="createCloseContact"),
    path('create-quarantineinfo',views.createQuarantineInfo,name="createQuarantineInfo"),
    path('create-hospital',views.createHospital,name="createHospital"),
    path('testing',views.testing,name="testing"),
    path('patients',views.patients,name='patients'),
    path('get-patients/<int:id>',views.getPatients,name='getPatients'),
    path('get-patients/',views.patients,name='patients'),
    path('quarantine',views.quarantine,name='quarantine'),
    path('get-quarantine/<int:id>',views.getQuarantine,name='getQuarantine'),
    path('get-quarantine/',views.quarantine,name='quarantine'),
    path('add-patient',views.addPatient,name="addPatient"),
    path('add-quarantine',views.addQuarantine,name="addQuarantine"),
    path('close-contact',views.closeContact,name="closeContact"),
    path('get-closeContact/<int:id>',views.getCloseContact,name='getCloseContact'),
    path('get-closeContact/',views.closeContact,name="closeContact"),
    path('add-close-contact',views.addCloseContact,name="addCloseContact"),
    path('hospital',views.hospital,name='hospital'),
    path('get-hospital/<int:id>',views.getHospital,name='getHospital'),
    path('get-hospital/',views.hospital,name='hospital'),
    path('locality',views.locality,name='locality'),
    path('get-locality/<int:id>',views.getLocality,name='getLocality'),
    path('get-locality/',views.locality,name='locality'),

]
