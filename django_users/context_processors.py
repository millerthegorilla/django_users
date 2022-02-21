from django.conf import settings # import the settings file

def base_html(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'BASE_HTML': settings.BASE_HTML}
