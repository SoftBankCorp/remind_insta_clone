from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("call get")
        return render(request, "djangoProject/main.html")

    def post(self, request):
        print("call post")
        return render(request, "djangoProject/main.html")
