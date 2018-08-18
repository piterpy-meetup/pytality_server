import random

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from pytality_server.api.bl import hangle_submitted_code
from .models import Snippet

from .forms import SubmitCodeForm


def upload_file(request):
    if request.method == 'POST':
        form = SubmitCodeForm(request.POST, request.FILES)
        if form.is_valid():
            hangle_submitted_code(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = SubmitCodeForm()
    return render(request, 'upload.html', {'form': form})


def get_next_snippet(request):
    unused_snippets = Snippet.objects.all().filter(used_in_current_rotation=False)
    snippet = random.choice(unused_snippets)
    response = JsonResponse({
        'status': 'OK',
        'snippet_id': snippet.id,
        'code': snippet.incorrect_code,
        'time_to_solve': snippet.time_to_solve
    })
    return response


