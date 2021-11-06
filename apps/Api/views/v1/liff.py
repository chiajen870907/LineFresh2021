from django.shortcuts import (render, redirect, reverse, HttpResponse)
from django import views

from apps.utils.response import (ErrorJsonResponse, SuccessJsonResponse)


class indexView(views.View):
    def get(self, request):
        return render(request, 'liff/index.html')


class redirectView(views.View):
    def get(self, request):
        if request.GET.get('liff.state'):
            return render(request, 'liff/redirect.html')
        redirectUrl = request.GET.get('redirect')
        if redirectUrl:
            # 景點轉址
            if redirectUrl == 'attractions':
                location = request.GET.get('location')
                return render(request,f'liff/attractions/{location}.html')
            # 其他轉址
            return render(request,f'liff/{redirectUrl}.html')
        # 電腦版轉址
        return render(request, 'liff/index.html')


