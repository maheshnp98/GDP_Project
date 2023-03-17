from django.shortcuts import render
from .models import GDP
import requests



def gdp_data(request):
    gdp_data = GDP.objects.all()
    gdp_inr_data = []
    for gdp in gdp_data:
        response = requests.get(f'https://anyapi.io/api/v1/exchange/convert?base=USD&to=INR&amount=100&apiKey=d835gcflb2g2flr26kfl28ks86rffre3dkvhncs97a6jspbvdd1no')
        if response.status_code == 200:
            gdp_inr = response.json()['rate']['INR']
            gdp_inr_data.append({'year': gdp.year, 'gdp_inr': gdp_inr, })
    return render(request, 'gdp_data.html', {'gdp_data': gdp_inr_data})



# https://anyapi.io/api/v1/exchange/convert?base=USD&to=INR&amount=100&apiKey=d835gcflb2g2flr26kfl28ks86rffre3dkvhncs97a6jspbvdd1no


# https://api.currencyfreaks.com/latest?apikey=797b4840ea8e48df9184fb5116f8e8ef=gdp.gdp_data