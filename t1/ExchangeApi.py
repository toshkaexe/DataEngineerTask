import requests
import json
import pprint



class Url:
    def __init__(self, url='https://api.exchangeratesapi.io/latest?base'):
        self.url = url

    def setUSD(self):
        self.url='https://api.exchangeratesapi.io/latest?base=USD&start_at=2020-01-01&end_at=2020-09-01'

    def setEUR(self):
        self.url='https://api.exchangeratesapi.io/latest?base=EUR&start_at=2020-01-01&end_at=2020-09-01'

    def setRUB(self):
        self.url='https://api.exchangeratesapi.io/latest?base=RUB&start_at=2020-01-01&end_at=2020-09-01'

    def setAll(self):
        self.url='https://api.exchangeratesapi.io/latest?base=USD&symbols=USD,GBP,EUR,RUB&start_at=2020-01-01&end_at=2020-09-01'

    def setAllUSA(self):
        self.url = 'https://api.exchangeratesapi.io/latest?base=USD&start_at=2021-01-01&start_at=2020-01-01&end_at=2020-09-01'

    def setAllEur(self):
        self.url = 'https://api.exchangeratesapi.io/latest?base=EUR&start_at=2020-01-01&end_at=2020-09-01'
'''
    def __init__(self, url='https://api.exchangeratesapi.io/latest?base'):
        self.url = url

    def setUSD(self):
        self.url='https://api.exchangeratesapi.io/history?base=USD&start_at=2020-01-01&end_at=2020-09-01'

    def setEUR(self):
        self.url='https://api.exchangeratesapi.io/history?base=EUR&start_at=2020-01-01&end_at=2020-09-01'

    def setRUB(self):
        self.url='https://api.exchangeratesapi.io/history?base=RUB&start_at=2020-01-01&end_at=2020-09-01'

    def setAll(self):
        self.url='https://api.exchangeratesapi.io/history?base=USD&symbols=USD,GBP,EUR,RUB&start_at=2020-01-01&end_at=2020-09-01'

    def setAllUSA(self):
        self.url = 'https://api.exchangeratesapi.io/history?base=USD&start_at=2021-01-01&start_at=2020-01-01&end_at=2020-09-01'

    def setAllEur(self):
        self.url = 'https://api.exchangeratesapi.io/history?base=EUR&start_at=2020-01-01&end_at=2020-09-01'
'''

def loadRowdata(url):
    return json.loads(requests.get(url).content)

if __name__ == '__main__':
    print("Tast E1")
    my_url = Url()

    user = input("Are you [B]oss or local [D]ealer? ").upper()
    if user not in "BD" or len(user) != 1:
        print("I do now know what you doeas mean?")
    elif user == 'B': #dealers
        print("Ok, You are Boss")
        targetCurrency = input("Select [D]ollar or [E]uro? ").upper()
        if targetCurrency not in "DE" or len(user) != 1:
            print("I do now know what currency you doeas mean? ")
        elif targetCurrency == "D":
            print("OK, You selected Dollar as target currency")
            my_url.setUSD()
            print("Url for USD = {} ".format(my_url.url))
            print(loadRowdata(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))
        elif targetCurrency == "E":
            print("You selected Euro as target currency")
            my_url.setEUR()
            print("Url for EUR = {} ".format(my_url.url))
            print(loadRowdata(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))
    elif user == "D":
        print("You are Dealer")
        country = input("Please country of Dealers [R]ussia,[E]uropa or [U]SA or [A]ll... ").upper()
        if country not in "REUA" or len(country) != 1:
            print("I do now know to do that, please restart script")
        elif country == 'D':
            my_url.setUSD()
            print("Url for USD = {} ".format(my_url.url))
            print(loadRowdata(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))
        elif country == 'E':
            my_url.setEUR()
            print("Url for EUR = {} ".format(my_url.url))
            print(loadRowdata(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))
        elif country == 'R':
            my_url.setRUB()
            print("Url for Rub = {} ".format(my_url.url))
            print(loadRowdata(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))
        elif country == 'A':
            my_url.setAll()
            print("Url for All = {} ".format(my_url.url))
            pprint.pprint(loadRowdata(my_url.url))









'''
       country = input("Please select country [R]ussia,[E]uropa or [U]SA... ").upper()
    if country not in "REUSA" or len(country) != 1:
        print("I do now know to do that")

    else:
        county = "USA"
        print("County = {} ".format(country))

    targetCurrency = input("Please select currency [D]olar, [E]uro or [A]ll... ").upper()
    if targetCurrency not in "DEA" or len(targetCurrency) != 1:
        print("I do now know to do that")
    if targetCurrency == 'D':
        my_url.setUSD()
        print("Url for USD = {} ".format(my_url.url))
        print(loadRowdata(my_url.url))
        pprint.pprint(loadRowdata(my_url.url))
    elif targetCurrency == 'E':
        my_url.setEUR()
        print("Url for EUR = {} ".format(my_url.url))
        print(loadRowdata(my_url.url))
        pprint.pprint(loadRowdata(my_url.url))
    elif targetCurrency == 'A':
        my_url.setAll()
        print("Url for All = {} ".format(my_url.url))
        pprint.pprint(loadRowdata(my_url.url))
'''
