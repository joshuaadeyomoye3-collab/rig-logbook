from django.shortcuts import render, get_object_or_404
from .models import ShiftLog

def dashboard(request):
    total_logs = ShiftLog.objects.count()
    total_incidents = ShiftLog.objects.exclude(incidents='').count()
    day_shifts = ShiftLog.objects.filter(shift_type='day').count()
    night_shifts = ShiftLog.objects.filter(shift_type='night').count()
    recent_logs = ShiftLog.objects.all().order_by('-shift_date')[:5]

    context = {
        'total_logs': total_logs,
        'total_incidents': total_incidents,
        'day_shifts': day_shifts,
        'night_shifts': night_shifts,
        'recent_logs': recent_logs,
    }
    return render(request, 'logbook/dashboard.html', context)

def log_list(request):
    logs = ShiftLog.objects.all().order_by('-shift_date')
    return render(request, 'logbook/log_list.html', {'logs': logs})

def log_detail(request, pk):
    log = get_object_or_404(ShiftLog, pk=pk)
    return render(request, 'logbook/log_detail.html', {'log': log})

def log_filtered(request):
    logs = ShiftLog.objects.exclude(incidents='').order_by('-shift_date')
    return render(request, 'logbook/log_list.html', {'logs': logs, 'filtered': True})