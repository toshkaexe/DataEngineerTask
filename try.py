import requests
import pprint


if __name__ == '__main__':
    countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
    countries = countries_api_res.json()[1]
    print(countries)

    print(len(countries))
    pprint.pprint(countries[0])