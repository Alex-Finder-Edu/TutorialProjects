from django.shortcuts import HttpResponse
from backend_webapp.models import Person

# Create your views here.
def hello_wold(request):
    message: str = "Hello World from bakckend web app"
    return HttpResponse(message)

def view_models(request):
    message: str = ""
    models_count = Person.objects.count()
    if models_count == 0:
        message += "<p>No models have been found</p>"
    else:
        message += f"<p>{models_count} models have been found</p>"
        persons = Person.objects.all()
        for person in persons:
            message += f"<p>{person}</p>"
    return HttpResponse(message)
