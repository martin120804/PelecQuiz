from django.shortcuts import render
from .forms import EventRegistrationForm

def register_event(request):

    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'events/success.html')

    else:
        form = EventRegistrationForm()

    return render(request, 'events/register.html', {'form': form})