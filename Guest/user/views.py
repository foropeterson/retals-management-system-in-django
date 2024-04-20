import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Room , House
from django.template import loader


def profile(request):
    email = request.session['member_id']  # Corrected variable name
    user = User.objects.filter(email=email)
    template = loader.get_template('user/index.html')
    context = {
        'user': user,
    }
    return render(request, 'user/profile.html', context)
def post(request):
    # Your logic here
    return render(request, 'user/post.html')
