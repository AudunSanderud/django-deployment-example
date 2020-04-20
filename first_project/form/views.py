from django.shortcuts import render
from form import forms

# Create your views here.

def form_name(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            ## THE DO_SOMETHING_CODE!
            print("VALIDATION SUCCESS")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request, 'form/form.html', {'form' : form})
