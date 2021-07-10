import stepic_tours.data as data
def statistics(request):
    return {
        'title_': data.title,
        'subtitle_': data.subtitle,
        'description_': data.description,
    }