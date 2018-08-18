from django.http import HttpResponseRedirect
from django.shortcuts import render

from pytality_server.api.bl import hangle_submitted_code
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
    pass
