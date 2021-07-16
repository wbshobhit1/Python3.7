

def news_speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    news_speak("Good Morning!! Today's news is as follows:")
    import json
    import requests
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=8b783c64a6d8410c9d0ccebb4040f8d0"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    i=0
    for articles in arts:
        i += 1
        print(i,".",articles['title'])
        news_speak(articles['title'])
        if i < 10:
            news_speak("Moving on !!!")
            continue
        else:
            news_speak("This is the end of today's news")
            break

    news_speak("Thanks and have a nice day!!!")