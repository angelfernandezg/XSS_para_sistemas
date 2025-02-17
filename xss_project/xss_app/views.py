from django.shortcuts import render
from django.utils.html import escape
from .forms import CommentForm
from html_sanitizer import Sanitizer

sanitizer = Sanitizer()

def xss_vulnerable(request):
    if request.method == 'POST':
        user_input = request.POST.get('comment', '')
        return render(request, 'C:/Users/angel/XSS_para_sistemas/xss_project/xss_app/templates/xss_result.html', {'result': user_input, 'sanitized': False})
    return render(request, 'xss_form.html')

def xss_protected(request):
    if request.method == 'POST':
        user_input = request.POST.get('comment', '')
        sanitized_input = sanitizer.sanitize(user_input)
        return render(request, 'xss_result.html', {'result': sanitized_input, 'sanitized': True})
    return render(request, 'xss_form.html')