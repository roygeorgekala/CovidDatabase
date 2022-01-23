from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#@csrf_exempt
def index(request):
    return render(request,"index.html")

#@csrf_exempt
def testing(request):
    return render(request, "testing.html")

#@csrf_exempt
def patients(request):
    return render(request, "patientInfo.html")

#@csrf_exempt
def quarantine(request):
    return render(request, "quarantine.html")

def hospital(request):
    return render(request, "hospital.html")

def closeContact(request):
    return render(request, "closeContact.html")

def addPatient(request):
    return render(request, "addPatient.html")

def locality(request):
    return render(request, "locality.html")

def addQuarantine(request):
    return render(request, "addQuarantine.html")

def addCloseContact(request):
    return render(request, "addCloseContact.html")

def getPatients(request,id):
    #try:
    patient = Patient.objects.get(id=id)
    context = {"details":patient}
    return render(request, "patientInfo.html",context)
    '''
    except :
        context = {"error":"No Such patient"}
        return render(request, "patientInfo.html",context)
    '''

def getHospital(request,id):
    #try:
    hospital = Hospital.objects.get(id=id)
    context = {"details":hospital}
    return render(request, "hospital.html",context)
    '''
    except :
        context = {"error":"No Such Hospital"}
        return render(request, "hospital.html",context)
    '''


def getQuarantine(request,id):
    #try:
    quarantine = Quarantine_Info.objects.get(patient_id=id)
    context = {"details":quarantine}
    return render(request, "quarantine.html",context)
    '''
    except:
        context = {"error":"No such information"}
        return render(request, "quarantine.html",context)
    '''

def getCloseContact(request,id):
    #try:
    closeContact = Close_Contact.objects.get(id=id)
    context = {"details":closeContact}
    return render(request, "closeContact.html",context)
    '''
    except:
        context = {"error":"No such information"}
        return render(request, "closeContact.html",context)
    '''


def getLocality(request,id):
    #try:
    locality = Locality.objects.get(pincode=id)
    context = {"details":locality}
    return render(request, "locality.html",context)
    '''

    except:
        context = {"error":"No such information"}
        return render(request, "locality.html",context)
    '''



#@csrf_exempt
def createPatient(request):

    if request.method == 'POST':

        try:
            name = request.POST.get('name')
            address = request.POST.get('address')
            age = request.POST.get('age')
            hospital_id = request.POST.get('hospital_id')
            try:
                hospital = Hospital.objects.get(id=hospital_id)
                hospital.patient_count+=1
                hospital.save()
                hospital.pincode.case_count+=1
                hospital.pincode.save()

            except:
                return render(request, "addPatient.html", {"error":"No such hospital"})

            gender = request.POST.get('gender')
            test_status = request.POST.get('test_status')

            Patient.objects.create(name=name,address=address,age=age, hospital_id=hospital, gender=gender, test_status=test_status)
            print("Patient created")
            return render(request, "index.html", {"data":"Patient created! ID for Patient: "+name+" is  "+ str(Patient.objects.order_by('-id')[0].id) })



        except:
                return render(request, "addPatient.html", {"error":"Invalid Data"})

#@csrf_exempt
def createQuarantineInfo(request):
    if request.method == 'POST':
        #try:
        patient_id = request.POST.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
        except:
            return render(request, "addQuarantine.html", {"error":"No such patient"})
        address = request.POST.get('address')
        test_status = request.POST.get('test_status')

        Quarantine_Info.objects.create(patient_id = patient,address = address, test_status = test_status)
        print("Quar info created")

        return render(request, "index.html", {"data":"Quarantine Info created!" })
        '''
        except None:
                return render(request, "addQuarantine.html", {"error":"Invalid Data"})
        '''

#@csrf_exempt
def createCloseContact(request):

    if request.method == 'POST':

        try:
            name = request.POST.get('name')
            patient_id = request.POST.get('patient_id')
            try:
                patient = Patient.objects.get(id=patient_id)
            except:
                return render(request, "addCloseContact.html",{"error":"No Such Patient"})

            relation = request.POST.get('relation')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            test_status = request.POST.get('test_status')

            Close_Contact.objects.create(name = name, patient_id = patient, relation = relation, age = age, gender = gender, address = address, test_status = test_status)
            print("Close Contact Created")

            return render(request, "index.html", {"data":"Close Contact created! ID for Close Contact: "+name+" is  "+ str(Close_Contact.objects.order_by('-patient_id')[0].id) })
        except None:
                return render(request, "addCloseContact.html",{"error":"Invalid Inputs"})

#@csrf_exempt
def createLocality(request):

    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        Locality.objects.create(pincode=pincode)

        print(pincode)
        print("Locality created")
        return render(request, "index.html", {"data":"Locale created"})

#@csrf_exempt
def createHospital(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pincode = request.POST.get('pincode')
        locality=Locality.objects.get(pk=pincode)
        Hospital.objects.create(name=name, pincode=locality)
        print("Hospital Created")

        return render(request, "index.html", {"data":"Hosp created"})
