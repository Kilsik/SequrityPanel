from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in current_visits:
        non_closed_visit = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit)
                }
        non_closed_visits.append(non_closed_visit)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
