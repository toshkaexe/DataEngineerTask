import pandas as pd

currency_List = [
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HRK", "HUF", "IDR", "ILS", "INR",
    "ISK", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB", "TRY", "USD",
    "ZAR"]

UDS_EURLIST = ["USD", "EUR"]

if __name__ == '__main__':
    print("Task E1_3")
    while True:
        target_currency = input("Please Enter target currency").upper()
        if any(x in target_currency for x in currency_List):
            target_day = input("Please Enter the day yyyy-mm-dd").upper()
            target_price = input("Enter price").upper()
            targer_c = input("Price in Eur or USD").upper()
            if any(x in targer_c for x in UDS_EURLIST):
                if targer_c == "USD":

                    print("target_currency= {}".format(target_currency))
                    print("target_day= {}".format(target_day))
                    print("target_price= {} in {}".format(target_price, target_currency))
                    print("targer_c= {}".format(targer_c))
                else:
                    # EUR
                    print("target_currency= {}".format(target_currency)) #RUB
                    print("target_day= {}".format(target_day))          #DAY
                    print("target_price= {} in {}".format(target_price, target_currency))      #PRICE in RUB
                    print("targer_c= {}".format(targer_c))              #PRICE in EURO

                    curfile = "file_" + target_currency + ".csv"
                    curday = "DAY == '" + target_day +"'"
                    data = pd.read_csv(curfile)
                    df = pd.DataFrame(data)
                    newdf = df.query(curday)
                    print(newdf)
                    print(newdf['USD'].values[0])









        else:
            print("I do now know to do that, please restart script")
