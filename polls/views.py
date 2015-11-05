from django.http import HttpResponse

def index(request):
    """TODO: Docstring for index.

    :request: TODO
    :returns: TODO

    """
    return HttpResponse("Hello, world. You're at the polls index.")
