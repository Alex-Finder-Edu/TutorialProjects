from django.shortcuts import HttpResponse
from backend_webapp.models import Person, Address

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
            addres_values = Address.objects.filter(person_id = person.id).values()
            addr_val = addres_values.first()
            address_string = f'{addr_val["city"]}, {addr_val["street_number"]} {addr_val["street_name"]}'
            message += f"<p>{person} - Living at: {address_string}</p>"
    return HttpResponse(message)
