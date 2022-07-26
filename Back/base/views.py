from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from .models import AllBooks, Loans
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#from .serializers import NoteSerializer
#from base.models import Note


def index(request):
    return JsonResponse({"test":"alive"}, safe=False)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
 
        return token
# signin/login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# signup/register
@api_view(['POST'])
def register(request):
    User.objects.create_user(username = request.data["username"], password = request.data["password"], email = request.data["email"])
    return JsonResponse({"register":"success"})

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def book_loan(request):
    book_tmp = AllBooks.objects.get(_id=request.data["b_id"])
    Loans.objects.create(book = book_tmp ,user = request.user)
    return JsonResponse({"Loan": "success"})

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_all_books(request):
    res = []
    for book in AllBooks.objects.all():
        res.append({
            "title":book.title,
            "desc":book.desc,
            "image":str(book.image),
            "id": book._id,
            "genre":book.genre,
            "author":book.author
        })
    return JsonResponse(res, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_books(request):
    res = []
    print(request.user)
    for loan in request.user.loans_set.all():
        res.append({
            "title":loan.book.title,
            "desc":loan.book.desc,
            "image":str(loan.book.image),
            "id": loan.book._id,
            "genre":loan.book.genre,
            "author":loan.book.author,
            "createdTime":loan.book.createdTime,
        })
    return JsonResponse(res, safe=False)