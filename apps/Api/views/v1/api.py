from django.shortcuts import (render, redirect, reverse, HttpResponse)
from django import views

from apps.utils.response import (ErrorJsonResponse, SuccessJsonResponse)


class indexView(views.View):
    def get(self, request):
        return SuccessJsonResponse(data=None, msg='Server side works fine !')
