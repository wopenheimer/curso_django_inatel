from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_return = {
        'course_name': 'IEIE',
        'alunos_list': [
            {'name': 'Wellington'},
            {'name':'José'},
            {'name':'Pedro'},
            {'name':'João'},
        ],
    }

    return render(request, 'heloo.html', context_return)
