from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .forms import SignUpForm
from .models import User, FarmData
from django.views.generic.edit import CreateView
from .resources import FarmDataResource
from tablib import Dataset
from crop_name_recommendation.naive_bayes import NaiveBayes
from crop_name_recommendation.SVM import SVM
from crop_name_recommendation.neural_network import NeuralNetwork
from crop_name_recommendation.random_forest import RandomForest
from crop_name_recommendation.ensemble import ensemble
#from crop_name_recommendation.all_algo import Neural

from collections import Counter

def researchhub(request):
   return render(request, 'crop_name_recommendation/research_hub.html')


def index(request):
   return render(request, 'crop_name_recommendation/details.html')

def home(request):
   return render(request, 'crop_name_recommendation/home.html')

def loginoption(request):
   return render(request, 'crop_name_recommendation/login_option.html')

def svm(request):
   return render(request, 'crop_name_recommendation/svm.html')

def naivebayes(request):
   return render(request, 'crop_name_recommendation/naivebayes.html')

def neuralnetwork(request):
   return render(request, 'crop_name_recommendation/neuralnetwork.html')

def randomforest(request):
   return render(request, 'crop_name_recommendation/randomforest.html')

def ensembleTech(request):
   return render(request, 'crop_name_recommendation/ensemble.html')

def aboutus(request):
   return render(request, 'crop_name_recommendation/aboutus.html')

def contactus(request):
   return render(request, 'crop_name_recommendation/contactus.html')

def signup(request):
       if(request.method == 'GET'):
           return render(request, 'crop_name_recommendation/signup.html')
       else:
          if(request.method == 'POST'):
             user_first_name = request.POST.get('firstname')
             user_last_name = request.POST.get('lastname')
             gender = request.POST.get('Gender')
             userEmail = request.POST.get("email")
             userPassword = request.POST.get("password")
             users = User.objects.filter(user_email = userEmail)
             
             print(" User password :: ",userPassword," User email :: ",userEmail )
             message = "not mentioned"
             url_path = "library_management/login.html"
             if users.count() > 0 :
                for  user in users:   
                   if user.first_name != user_first_name and user.user_email != userEmail:
                      userDetail = User(first_name=user_first_name,last_name=user_last_name,gender=gender,user_email=userEmail,user_password=userPassword)
                      userDetail.save()
                      print("Not find user name :: ")
                      message = 'Registration successfully...'
                      url_path = 'crop_name_recommendation/login.html'
                      break
                   else:
                      url_path = 'crop_name_recommendation/signup.html'
                      message = 'This user name already use. Please try another user name!!..',
             else:
                   userDetail = User(first_name=user_first_name,last_name=user_last_name,gender=gender,user_email=userEmail,user_password=userPassword)
                   userDetail.save()
                   message = 'Registration successfully...'
                   url_path = 'crop_name_recommendation/login.html'
                  
                  
             template = loader.get_template(url_path)
             context = {
                   'message':message,
                   }
             return HttpResponse(template.render(context,request)) 
       
     
def signin(request):
	if(request.method == 'GET'):
	   return render(request, 'crop_name_recommendation/login.html')
	else:
           if(request.method == 'POST'):
               user_name = request.POST.get('email')
               userPassword = request.POST.get('password')
               print("user Name :: ",user_name," User Password :: ",userPassword)
               users = User.objects.filter(user_email=user_name,user_password=userPassword)
               user_path = ''
               if users.count() > 0:
                  for user in users:
                     print("FOR -- user Name :: ",user_name," User Password :: ",userPassword)
                     if user.user_email==user_name and user.user_password == userPassword:
                        print("Login successfully.. ")
                        request.session['session_user_name']=user_name
                        url_path = 'crop_name_recommendation/home.html'
                        message = 'login successfully'
                     else:
                        url_path = 'crop_name_recommendation/login.html'
                        message = 'please check user name and password!!..'
               else:
                  url_path = 'crop_name_recommendation/login.html'
                  message='Please check user name and password!!...'

               template = loader.get_template(url_path)
               context = {
               'message':message,
               }
               return HttpResponse(template.render(context,request))  
      
def userLogout(request):
    try:
        del request.session['session_user_name']
        
    except KeyError:
        pass
    template = loader.get_template('crop_name_recommendation/login.html')
    context = {
               'message':'You\'re logged out.',
      }
    return HttpResponse(template.render(context,request))		

def naiveBayesAlgo(request):
     if(request.method == 'POST'):
        print("request Data :: ",request.body)
        requestJson = json.loads(request.body) 
        test_records = []
        test_records.append(requestJson['soil_type'])
        test_records.append(requestJson['soil_depth'])
        test_records.append(requestJson['ph'])
        test_records.append(requestJson['bulk_density'])
        test_records.append(requestJson['ec'])
        test_records.append(requestJson['organic_carbon'])
        test_records.append(requestJson['soil_moisture_retention'])
        test_records.append(requestJson['availabel_water_capacity'])
        test_records.append(requestJson['infiltration_rate'])
        test_records.append(requestJson['clay'])
# =============================================================================
#         print("ARRAY :: ",test_records)
# =============================================================================
        testD = ",".join(str(item) for item in test_records) 
# =============================================================================
#         print("String Test Data :: ",testD)
# =============================================================================
        naiveBayes = NaiveBayes()
        result = naiveBayes.run_naive_bayes_algorithm(testD)
        response = JsonResponse({'predict_label':result})
        return response
    
