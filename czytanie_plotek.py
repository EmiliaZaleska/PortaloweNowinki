import urllib.request
import datetime


def czytaj_plotki(link):

    plotki = {}
    tagi = []

    try:
        with urllib.request.urlopen(link) as stream:
            html = stream.read()
            tekst = html.decode("utf-8-sig")
            #print(tekst)

            slowa = tekst.split()
            for slowo in slowa:
                if slowo in plotki:
                    plotki[slowo] += 1
                else:
                    plotki[slowo] = 1

            for key in plotki:
                if "www.pudelek.pl/tag/" in key:
                    key = key.replace('"https://www.pudelek.pl/tag/', '')
                    key = key.replace('<a href=', '')
                    key = key.replace('href=', '')
                    key = key.replace('/">', '')
                    key = key.replace('+', ' ')

                    tagi.append(key)

            return tagi

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
