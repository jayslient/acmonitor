from django.shortcuts import render
from h3c_ipudong3.models import Apinform
from django.http import HttpResponse
# Create your views here.

def ipudong3_select_all_inf(request):
    data = Apinform.objects.using('h3c_ipudong3').all()
    context = { 'data':data,}
    return render(request, 'ipudong3_select_all.html', context)

def ipudong3_update_inf(request):
    oid=request.GET['a']
    Apinform.objects.using('h3c_ipudong3').filter(ap_oid=oid).update(ap_warnsw='yes')
    return HttpResponse("ok")

def ipudong3_update_page(request):
    return render(request,'ipudong3_update_page.html')

def ipudong3_filter_inf(request):
    return render(request,'ipudong3_filter_page.html')

def ipudong3_filter_inf_display(request):
    filterstr=request.GET['sc']
    data=Apinform.objects.using('h3c_ipudong3').filter(ap_warnsw=filterstr)
    context = { 'data':data,}
    return render(request, 'ipudong3_select_all.html', context)

