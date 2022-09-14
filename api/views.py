from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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


