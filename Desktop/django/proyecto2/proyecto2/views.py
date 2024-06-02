from django.http import HttpResponse
import datetime
from django.template import Template, Context
#from django.template import loader
#from django.template.loader import get_template
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
def saludo(request):
    return HttpResponse("Hola. Soy Jaime Ramírez A.")   #first view

def despedida(request):
    #nombre = "Jaime"
    #apellido = "Ramírez"
    p1 = Persona("Jaime","Ramírez")
    ahora = datetime.datetime.now()
    temas_curso = ["plantillas","modelos","formularios","vistas","despliegues"]
    #temas_curso = []
    doc_externo = open("C:/Users/Administrator/desktop/django/proyecto2/proyecto2/templates/template1.html")
    templa = Template(doc_externo.read())
    doc_externo.close()
    #context = Context({'nombre_persona': nombre, 'apellido_persona': apellido, "momento_actual": ahora})

    #doc_externo = loader.get_template('template1.html')
    #doc_externo = get_template('template1.html')
    context = Context({'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido, "momento_actual": ahora,'temas':temas_curso})
    #documento = doc_externo.render({'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido, "momento_actual": ahora,'temas':temas_curso})
    documento = templa.render(context)
    return HttpResponse(documento)

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    '''
    <html>
    <body>
    <h1>
    %s
    </h1>
    </body>
    </html
    '''
    return HttpResponse(fecha_actual)