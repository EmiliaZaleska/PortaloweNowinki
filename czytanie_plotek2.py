import urllib.request
import datetime
from bs4 import BeautifulSoup


def czytaj_plotki(link):

    plotki = {}
    tagi = []

    try:
        with urllib.request.urlopen(link) as stream:
            html = stream.read()
            tekst = html.decode("utf-8-sig")
            #print(tekst)

            soup.find_all("div", class_="entry__header")

            #tagi.append(key)

            #return tagi

    except urllib.request.HTTPError as err:
        print("Błąd HTTP")

    except urllib.request.ContentTooShortError:
        print("Odpowiedź serwera za krótka")

    except Exception as err:
        with open("error.log", 'a') as fh:
            fh.write("{0}: {1}\n".format(datetime.datetime.now(), str(err)))

    finally:
        stream.close()



print(czytaj_plotki("https://www.pudelek.pl/"))
