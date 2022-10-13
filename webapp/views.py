from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from webapp.forms import ContactForm


def indexer(request):
    form1 = ContactForm()
    if request.method == 'POST':
        # print(request.POST)
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            messages.success(request, 'Thank you for your time. We will reach you at the earliest')
            form1.save()
            redirect("/indexes/")
        else:
            print("Form is invalid")
    context = {'form1': form1}
    print("Context", context)

    return render(request, 'index.html', context)


def index(request):
    template = loader.get_template('index1.html')
    return HttpResponse(template.render())
