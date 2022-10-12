from django.shortcuts import render
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books, Reviews
from api.serializer import  ReviewModelSerializer, BookSerializer, UserModelSerializer

from django.contrib.auth.models import User

from rest_framework import authentication
from rest_framework import permissions

from rest_framework.decorators import action


# class ProductsView(APIView):
#
#     def get(self, request,*args, **kwargs):
#         return Response({"Msg": "You received the data"})
#
#
# class Greetings(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"Greeting": "Hello, Good morning"})
#
# class Add(APIView):
#     def get(self, request, *args, **kwargs):
#         num1 = int(input("Enter a number : "))
#         num2 = int(input("Enter the second number: "))
#         total = num1 + num2
#         return Response({"Output": total})
#
# class AddView(APIView):
#     def post(self, request, *args, **kwargs):
#         val1 = request.data.get("num1")
#         val2 = request.data.get("num2")
#         total_val = int(val1) + int(val2)
#         return Response({"Final Output": total_val})
#

class Findcube(APIView):
    def post(self, request, *args, **kwargs):
        cube = int(request.data.get("num"))
        cube_val = cube ** 3
        return Response({"Cube value is: ": cube_val})

class Numcheck(APIView):
    def post(self, request, *args, **kwargs):
        num = int(request.data.get("num"))
        res = "Even" if num % 2 == 0 else "Odd"
        # if num % 2 == 0:

        #     odd = "Even number"
        # else:
        #     odd = "Odd number"
        return Response({"Output is: ": res})

class Numfactorial(APIView):

    def post(self, request, *args, **kwargs):

        fact = int(request.data.get("num"))

        get_fact = 1
        for i in range(1, fact + 1):
            get_fact = get_fact * i
        return Response({"Output is:": get_fact})

class Wordcount(APIView):
    def post(self, request, *args, **kwargs):

        get_word = request.data.get("text")
        words = get_word.split(" ")
        wc = {}
        for w in words:
            if w in wc:
                wc[w] += 1
            else:
                wc[w]=1
        return Response(data=wc)

class Palindrome(APIView):
    def post(self, request, *args, **kwargs):

        num = request.data.get("num")

        new_num = ""
        for i in num:
            new_num += i
        rev_num = new_num[::-1]

        if rev_num == num:
            res="Palindrome"
        else:
            res="Not a palaindrome"

        return Response(data=res)

class Armstrong(APIView):
    def post(self, request, *args, **kwargs):
        num = int(request.data.get("num"))

        new_num = 0
        temp = num
        while temp > 0:
            rem = temp % 10
            new_num += rem ** 3
            temp //= 10

        if num == new_num:
           is_armstrong = 'Armstrong number'
        else:
           is_armstrong = 'Not an Armstrong number'
        return Response(data=is_armstrong)


class Primenumber(APIView):
    def post(self, request, *args, **kwargs):
        num1 = int(request.data.get("num"))

        is_prime = False
        for i in range(2, num1):
            if num1 % i == 0:
                is_prime = True
                break
        if is_prime:
            is_prime_number = num1, "is not a Prime Number"
        else:
            is_prime_number = num1, "is a Prime Number"

        return Response(data=is_prime_number)





class Products(APIView):



    def get(self, request, *args, **kwargs):
        get_data = Books.objects.all()
        serializer = BookSerializer(get_data, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        # book_name = request.data.get("name")
        # book_author = request.data.get("author")
        # book_price = request.data.get("price")
        # book_publisher = request.data.get("publisher")
        # book_quantity = request.data.get("quantity")
        # Books.objects.create(Name=book_name, Author=book_author, Price=book_price, Publisher=book_publisher, Qty=book_quantity)
        # return Response(data="A new book created")

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        book = Books.objects.get(id=id)
        serializer = BookSerializer(book, many=False)
        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data = f"The Book {id} is deleted")

    def put(self, request, *args, **kwargs):

        id = kwargs.get("id")
        serialization = BookSerializer(data=request.data)

        if serialization.is_valid():
            Books.objects.filter(id=id).update(**serialization.validated_data)
            return Response(data=serialization.data)
        else:
            return Response(data=serialization.errors)





# Modelserializer Views


class ReviewView(APIView):

    def post(self, request, *args, **kwargs):

        serializer = ReviewModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def get(self, request, *args, **kwargs):

        get_review = Reviews.objects.all()
        serializer = ReviewModelSerializer(get_review, many=True)
        return Response(data=serializer.data)

class ReviewDetails(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        get_id = Reviews.objects.get(id=id)
        serializaton = ReviewModelSerializer(get_id, many=False)
        return Response(data=serializaton.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data=f"The id: {id} is deleted")

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        get_id = Reviews.objects.get(id=id)
        serializer = ReviewModelSerializer(instance=get_id, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)





#Using ViewSet to write views instead of APIView

from rest_framework.viewsets import ViewSet, ModelViewSet

class ProductsViewSetView(ViewSet):

    # authentication_classes = [authentication.BasicAuthentication]
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        get_details = Books.objects.all()
        serializer = BookSerializer(get_details, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.error)

    def retrieve(self, request, *args, **kwargs):

        id = kwargs.get("pk")
        books = Books.objects.get(id=id)
        serializer = BookSerializer(books, many=False)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):

        id = kwargs.get("pk")
        get_book = Books.objects.get(id=id)
        serializer = BookSerializer(instance=get_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):

        id = kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data= f"The id {id} is deleted")

    @action(methods=["POST"], detail=True)
    def add_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        user = request.user
        book = Books.objects.get(id=id)
        Reviews.objects.create(book=book,
                               user=user,
                               comment=request.data.get("comment"),
                               rating=request.data.get("rating"))
        return Response(data="Review created succesfully")


    @action(methods=["GET"], detail=True)
    def get_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        rev = Books.objects.get(id=id)
        get_rev = rev.reviews_set.all()
        serializer = ReviewModelSerializer(get_rev, many=True)
        return Response(data=serializer.data)






class ProductModelViewSet(ModelViewSet):

    serializer_class = BookSerializer
    queryset = Books.objects.all()

    # @action(methods=["POST"], detail=True)
    # def get_review(self, request, *args, **kwargs):
    #     return Response(data="Review sucesfully created")


class ReviewsModelViewSet(ModelViewSet):

    serializer_class = ReviewModelSerializer
    queryset = Reviews.objects.all()

    def list(self, request, *args, **kwargs):
        all_reviews = Reviews.objects.all()

        if 'user' in request.query_params:
            all_reviews = all_reviews.filter(user=request.query_params.get("user"))
        serializer = ReviewModelSerializer(all_reviews, many=True)
        return Response(data=serializer.data)





# Password Authentication


class UserSerializer(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()



