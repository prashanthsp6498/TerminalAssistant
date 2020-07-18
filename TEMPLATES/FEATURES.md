# Features : 

### Assist Features : 

Here, are the list of features of ASSIST Package in the given below Snippet :
```
$ assist --features

Hey kushtej!

These are the list of all the features provided by Assist : 

--bitcoin-price         Check current bitcoin price
--currency              Check current currency exchange of more than 16 countries
--quotes                Programming Quotes to motivate you during Coding
--cat-fact              Cat facts for your cat :)
--check-speed           Check Internet Speed
--dictionary            Check the meaning of the word.
--forcast               The Current Weather Forcast in your city
--joke                  Funny jokes to clear your mind!
```

## 1. assist `--currency`

The `--forcast` module API gives the currency exchange of more than 16 countries with different country bases.

**Sample :**
```
$ assist --currency

Hey kushtej!                    

BASE : EUR

CAD : 1.55      HKD : 8.82      ISK : 159.40    PHP : 56.30     DKK : 7.44
HUF : 355.48    CZK : 26.64     AUD : 1.63      RON : 4.84      SEK : 10.39
IDR : 16436.88  INR : 85.77     BRL : 6.09      RUB : 80.84     HRK : 7.53
JPY : 122.17    THB : 35.92     CHF : 1.07      SGD : 1.58      PLN : 4.48
BGN : 1.96      TRY : 7.81      CNY : 7.98      NOK : 10.71     NZD : 1.74
ZAR : 19.07     USD : 1.14      MXN : 25.74     ILS : 3.91      GBP : 0.91
KRW : 1371.98   MYR : 4.86

To set Default Currency BASE : assist [--currency] [--setbase]

```
### To set base currency :

```
$ assist --currency --setbase

Hey kushtej!

CAD HKD ISK PHP DKK HUF CZK AUD RON SEK IDR INR BRL RUB HRK JPY THB CHF SGD PLN BGN TRY CNY 
NOK NZD ZAR USD MXN ILS GBP KRW MYR

Choose one of the above : USD

BASE : USD

CAD : 1.36      HKD : 7.75      ISK : 140.13    PHP : 49.50     DKK : 6.54
HUF : 312.51    CZK : 23.42     GBP : 0.80      RON : 4.26      SEK : 9.13
IDR : 14450.00  INR : 75.40     BRL : 5.36      RUB : 71.07     HRK : 6.62
JPY : 107.40    THB : 31.58     CHF : 0.94      EUR : 0.88      MYR : 4.27
BGN : 1.72      TRY : 6.87      CNY : 7.02      NOK : 9.42      NZD : 1.53
ZAR : 16.77     MXN : 22.63     SGD : 1.39      AUD : 1.44      ILS : 3.44
KRW : 1206.14   PLN : 3.94

To set Default Currency BASE : assist [--currency] [--setbase]
```


## 1. assist `--forcast`

The `--forcast` module API gives the current maximum and minimum temparature of your city as well as the prediction of the weather.

**Sample :**
```
$ assist --forcast

Hey kushtej!

Heavy Rain
MINIMUM TEMPARATURE : 26.29
MAXIMUM TEMPARATURE : 34.015
```
## 2. assist `--check-speed`

The `--check-speed` module API gives your current upload and download internet speed to you in moments with all your ISP Details.

**Sample :**
```
$ assist --check-speed

Hey kushtej!

Retrieving speedtest.net configuration...
Testing from Airtel (96.71.147.606)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Bharti Airtel Ltd (Delhi) [127.67 km]: 18.345 ms
Testing download speed................................................................................
Download: 100.00 Mbit/s
Testing upload speed......................................................................................................
Upload: 100.71 Mbit/s
```


## 3. assist `--bitcoin-price`

The `--bitcoin-price` module API pedicts the current price of the bitcoin in USD,EURO and POUND.

**Sample :**
```
$ assist --bitcoin-price

Hey kushtej!

TODAY'S BITCOIN RATE :

United States Dollar - 9,276.0262 Dollars
Euro - 8,202.7900 Euro
British Pound Sterling - 7,422.1010 Pound
```
## 4. assist `--quotes`

The `--quotes` module API gives Programming Quotes to motivate you during Coding 

**Sample :**
```
$ assist --quotes

Hey kushtej!

Just because you've implemented something doesn't mean you understand it.
- Brian Cantwell Smith
```
## 5. assist `--cat-fact`

The `--cat-fact` module API gives cat facts to you.

**Sample :**
```
$ assist --cat-fact

Hey kushtej!

Did you Know...
Thank to an extremely efficient pair of kidneys, cats can hydrate themselves by drinking salt water.
```

## 6. assist `--joke`

The `--joke` module API gives all types of jokes like dark,homour and programmer jokes to you to pass the time.

**Sample :**
```
$ assist --joke

Hey kushtej!
 ------JOKE------
Why did the Python programmer not respond to the foreign mails he got?
Because his interpreter was busy collecting garbage.😂😂
```
