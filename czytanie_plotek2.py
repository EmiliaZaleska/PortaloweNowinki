import urllib.request
import datetime
import csv
import bs4
from bs4 import BeautifulSoup



def czytaj_plotki(link):

    plik_csv = 'Tagi.csv'
    plotki = {}



    try:
        with urllib.request.urlopen(link) as stream:
            html = stream.read()
            tekst = html.decode("utf-8-sig")
            #print(tekst)

            soup = BeautifulSoup(tekst, 'html.parser')
            entryheaders = soup.find_all("div", class_="entry_header")
            dates = soup.find_all("span", class_="time")
            tags = soup.find_all("span", class_="inline-tags")

            for eh in entryheaders:
                for d in dates:
                    if d in eh:
                        for t in tags:
                            if t in eh:
                                plotki[t].append(d)

            print (plotki)

            #for d in dates:
             #   print (d.text)
            #for t in tags:
             #   print (t.text)

    except urllib.request.HTTPError as err:
        print("Błąd HTTP")

    except urllib.request.ContentTooShortError:
        print("Odpowiedź serwera za krótka")

    except Exception as err:
        with open("error.log", 'a') as fh:
            fh.write("{0}: {1}\n".format(datetime.datetime.now(), str(err)))

    finally:
        stream.close()

    with open(plik_csv, 'w') as csvFile:
        Writer = csv.writer(csvFile)

        columnTitleRow = "date, tag\n"
        Writer.writerow(columnTitleRow)

        for key in plotki:
            row = key + ',' + plotki[key]
            csvFile.write(row + '\n')





print(czytaj_plotki("https://www.pudelek.pl/"))
