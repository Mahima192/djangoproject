from django.shortcuts import render

# Create your views here.
def book_list(request):
    return render(request,"book_register/demo.html")
def book_form(request):
    return render(request,"book_register/book_form.html")
def book_delete(request):
    return