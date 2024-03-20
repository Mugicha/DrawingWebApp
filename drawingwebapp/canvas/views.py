from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # 'canvas/index.html' テンプレートをレンダリングする
    return render(request, 'canvas/index.html')
