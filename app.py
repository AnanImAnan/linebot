from flask import Flask, request, abort

import urllib.request, json
import requests
from bs4 import BeautifulSoup

import os
import sys
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

ACCESS_TOKEN= os.environ['ACCESS_TOKEN']
SECRET= os.environ['CHANNEL_SECRET']

# Channel Access Token
line_bot_api = LineBotApi(ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(SECRET)

pm_site = {}

@app.route("/")
def hello_world():
    return "hello world!"


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#     _message = TextSendMessage(text='Nice to meet you!')
#     _message = TextSendMessage(text=(event.source.user_id)) #reply userid
#     line_bot_api.reply_message(event.reply_token, _message)  
    # message = TextSendMessage(text=event)
#     print(event)

    msg = event.message.text
    _low_msg = msg.lower()
    
    _token = msg.strip().split(" ")
    _low_token = _token[0].lower()
    
    # query THU courses
    
    to = event.source.user_id
    if '開始' in _token[0]:
      x = 0
      line_bot_api.push_message(to, TextSendMessage(text="回過神來，你身在一個陌生的環境\n眼前有一位長的很像充氣娃娃的女性"))
      line_bot_api.push_message(to, TextSendMessage(text="女神：「你好，我是女神智慧娃娃」\n你：「我是哪？這裡是誰？」\n女神：「原來如此，失憶了啊。」\n(請輸入繼續)"))
      
    elif '繼續' in _token[0]:
        if x == 0:
          x = 1
          line_bot_api.push_message(to, TextSendMessage(text="好吧，我說明一下\n你是一位人見人愛的慣老闆\n某天\n由於你平常oo行經所累積的業障實在太多\n導致你在回家的路上\n經過海浪法師的經舍時\n聽到不小心漏音漏出來的佛經\n\n頓時\n\n剎那間\n\n須臾之間\n\n你\n\n被業力引爆\n了"))
          line_bot_api.push_message(to, TextSendMessage(text="你體內的大量高濃度業障\n在一瞬間向外爆發\n而爆炸中心——也就是你所在的區域瞬間來到了「零業障」狀態\n在這神聖且充滿靈性與悟性的空間裡產生了「聖結石」\n聖結石對業障有強大的吸引力\n瞬間將你所釋放的業障通通吸了回來\n但由於這股吸引力——也就是業力太過強大\n導致連你自己都被聖結石速到起飛\n\n而這一飛\n就飛到了異世界\n剛好這世界正受魔王——太陽王所侵襲\n而你要以勇者的身份打倒魔王\n拯救世界\n以償還你還在當老闆時的罪過"))
          line_bot_api.push_message(to, TextSendMessage(text="當然\n我會給你一些必要的協助\n只是你要告訴我你的基本資料\n(請輸入繼續)"))
        elif x == 1:
          x = 2
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的種族是什麼?」\n『『人類』』\n『『獸人』』\n『『精靈』』\n(請輸入想要的種族)"))
    #種族
    elif '人類' in _token[0]:
        if x == 2:
          a = 1
          x = 3
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的職業是什麼?」\n『『劍士』』\n『『武士』』\n『『騎士』』\n(請輸入想要的職業)"))
    elif '獸人' in _token[0]:
        if x == 2:
          a = 2
          x = 3
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的職業是什麼?」\n『『劍士』』\n『『武士』』\n『『騎士』』\n(請輸入想要的職業)"))
    elif '精靈' in _token[0]:
        if x == 2:
          a = 3
          x = 3
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的職業是什麼?」\n『『劍士』』\n『『武士』』\n『『騎士』』\n(請輸入想要的職業)"))
    #職業
    elif '劍士' in _token[0]:
        if x == 3:
          b = 1
          x = 4
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的性別是什麼?」\n『『男的』』\n『『女的』』\n『『請尊重多元』』"))
    elif '武士' in _token[0]:
        if x == 3:
          b = 2
          x = 4
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的性別是什麼?」\n『『男的』』\n『『女的』』\n『『請尊重多元』』"))
    elif '騎士' in _token[0]:
        if x == 3:
          b = 3
          x = 4
          line_bot_api.push_message(to, TextSendMessage(text="女神：「你的性別是什麼?」\n『『男的』』\n『『女的』』\n『『請尊重多元』』"))
    #性別
    elif '男的' in _token[0]:
        if x == 4:
          c = 1
          x = 5
          line_bot_api.push_message(to, TextSendMessage(text="女神：「最後，你的尊姓大名是?」\n(請輸入名字)"))
    elif '女的' in _token[0]:
        if x == 4:
          c = 2
          x = 5
          line_bot_api.push_message(to, TextSendMessage(text="女神：「最後，你的尊姓大名是?」\n(請輸入名字)"))
    elif '請尊重多元' in _token[0]:
        if x == 4:
          c = 3
          x = 5
          line_bot_api.push_message(to, TextSendMessage(text="女神：「最後，你的尊姓大名是?」\n(請輸入名字)"))

            
import os
if __name__ == "__main__":
    # load PM2.5 records
   # loadPMJson()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
