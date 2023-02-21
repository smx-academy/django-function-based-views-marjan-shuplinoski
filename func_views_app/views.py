from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET", "POST"])
def ime_get_post(request):
    if(request.method=='GET'):
        ime = request.GET.get('ime','')
    elif(request.method=='POST'):
        ime = request.data.get('ime','')
    data = {"Ime": ime,
            "Dolzina": len(ime),
            "Golemi Bukvi": ime.upper(),
            "Mali Golemi": ime.swapcase()
            }
    return Response(data)


@api_view(['POST'])
def plostina_perimetar(request):
    stranaA = int(request.data.get('stranaA', 0))
    stranaB = int(request.data.get('stranaB', 0))
    rezultat = request.data.get('rezultat', 0)
    if (rezultat == 'perimetar'):
        result = 2 * (stranaA + stranaB)
    elif (rezultat == 'plostina'):
        result = stranaA * stranaB
    else:
        rezultat = "Ne postoi takov parametar za presmetka"
        result = 0
    data = {"Strana A": stranaA,
            "Strana B": stranaB,
            rezultat: result,
            }
    return Response(data)


@api_view(['GET'])
def paren_neparen(request):
    broj = int(request.GET.get('broj', 0))
    if (broj % 2 == 0):
        rezultat = True
    else:
        rezultat = False
    return Response({"Paren": rezultat})
