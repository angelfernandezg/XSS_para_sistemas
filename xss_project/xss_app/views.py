from django.shortcuts import render
from django.utils.html import escape
from .forms import CommentForm
from html_sanitizer import Sanitizer

sanitizer = Sanitizer()

def xss_vulnerable(request):
    if request.method == 'POST':
        user_input = request.POST.get('comment', '')
        return render(request, 'xss_result.html', {'result': user_input, 'sanitized': False, 'css_file': 'xss_app/vulnerable.css'})
    return render(request, 'xss_form.html', {'css_file': 'xss_app/vulnerable.css'})

def xss_protected(request):
    if request.method == 'POST':
        user_input = request.POST.get('comment', '')
        sanitized_input = escape(user_input)
        return render(request, 'xss_result.html', {'result': sanitized_input, 'sanitized': True, 'css_file': 'xss_app/protected.css'})
    return render(request, 'xss_form.html', {'css_file': 'xss_app/protected.css'})