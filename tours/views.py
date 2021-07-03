from django.shortcuts import render


# Create your views here.
def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html', {})


def tour_view(request, idtour):
    return render(request, 'tour.html')
