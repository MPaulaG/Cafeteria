from .models import Social


#se crea un diccionario
def ctx_dict(request):
    ctx={}
    socialList=Social.objects.all()
#recorrer valores y agregar al diccionario
    for social in socialList: 
        ctx[social.key]=social.url
    return ctx