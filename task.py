import requests
from datetime import datetime

class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.url =f'https://api.currencyfreaks.com/latest?apikey={self.api_key}&symbols=PKR,GBP,EUR,INR&base=EUR'
        self.output = ' '
        self.file_name= datetime.now().strftime('%d %b -%Y')
        print(self.file_name)

    def do_request(self):
        res= requests.get(self.url)
        if res.status_code == 200:
            self.output = res.json()
            print(self.output)

c=Currency()
c.do_request()