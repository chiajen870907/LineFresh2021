from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django import views

from apps.utils.response import ErrorJsonResponse, SuccessJsonResponse
from apps.utils.flex import *
from application.settings import CHANNLE_SECRET, CHANNLE_TOKEN

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, BeaconEvent, TextSendMessage, FlexSendMessage

# Channel Access Token
line_bot_api = LineBotApi(CHANNLE_TOKEN)
# Channel Secret
handler = WebhookParser(CHANNLE_SECRET)


class callbackView(views.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(callbackView, self).dispatch(*args, **kwargs)

    def post(self, request):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = handler.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                print('MessageEvent')
                messageFlex = FlexSendMessage(alt_text='景點訊息', contents=flex_message_attractions(location='puppet',title='雲林布袋戲館',description='虎尾郡於大正九年（1920年）設置....',image='https://www.niusnews.com/upload/imgs/default/2020MAY__Chocooo/yunlin/520/1/IMG_6548.JPG'))
                messageText = TextSendMessage(text='現在所在的位置是 雲林布袋戲館\n 點擊下方"查看更多"則有機會獲得商圈優惠券哦!!')
                message = [messageText, messageFlex]
                line_bot_api.reply_message(event.reply_token, message)

            if isinstance(event, BeaconEvent):
                """
                    01525aa07a 布袋戲館
                """

                if event.beacon.hwid == '01525aa07a':
                    location = 'puppet'
                    title = '雲林布袋戲館'
                    description = '虎尾郡於大正九年（1920年）設置....'
                    image = 'https://www.niusnews.com/upload/imgs/default/2020MAY__Chocooo/yunlin/520/1/IMG_6548.JPG'

                messageFlex = FlexSendMessage(alt_text='景點訊息', contents=flex_message_attractions(location=location,title=title, description=description, image=image))
                messageText = TextSendMessage(text=f'現在所在的位置是 {title}\n 點擊下方"查看更多"則有機會獲得商圈優惠券哦!!')
                message = [messageText, messageFlex]
                line_bot_api.reply_message(event.reply_token, message)

        return HttpResponse()
