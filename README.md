
Exchange Rate API
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
