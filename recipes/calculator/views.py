from django.core.paginator import Paginator

from django.http import HttpResponse

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'dumplings': {
        'мука, г': 500,
        'яйцо, шт': 1,
        'вода, мл': 250,
        'соль, ч.л.': 0.5,
        'перец черный молотый, г': 0.2,
        'говяжий фарш, г': 300,
        'свиной фарш, г': 300,
        'репчатый лук, шт': 2,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipes_item(request, recipe_name):

    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = request.GET.get('servings', None)

        if servings:

            result = dict()

            for ingredients, quantity in data.items():
                all_ingredients = quantity * int(servings)
                result[ingredients] = all_ingredients
            context = {
                'recipe_name': recipe_name,
                'recipe': result
            }

        else:
            context = {
                'recipe_name': recipe_name,
                'recipe': data
            }

    else:
        context = None

    return render(request,'calculator/index.html', context)
