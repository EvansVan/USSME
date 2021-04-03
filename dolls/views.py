from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def index(request):
  if request.method=='POST':
    # Read the variables sent via POST from our API
    session_id = request.POST.get("sessionId", None)
    serviceCode = request.POST.get("serviceCode", None)
    phone_number = request.POST.get("phoneNumber", None)
    text = request.POST.get("text")

    response = ""
    #First request
    if text == "":
      response = "CON Select your vendor \n"
      response += "1.Vans \n"
      response += "2.Peter \n"

    elif text == "1":
      response = "CON Choose the product you would like from vannie \n"
      response += "1. Prod1 \n"
      response += "2. Prod2 \n"

    elif text == "1*1":
      response = "CON How many 1 you want? \n"
      response += "1. Number of products \n"
      #response = "2. Go back \n"

    elif text == "1*2":
      response = "CON How many 2 you want? \n"
      response += "1. Number of products \n"
      #response = "2. Go back \n"
    
    elif text == "2":
      response = "CON Choose the product you would like from pete \n"
      response += "1. Prod1 \n"
      response += "2. Prod2 \n"


    elif text == "2*1":
      response = "CON How many 1 you want? \n"
      response += "1. Number of products \n"
      response += "2. Go back \n"

    elif text == "2*2":
      response = "CON How many 2 you want? \n"
      response += "1. Number of products \n"
      response += "2. Go back \n"
    

    return HttpResponse(response)

def detail(request):
    return HttpResponse("You're looking at question ." )
    
