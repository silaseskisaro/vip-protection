from django.shortcuts import render
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='signin')
def homepage(request):
    today = datetime.datetime.now().date()
    context = {
      'today': today,
    }
    return render(request, 'homepage.html', context)
