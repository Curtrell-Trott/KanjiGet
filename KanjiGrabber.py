        from bs4 import BeautifulSoup
import requests
import textwrap3

#read text file w/ kanji and put each kanji in the URL 
input_file = open('input.txt', 'r', encoding = "utf-8")
input_list = (input_file.read().split())

output_file = open('output.txt', 'w', encoding = "utf-8")
output_text = ""

for c in input_list:
    #request the kanji page
    pg = requests.get('https://jisho.org/search/'+ c + '%23kanji') #url
    html = pg.text

    soup = BeautifulSoup(html, 'lxml')

    #kanji
    kanji = soup.find('h1', class_ = 'character').text

    #meaning
    meaning = soup.find('div', class_ = 'kanji-details__main-meanings').text

    #readings
    reading = soup.find('div', class_ = 'kanji-details__main-readings')

    if reading.find('dl', class_ = 'dictionary_entry kun_yomi') is not None:
        kun_read_list = reading.find('dl', class_ = 'dictionary_entry kun_yomi').find_all('a')
        kun_read = []
        for c in kun_read_list: kun_read.append(c.text)

    if reading.find('dl', class_ = 'dictionary_entry on_yomi') is not None:
        on_read_list = reading.find('dl', class_ = 'dictionary_entry on_yomi').find_all('a')
        on_read = []
        for c in on_read_list: on_read.append(c.text)

    #print into a text file
    output_text += (kanji + "\n" + "訓読み: " + ', '.join(kun_read) + "\n" + "音読み: " + ', '.join(on_read) + "" + textwrap3.dedent(meaning) + "\n")

    print(kanji + "\n")
    print(kun_read)
    print(on_read)

output_file.write(output_text)
output_file.close()

