from django.shortcuts import render
import stepic_tours.data as data


# Create your views here.
def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    tours = dict()
    for key, inf in data.tours.items():
        if inf['departure'] == departure:
            tours[key] = inf
    print(tours)
    return render(request, 'departure.html', {'tours': tours})


def tour_view(request, idtour=None):
    selected_tour = data.tours[idtour].copy()
    selected_tour['departure'] = data.departures[data.tours[idtour]['departure']]  # get and replace departure
    selected_tour['stars'] = '★' * int(data.tours[idtour]['stars'])  # get str with stars
    return render(request, 'tour.html', selected_tour)
