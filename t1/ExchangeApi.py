import requests
import json
import pprint
import pandas as pd

from Utils import dataParser


class Url:
    def __init__(self, url=''):
        self.url = url

    def setUSD(self):
        self.url = 'https://api.exchangeratesapi.io/history?base=USD&start_at=2020-01-01&end_at=2020-12-31'

    def setEUR(self):
        self.url = 'https://api.exchangeratesapi.io/history?base=EUR&start_at=2020-01-01&end_at=2020-12-31'

    def setRUB(self):
        self.url = 'https://api.exchangeratesapi.io/history?base=RUB&start_at=2020-01-01&end_at=2020-12-31'


def loadRowdata(url):
    return json.loads(requests.get(url).content)


def openJson(json):
    pprint.pprint(json)


def saveDataFrame(url, fileName):
    dataframe = pd.DataFrame(loadRowdata(url))
    pd.DataFrame(dataParser(dataframe)).to_csv(fileName)


currency_List = [
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HRK", "HUF", "IDR", "ILS", "INR",
    "ISK", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB", "TRY", "USD",
    "ZAR"]

if __name__ == '__main__':
    print("Tast E1")
    my_url = Url()

    user = input("Are you [B]oss or local [D]ealer? ").upper()
    if user not in "BD" or len(user) != 1:
        print("I do now know what you does mean?")
    elif user == 'B':
        # boss
        print("Ok, You are Boss")
        targetCurrency = input("Select [D]ollar or [E]uro? ").upper()
        if targetCurrency not in "DE" or len(user) != 1:
            print("I do now know what currency you doeas mean? ")
        elif targetCurrency == "D":
            print("OK, You selected Dollar as target currency")
            my_url.setUSD()
            saveDataFrame(my_url.url, "t1/file_USD.csv")
        elif targetCurrency == "E":
            print("You selected Euro as target currency")
            my_url.setEUR()
            saveDataFrame(my_url.url, "t1/file_EUR.csv")
    elif user == "D":
        # dealers
        print("You are Dealer")
        country = input("Please country of Dealers [R]ussia,[E]uropa or [U]SA...").upper()
        if country not in "REUA" or len(country) != 1:
            print("I do now know to do that, please restart script")
        elif country == 'U':
            print("You selected dollar as target currency")
            my_url.setUSD()
            saveDataFrame(my_url.url, "t1/file_USD.csv")
        elif country == 'E':
            print("You selected Euro as target currency")
            my_url.setEUR()
            saveDataFrame(my_url.url, "t1/file_EUR.csv")
        elif country == 'R':
            print("You selected Rub as target currency")
            my_url.setRUB()
            saveDataFrame(my_url.url, "t1/file_RUB.csv")

        # for the test
        # openJson(loadRowdata("https://api.exchangeratesapi.io/history?base=USD&start_at=2020-01-01&end_at=2020-09-01"))
