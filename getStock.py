import yfinance as yf

stock.info = {'address1': 'One Microsoft Way', 'city': 'Redmond', 'state': 'WA', 'zip': '98052-6399', 'country': 'United States', 
'phone': '425 882 8080', 'fax': '425 706 7329', 'website': 'https://www.microsoft.com', 'industry': 
'Software—Infrastructure', 'sector': 'Technology', 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. The company operates in three segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. The Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, Microsoft Viva, and Skype for Business; Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for organizations and enterprise divisions. The Intelligent Cloud segment licenses SQL, Windows Servers, Visual Studio, System Center, and related Client Access Licenses; GitHub that provides a collaboration platform and code hosting service for developers; Nuance provides healthcare and enterprise AI solutions; and Azure, a cloud platform. It also offers enterprise support, Microsoft consulting, and nuance professional services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification on Microsoft products. The More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; and Windows Internet of Things. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. The company sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. Microsoft Corporation was founded in 1975 and is headquartered in Redmond, Washington.', 
'fullTimeEmployees': 221000, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Satya  Nadella', 'age': 55, 'title': 'Chairman & CEO', 'yearBorn': 1967, 'fiscalYear': 2022, 'totalPay': 12676750, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Bradford L. Smith LCA', 'age': 63, 'title': 'Pres & Vice Chairman', 'yearBorn': 1959, 'fiscalYear': 2022, 'totalPay': 4655274, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Amy E. Hood', 'age': 50, 'title': 'Exec. VP & CFO', 'yearBorn': 1972, 'fiscalYear': 2022, 'totalPay': 4637915, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Judson  Althoff', 'age': 49, 'title': 'Exec. VP & Chief Commercial Officer', 'yearBorn': 1973, 'fiscalYear': 2022, 'totalPay': 4428268, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Christopher David Young', 'age': 50, 'title': 'Exec. VP of Bus. Devel., Strategy & Ventures', 'yearBorn': 1972, 'fiscalYear': 2022, 'totalPay': 4588876, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Alice L. Jolla', 'age': 55, 'title': 'Corp. VP & Chief Accounting Officer', 'yearBorn': 1967, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Brett  Iversen', 'title': 'Gen. Mang. of Investor Relations', 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Frank X. Shaw', 'title': 'Corp. VP for Corp. Communications', 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Christopher C. Capossela', 'age': 52, 'title': 'Exec. VP & Chief Marketing Officer', 'yearBorn': 1970, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Keith Ranger Dolliver Esq.', 'title': 'VP, Deputy Gen. Counsel of Corp., External & Legal Affairs and Assistant Sec.', 'exercisedValue': 0, 'unexercisedValue': 0}], 
'auditRisk': 5, 'boardRisk': 5, 'compensationRisk': 2, 'shareHolderRightsRisk': 2, 'overallRisk': 2, 'governanceEpochDate': 1680307200, 
'compensationAsOfEpochDate': 1672444800, 'maxAge': 86400, 'priceHint': 2, 'previousClose': 295.37, 'open': 295.97, 'dayLow': 295.27, 
'dayHigh': 303.25, 'regularMarketPreviousClose': 295.37, 'regularMarketOpen': 295.97, 'regularMarketDayLow': 295.27, 
'regularMarketDayHigh': 303.25, 'dividendRate': 2.72, 'dividendYield': 0.0092, 'exDividendDate': 1684281600, 
'payoutRatio': 0.28170002, 'fiveYearAvgDividendYield': 1.12, 'trailingPE': 32.849262, 'forwardPE': 27.786259, 'volume': 19987446, 
'regularMarketVolume': 19987446, 'averageVolume': 30885490, 'averageVolume10days': 28817040, 'averageDailyVolume10Day': 28817040, 
'bid': 302.91, 'ask': 302.93, 'bidSize': 2200, 'askSize': 900, 'marketCap': 2251988402176, 'fiftyTwoWeekLow': 213.43, 
'fiftyTwoWeekHigh': 303.25, 'fiftyDayAverage': 271.5324, 'twoHundredDayAverage': 255.5804, 'trailingAnnualDividendRate': 0.0, 
'trailingAnnualDividendYield': 0.0, 'currency': 'USD', 'enterpriseValue': 2202837450752, 'profitMargins': 0.0, 
'sharesOutstanding': 7435489792, 'sharesShort': 40038879, 'sharesShortPriorMonth': 35907039, 
'sharesShortPreviousMonthDate': 1678838400, 'dateShortInterest': 1681430400, 'sharesPercentSharesOut': 0.0054, 
'heldPercentInsiders': 0.00052, 'heldPercentInstitutions': 0.73767, 'shortRatio': 1.25, 'shortPercentOfFloat': 0.0054, 
'impliedSharesOutstanding': 0, 'bookValue': 22.313, 'priceToBook': 13.573711, 'lastFiscalYearEnd': 1656547200, 
'nextFiscalYearEnd': 1688083200, 'mostRecentQuarter': 1680220800, 'trailingEps': 9.22, 'forwardEps': 10.9, 'pegRatio': 2.54, 
'lastSplitFactor': '2:1', 'lastSplitDate': 1045526400, '52WeekChange': 0.019818425, 'SandP52WeekChange': -0.053996503, 
'lastDividendValue': 0.68, 'lastDividendDate': 1676419200, 'exchange': 'NMS', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 
'underlyingSymbol': 'MSFT', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 
'firstTradeDateEpochUtc': 511108200, 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EDT', 
'uuid': 'b004b3ec-de24-385e-b2c1-923f10d3fb62', 'messageBoardId': 'finmb_21835', 'gmtOffSetMilliseconds': -14400000, 
'currentPrice': 302.8702, 'targetHighPrice': 400.0, 'targetLowPrice': 232.0, 'targetMeanPrice': 321.27, 
'targetMedianPrice': 327.5, 'recommendationMean': 1.8, 'recommendationKey': 'buy', 'numberOfAnalystOpinions': 46, 
'revenuePerShare': 26.45, 'grossProfits': 135620000000, 'grossMargins': 0.0, 'ebitdaMargins': 0.0, 'operatingMargins': 0.0, 
'financialCurrency': 'USD', 'trailingPegRatio': 2.0698}

# REST API: https://query2.finance.yahoo.com/v10/finance/quoteSummary/MFST?modules=summaryProfile%2CfinancialData%2CquoteType%2CdefaultKeyStatistics%2CassetProfile%2CsummaryDetail&ssl=true

listStocks = ['AMZN','MSFT']
 
msft = yf.Ticker('MSFT')
data = msft.info

print(msft.info)

print(data['shortName'])
print(data['currency'])
print(data['open'])
print(data['bookValue'])

