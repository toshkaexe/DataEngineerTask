https://docs.google.com/document/d/1WYA3V-eDgdtoiJDzAcQ-4k-q0zW0crBve5MKYq1y1Ls/edit
Background: This is a practice within the recruiting process for the data engineer. It takes place between the first and the second interview and has to be prepared by the applicant before the second interview (the technical interview).

Goal:
get insights on how a problem is solved
see the working style of an applicant
see how the candidate present the results

Preamble: There is no right or false. It’s not given, that you have to show a fancy presentation - you can also do it on a command line. Every human is different - someone is better in presenting/explaining, understanding users, problem-solving, programming or writes beautiful code. We want to understand how the applicant work and behave. So please do it your way and within your personal style!

E1 - Use external Exchange Rate API and load exchange rates into a database

Goal:
please show how you downloaded the data (any observations, pitfalls?)
show and explain the data model you created
show that you can convert multiple source (target) prices from a query result (eg. SQL “data example” below), into each base price

Background - Use case:
you have a dashboard with currency-related numbers.
you have different users for that dashboard: All local dealers (eg. Russia, Europe, US), but also the boss of that dealers
All use the same dashboards, but want to see their own numbers (the numbers are in the original values and (target) currency stored) in RUB, EUR, USD etc.
Their Bosses wants to see over ALL locations the numbers in EUR or USD
ToDo: sketch out a (data) solution, that would solve this problem (do NOT build the dashboard, do not build another API, instead build the load into a (data) storage to get all the raw data for calculation, sketch out the problem and show a solution (e.g. with SQL) how you calculate on the fly into the two base currencies EUR or USD from some dummy data (eg. data example SELECT below) from RUB, GBP whatever)

HowTo:
at exchangeratesapi.io you find an exchange API for currency rates on a daily bases
load all available exchanges for the current year into a database
ensure that you can easily convert multiple source (target) prices into at least 2 base currencies: USD or EUR, example target data as postgreSQL that needs to be calculated (Hint: Goal are two SQLs that do a translation in each execution for each base[EUR|USD]):


SELECT CAST('2020-01-01' AS DATE) AS date_date, CAST('EUR' AS CHAR(3)) AS target_currency, CAST('11.11' AS NUMERIC(14,4)) AS a_price UNION
SELECT CAST('2020-02-01' AS DATE) AS date_date, CAST('GBP' AS CHAR(3)) AS target_currency, CAST('12.12' AS NUMERIC(14,4)) AS a_price UNION
SELECT CAST('2020-03-01' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency, CAST('333.33' AS NUMERIC(14,4)) AS a_price;

E2 - crawling, data extraction of a static website
A user asks about how he can obtain data of a website without spending days to extract the data by hand
Look at https://www.urparts.com/index.cfm/page/catalogue and check for a manufacturer, then look into the categories, then the models and the result set where the part (number) before ‘ - ‘ and the part category
crawl the overall at this point in time existing catalogue and create a CSV file with the following data (example with 10 lines):

manufacturer,category,model,part,part_category
Ammann,Roller Parts,ASC100,ND011710,LEFT COVER
Ammann,Roller Parts,ASC100,ND011758,VIBRATOR
Ammann,Roller Parts,ASC100,ND011785,RIGHT COVER
Ammann,Roller Parts,ASC100,ND017673,ECCENTRIC
Ammann,Roller Parts,ASC100,ND017675,ECCENTRIC
Ammann,Roller Parts,ASC100,ND018184,HUB
Ammann,Roller Parts,ASC100,ND018193,BRACKET
Ammann,Roller Parts,ASC100,ND018214,LEFT SHAFT
Ammann,Roller Parts,ASC100,ND018216,RIGHT SHAFT


E3 - write a unit test
Write at least one simple unit test for E1 or E2 with any framework you want!

Hint: You also need this to be better prepared and understand the pairing session during the technical interview
