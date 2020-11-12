from django.shortcuts import render
from django.http import HttpResponse
import random, string
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'asdas4t34gvsd'})


def password(request):

    length = 12

    # Set length if length request parameter is set and can be parsed to int type, else keep the default 12
    try:
        if request.GET.get('length'):
            length = int(request.GET.get('length'))
    except ValueError:
        pass

    # This variable holds the characters we gonna use in random() to generate the password
    password_characters = string.ascii_lowercase

    if request.GET.get('uppercase'):
        password_characters = string.ascii_letters

    if request.GET.get('numbers'):
        password_characters += string.digits

    if request.GET.get('special_chars'):
        password_characters += string.punctuation

    # To get random password without char repetition, use random.sample
    generated_password = ''.join(random.sample(password_characters, length))

    # To get random password with char repetition, use random.choice
    # generated_password = ''.join(random.choice(password_characters) for x in range(length))

    return render(request, 'generator/password.html', {'password': generated_password})
