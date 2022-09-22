# SDK software development kit
# web app
# flask, django 兩個最大的架站軟件 flask 比較小，django 比較大



from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ZEq0oWtAUu1yWdqLCzBUX69S2dFzYpxbcqxSKPtPBWC/RQe54P5CxGssvHpKYFJ/Crr5qvW8w7nT9cWuIJS4ue6HRlbw5klz5K7HdO4di8c9/hivHpDsUKV1+AXpJcGiP3j3+Rev/1RAoM6H1EKvMAdB04t89/1O/w1cDnyilFU= ')
handler = WebhookHandler('1836560a361039c1f1ad7fc558981ab4')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()