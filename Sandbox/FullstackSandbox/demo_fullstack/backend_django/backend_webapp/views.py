from django.shortcuts import HttpResponse

# Create your views here.
def hello_wold(request):
    message: str = "Hello World from bakckend web app"
    return HttpResponse(message)
