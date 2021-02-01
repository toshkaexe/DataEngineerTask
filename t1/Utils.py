# colum's name
TARGET_CURRENCY = "base"
DAY = "DAY"
CURRENCY_AUD = "AUD"
CURRENCY_BGN = "BGN"
CURRENCY_BRL = "BRL"
CURRENCY_CAD = "CAD"
CURRENCY_CHF = "CHF"
CURRENCY_CNY = "CNY"
CURRENCY_CZK = "CZK"
CURRENCY_DKK = "DKK"
CURRENCY_EUR = "EUR"
CURRENCY_GBP = "GBP"
CURRENCY_HDK = "HKD"
CURRENCY_HRK = "HRK"
CURRENCY_HUF = "HUF"
CURRENCY_IDR = "IDR"
CURRENCY_ILS = "ILS"
CURRENCY_INR = "INR"
CURRENCY_ISK = "ISK"
CURRENCY_JPY = "JPY"
CURRENCY_KRW = "KRW"
CURRENCY_MXN = "MXN"
CURRENCY_MYR = "MYR"
CURRENCY_NOK = "NOK"
CURRENCY_NZD = "NZD"
CURRENCY_PHP = "PHP"
CURRENCY_PLN = "PLN"
CURRENCY_RON = "RON"
CURRENCY_RUB = "RUB"
CURRENCY_SEK = "SEK"
CURRENCY_SGD = "SGD"
CURRENCY_THB = "THB"
CURRENCY_TRY = "TRY"
CURRENCY_USD = "USD"
CURRENCY_ZAR = "ZAR"


def dataParser(dataJson):
    item = []
    for i in range(0, len(dataJson["rates"])):
        item.append({
            "DAY": dataJson["rates"].index[i],
            TARGET_CURRENCY: dataJson["base"][0],
           # CURRENCY_EUR: dataJson["rates"][i][CURRENCY_EUR],
            CURRENCY_AUD: dataJson["rates"][i][CURRENCY_AUD],
            CURRENCY_BGN: dataJson["rates"][i][CURRENCY_BGN],
            CURRENCY_BRL: dataJson["rates"][i][CURRENCY_BRL],
            CURRENCY_CAD: dataJson["rates"][i][CURRENCY_CAD],
            CURRENCY_CHF: dataJson["rates"][i][CURRENCY_CHF],
            CURRENCY_CNY: dataJson["rates"][i][CURRENCY_CNY],
            CURRENCY_CZK: dataJson["rates"][i][CURRENCY_CZK],
            CURRENCY_DKK: dataJson["rates"][i][CURRENCY_DKK],
            CURRENCY_GBP: dataJson["rates"][i][CURRENCY_GBP],
            CURRENCY_HDK: dataJson["rates"][i][CURRENCY_HDK],
            CURRENCY_HRK: dataJson["rates"][i][CURRENCY_HRK],
            CURRENCY_HUF: dataJson["rates"][i][CURRENCY_HUF],
            CURRENCY_IDR: dataJson["rates"][i][CURRENCY_IDR],
            CURRENCY_ILS: dataJson["rates"][i][CURRENCY_ILS],
            CURRENCY_INR: dataJson["rates"][i][CURRENCY_INR],
            CURRENCY_ISK: dataJson["rates"][i][CURRENCY_ISK],
            CURRENCY_JPY: dataJson["rates"][i][CURRENCY_JPY],
            CURRENCY_KRW: dataJson["rates"][i][CURRENCY_KRW],
            CURRENCY_MXN: dataJson["rates"][i][CURRENCY_MXN],
            CURRENCY_MYR: dataJson["rates"][i][CURRENCY_MYR],
            CURRENCY_NOK: dataJson["rates"][i][CURRENCY_NOK],
            CURRENCY_NZD: dataJson["rates"][i][CURRENCY_NZD],
            CURRENCY_PHP: dataJson["rates"][i][CURRENCY_PHP],
            CURRENCY_PLN: dataJson["rates"][i][CURRENCY_PLN],
            CURRENCY_RON: dataJson["rates"][i][CURRENCY_RON],
            CURRENCY_RUB: dataJson["rates"][i][CURRENCY_RUB],
            CURRENCY_SEK: dataJson["rates"][i][CURRENCY_SEK],
            CURRENCY_SGD: dataJson["rates"][i][CURRENCY_SGD],
            CURRENCY_THB: dataJson["rates"][i][CURRENCY_THB],
            CURRENCY_TRY: dataJson["rates"][i][CURRENCY_TRY],
            CURRENCY_USD: dataJson["rates"][i][CURRENCY_USD],
            CURRENCY_ZAR: dataJson["rates"][i][CURRENCY_ZAR]
        })
    return item
