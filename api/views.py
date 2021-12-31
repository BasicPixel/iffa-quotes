from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from . import serializers
from .models import Quote

import random

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({
        "":"Return available API routes",
        "/list":"Return all non-pending quotes",
        "/pending":"Return all pending quotes",
        "/[id]":"Return a single quote with the specified id",
        "/random":"Return a random quote from the database",
        "/add-quote":"Add a quote to the database (only accepts POST and requires admin)",
        "/delete/[id]":"Delete a quote from the database (requires admin)",
    })

@api_view(['GET'])
def quote_list(request):
    quotes = Quote.objects.filter(pending=False)
    serializer = serializers.QuoteSerializer(quotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pending_quotes(request):
    quotes = Quote.objects.filter(pending=True)
    serializer = serializers.QuoteSerializer(quotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_quote(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except Quote.DoesNotExist:
        return Response({f"Quote with the id {id} does not exist"})
    serializer = serializers.QuoteSerializer(quote)
    return Response(serializer.data)

@api_view(['GET'])
def random_quote(request):
    quote_list = list(Quote.objects.filter(pending=False))
    quote = random.choice(quote_list)
    serializer = serializers.QuoteSerializer(quote)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((AllowAny,))
def add_quote(request):
    # return Response(request.data)
    if request.user.is_superuser:
        request.data["pending"] = False

    serializer = serializers.QuoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_quote(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except:
        return Response({f"Quote with the id {id} does not exist"})

    quote.delete()
    return Response("Quote successfully deleted.")