def svmAlgo(request): 
    if(request.method == 'POST'):
        print("request Data :: ",request.body)
        requestJson = json.loads(request.body) 
        test_records = []
        test_records.append(requestJson['soil_type'])
        test_records.append(requestJson['soil_depth'])
        test_records.append(requestJson['ph'])
        test_records.append(requestJson['bulk_density'])
        test_records.append(requestJson['ec'])
        test_records.append(requestJson['organic_carbon'])
        test_records.append(requestJson['soil_moisture_retention'])
        test_records.append(requestJson['availabel_water_capacity'])
        test_records.append(requestJson['infiltration_rate'])
        test_records.append(requestJson['clay'])
        testD = ",".join(str(item) for item in test_records) 
        svm = SVM()
        result = svm.runSVMAlgo(testD)
        response = JsonResponse({'predict_label':result})
        return response
    
def neuralNetworkAlgo(request):   
        if(request.method == 'POST'):
                print("request Data :: ",request.body)
                requestJson = json.loads(request.body) 
                test_records = []
                test_records.append(requestJson['soil_type'])
                test_records.append(requestJson['soil_depth'])
                test_records.append(requestJson['ph'])
                test_records.append(requestJson['bulk_density'])
                test_records.append(requestJson['ec'])
                test_records.append(requestJson['organic_carbon'])
                test_records.append(requestJson['soil_moisture_retention'])
                test_records.append(requestJson['availabel_water_capacity'])
                test_records.append(requestJson['infiltration_rate'])
                test_records.append(requestJson['clay'])
                testD = ",".join(str(item) for item in test_records) 
                neuralNetwork = NeuralNetwork()
                result = neuralNetwork.runAlgorithm(testD)
                response = JsonResponse({'predict_label':result})
                return response

def randomForestAlgo(request):   
        if(request.method == 'POST'):
                print("request Data :: ",request.body)
                requestJson = json.loads(request.body) 
                test_records = []
                test_records.append(requestJson['soil_type'])
                test_records.append(requestJson['soil_depth'])
                test_records.append(requestJson['ph'])
                test_records.append(requestJson['bulk_density'])
                test_records.append(requestJson['ec'])
                test_records.append(requestJson['organic_carbon'])
                test_records.append(requestJson['soil_moisture_retention'])
                test_records.append(requestJson['availabel_water_capacity'])
                test_records.append(requestJson['infiltration_rate'])
                test_records.append(requestJson['clay'])
                testD = ",".join(str(item) for item in test_records) 
                randomForest = RandomForest()
                result = randomForest.runRandomForestAlgo(testD)
                response = JsonResponse({'predict_label':result})
                return response

def runEAlgo(request):   
        if(request.method == 'POST'):
                print("request Data :: ",request.body)
                requestJson = json.loads(request.body) 
                test_records = []
                test_records.append(requestJson['soil_type'])
                test_records.append(requestJson['soil_depth'])
                test_records.append(requestJson['ph'])
                test_records.append(requestJson['bulk_density'])
                test_records.append(requestJson['ec'])
                test_records.append(requestJson['organic_carbon'])
                test_records.append(requestJson['soil_moisture_retention'])
                test_records.append(requestJson['availabel_water_capacity'])
                test_records.append(requestJson['infiltration_rate'])
                test_records.append(requestJson['clay'])
                testD = ",".join(str(item) for item in test_records) 
                ensbl = ensemble()
                result = ensbl.runEAlgo(testD)
                response = JsonResponse({'predict_label':result})
                return response   

def fileupload(request):
   nnResult = []
   nbResult = []
   svmResult = []
   rfResult = []
   enResult = []
   if(request.method == 'POST'):
      print("request Data :: ",request.body)
      requestJson = json.loads(request.body) 
      test_records = []
      test_records.append(requestJson['soil_type'])
      test_records.append(requestJson['soil_depth'])
      test_records.append(requestJson['ph'])
      test_records.append(requestJson['bulk_density'])
      test_records.append(requestJson['ec'])
      test_records.append(requestJson['organic_carbon'])
      test_records.append(requestJson['soil_moisture_retention'])
      test_records.append(requestJson['availabel_water_capacity'])
      test_records.append(requestJson['infiltration_rate'])
      test_records.append(requestJson['clay'])
      testD = ",".join(str(item) for item in test_records) 
      neuralNetwork = NeuralNetwork()
      nnResult = neuralNetwork.runAlgorithm(testD)
      df = pd.DataFrame({"Neural ": nnResult, "NaiveBayes":nbResult, "SVM ":svmResult,"RandomF":rfResult, "Ensemble":enResult})
      df.to_csv("allAlgoResult.csv", index = False)
      result = neuralNetwork.runAlgorithm(testD)
      response = JsonResponse({'predict_label':result})
      return response
   

class SoilDataCollectionFormView(LoginRequiredMixin, CreateView):
  template_name = 'crop_name_recommendation/data_collection.html'
  model = FarmData
  fields = '__all__'




# Exporting to CSV view
def exportCsv(request):
    farm_data_resource = FarmDataResource()
    dataset = farm_data_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="agrinepal_datasets.csv"'
    return response

# Exporting to JSON view
def exportJson(request):
    farm_data_resource = FarmDataResource()
    dataset = farm_data_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="agrinepal_datasets.json"'
    return response


# Exporting to Excel view
def exportExcel(request):
    farm_data_resource = FarmDataResource()
    dataset = farm_data_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="agrinepal_datasets.xls"'
    return response
