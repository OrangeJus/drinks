from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    #get all the drinks