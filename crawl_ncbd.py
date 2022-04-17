import requests
from bs4 import BeautifulSoup
import telepot
import dateparser
import time

TELEGRAM_TOKEN = '5118273643:AAG_O_GshxoRpuV-qBU-85YySyb473iXxo4'

def send_mess(mess):
    bot = telepot.Bot(TELEGRAM_TOKEN)
    bot.sendMessage(-640764629, mess)

news = "Hội nghị Hợp tác Phát triển Thương mại Biên giới Việt Nam - Lào lần thứ XII:  xác định 7 định hướng hợp tác phát triển thương mại biên giới Việt Nam - Lào"

while(True):
    cont = 0
    a = requests.get("https://nghiencuubiendong.vn/tin-cap-nhat.954.snews")
    soup = BeautifulSoup(a.text, 'html.parser')
    new_feeds = soup.select('a[style*="font-size"]')
    times = soup.select('div[style*="italic"]')
    for idx, x in enumerate(new_feeds):
        _title = x.get_text()
        time_new = dateparser.parse(times[idx].get_text())
        if(news != _title):
            send_mess("Have new news at: " + str(time_new))
            send_mess("Main content: " +_title)
            send_mess("---------------------------------------------")
            cont +=1
            time.sleep(0.5)
        if(news == _title):
            break
    if(cont==0):
        send_mess("Don't have any new news")

    news = new_feeds[0].get_text()
    time.sleep(600)

