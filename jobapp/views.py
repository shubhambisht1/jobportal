from django.shortcuts import render
from jobapp.models import delhijob
from jobapp import forms

# Create your views here.
def jobinfo(request):
    return render(request,'jobapp/home.html')
def delhijobinfo(request):
    delhijob_list=delhijob.objects.all()
    my_dict={'delhijob_list':delhijob_list}
    return render(request,'jobapp/delhijob.html',context=my_dict)
def signupinfo(request):
    form=forms.signupForm()
    if request.method=='POST':
        form=forms.signupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'jobapp/home.html')
    return render(request,'jobapp/signup.html',{'form':form})
def feedbackinfo(request):
    form=forms.feedbackForm()
    if request.method=='POST':
        form=forms.feedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'jobapp/home.html')
    return render(request,'jobapp/feedback.html',{'form':form})
