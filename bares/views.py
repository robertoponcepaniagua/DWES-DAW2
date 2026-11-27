from django.http import HttpResponse, HttpResponseNotFound
from django.utils.html import escape


BARES = [
    {"id": 1, "nombre": "Casa Felipe", "barrio": "La Viña"},
    {"id": 2, "nombre": "El Faro", "barrio": "El Pópulo"},
    {"id": 3, "nombre": "Bar Cañailla", "barrio": "La Viña"},
]


def portada(request):
    return HttpResponse(
        "<h1>De tapeo por Cádiz</h1>"
        "<p>Guía de bares del casco antiguo. En obras.</p>"
    )


def listado(request):
    return HttpResponse("Aquí irá el listado de bares.")


def inspector(request):
    return HttpResponse(
        f"method: {request.method}\n"
        f"path:   {request.path}\n"
        f"GET:    {dict(request.GET)}\n"
        f"navegador: {request.headers.get('User-Agent', 'desconocido')}\n"
        f"IP: {request.META.get('REMOTE_ADDR', 'desconocida')}\n"
        f"Host: {request.headers.get('Host', 'desconocido')}\n",
        content_type="text/plain; charset=utf-8",
    )


def buscar(request):
    valores = request.GET.getlist("q")
    termino = valores[0].strip().casefold() if valores else ""

    if termino == "":
        return HttpResponse(
            "Escribe un término de búsqueda: /bares/buscar/?q=camarones"
        )

    aviso = ""
    if len(valores) > 1:
        aviso = "<p>El parámetro q llegó repetido; solo se atiende al primero.</p>"

    return HttpResponse(
        f"{aviso}<p>Buscando «{escape(termino)}»...</p>"
    )

# def buscar(request):
#     termino = request.GET.get("q", "").strip()
#     if termino == "":
#         return HttpResponse(
#             "Escribe un término de búsqueda: /bares/buscar/?q=camarones"
#         )
#     return HttpResponse(f"Buscando «{escape(termino)}»...")


def detalle(request, pk):
    for bar in BARES:
        if bar["id"] == pk:
            return HttpResponse(
                f"<h1>{escape(bar['nombre'])}</h1>"
                f"<p>Barrio: {escape(bar['barrio'])}</p>"
            )

    return HttpResponseNotFound("No hay ningún bar con ese identificador.")


def plato(request, pk):
    return HttpResponse(f"El plato estrella del bar {pk}")
