from django.shortcuts import render
import stepic_tours.data as data


# Create your views here.
def main_view(request):

    return render(request, 'index.html')


def departure_view(request, departure):
    tours = dict()
    min_nights = 0
    max_nights = 0
    min_price = 0
    max_price = 0
    for key, inf in data.tours.items():
        if inf['departure'] == departure:
            tours[key] = inf
            if (inf['price'] < min_price) or min_price == 0:
                min_price = inf['price']
            if inf['price'] > max_price:
                max_price = inf['price']
            if inf['nights'] < min_nights or min_nights == 0:
                min_nights = inf['nights']
            if inf['nights'] > max_nights:
                max_nights = inf['nights']
    return render(request, 'departure.html', {'tours': tours,
                                              'count': len(tours),
                                              'min_nights': min_nights,
                                              'max_nights': max_nights,
                                              'min_price': min_price,
                                              'max_price': max_price,
                                              })


def tour_view(request, idtour=None):
    selected_tour = data.tours[idtour].copy()
    selected_tour['departure'] = data.departures[data.tours[idtour]['departure']]  # get and replace departure
    selected_tour['stars'] = '★' * int(data.tours[idtour]['stars'])  # get str with stars
    return render(request, 'tour.html', selected_tour)
