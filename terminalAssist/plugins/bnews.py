import requests
import colorama


def breaking_news():
    url = 'https://myallies-breaking-news-v1.p.rapidapi.com/GetTopNews'
    headers = {
        "X-RapidAPI-Host": "myallies-breaking-news-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "a71f30d0fbmsh2371d6a86a592bcp185555jsn1338ef98d457"
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED, 'Connection error, Please check your internet connection', colorama.Fore.RESET)
        return
    news = response.json()['Data']
    count = 1
    print('\n\n', colorama.Fore.RED, "Breaking News", colorama.Fore.RESET,
          '\n')
    for i in news:
        print(count, '---> ', i['MainTitle'], '\n\t', i['Duration'], '\n')
        count += 1
