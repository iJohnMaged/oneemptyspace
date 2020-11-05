from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def index(request):
     with open(BASE_DIR / 'hello_world/templates/traits.csv', newline='') as f:
          reader = csv.reader(f)
          t = list(reader)


     flat_list = []
     for sublist in t:
          for item in sublist:
               flat_list.append(item)

     return render(request, 'home.html', {
          'traits': flat_list,
     })


