from django.shortcuts import render
import json
# Create your views here.

file = open(r'C:\Users\antho\Desktop\weekday_m1\menu\templates\recipes.json','r')
json_data = file.read()

py_data = json.loads(json_data)

recipes = py_data['recipes']

def recipes_view(request):
    context = {
        'recipes' : recipes
    }
    return render(request,'index.html',context)

def one_recipe_view(request,id):
    context = {
        'recipe' : recipes[id-1]
    }
    return render(request,'recipe.html' ,context)
    