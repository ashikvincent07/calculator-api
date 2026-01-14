from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name= "dispatch")
class AdditionView(View):

    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n1 = data.get("num1")
        n2 = data.get("num2")

        result = n1 + n2
        
        return JsonResponse({"Addition Result" : result})
    


@method_decorator(csrf_exempt, name= "dispatch")
class MultiplicationView(View):

    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n1 = data.get("num1")
        n2 = data.get("num2")

        result = n1 * n2
        
        return JsonResponse({"Multiplication Result" : result})
    


@method_decorator(csrf_exempt, name= "dispatch")
class SubtractionView(View):

    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n1 = data.get("num1")
        n2 = data.get("num2")

        result = n1 - n2
        
        return JsonResponse({"Subtraction Result" : result})
    

@method_decorator(csrf_exempt, name= "dispatch")
class DivisionView(View):

    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n1 = data.get("num1")
        n2 = data.get("num2")

        result = n1 / n2

        return JsonResponse({"Division Result" : result})
    

@method_decorator(csrf_exempt, name= "dispatch")
class CubeView(View):
    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n = data.get("num")

        result = n ** 3

        return JsonResponse({"Cube Result" : result})
    

@method_decorator(csrf_exempt, name= "dispatch")
class FactorialView(View):
    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n = data.get("num")

        fact = 1

        for i in range(1, n+1):
            fact *= i
        
        return JsonResponse({"Factorial" : fact})
    

@method_decorator(csrf_exempt, name= "dispatch")
class SquareView(View):
    def post(self, request, *args, **kwargs):

        data = loads(request.body)

        n = data.get("num")

        result = n ** 2

        return JsonResponse({"Square" : result})


    
