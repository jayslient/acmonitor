from django.shortcuts import render
from ruckus_ipudong1.models import Apinform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required 
def home_page(request):
    return render(request,'home_page.html')

@login_required 
def ipudong1_select_all_inf(request):
    data = Apinform.objects.using('ruckus_ipudong1').all()
    context = { 'data':data,}
    return render(request, 'ipudong1_select_all.html', context)

@login_required 
def ipudong1_update_inf(request):
    oid=request.GET['a']
    Apinform.objects.using('ruckus_ipudong1').filter(ap_oid=oid).update(ap_warnsw='yes')
    return HttpResponse("ok")

@login_required 
def ipudong1_update_page(request):
    return render(request,'ipudong1_update_page.html')

@login_required 
def ipudong1_filter_inf(request):
    return render(request,'ipudong1_filter_page.html')

@login_required 
def ipudong1_filter_inf_display(request):
    filterstr=request.GET['sc']
    data=Apinform.objects.using('ruckus_ipudong1').filter(ap_warnsw=filterstr)
    context = { 'data':data,}
    return render(request, 'ipudong1_select_all.html', context)

