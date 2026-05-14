from django.shortcuts import render, get_object_or_404
from .models import ShiftLog

def log_list(request):
    logs = ShiftLog.objects.all().order_by('-shift_date')
    return render(request, 'logbook/log_list.html', {'logs': logs})

def log_detail(request, pk):
    log = get_object_or_404(ShiftLog, pk=pk)
    return render(request, 'logbook/log_detail.html', {'log': log})

def log_filtered(request):
    logs = ShiftLog.objects.exclude(incidents='').order_by('-shift_date')
    return render(request, 'logbook/log_list.html', {'logs': logs, 'filtered': True})