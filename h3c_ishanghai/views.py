from django.shortcuts import render
from h3c_ishanghai.models import Apinform
from django.http import HttpResponse
# Create your views here.

def ishanghai_select_all_inf(request):
    data = Apinform.objects.using('h3c_ishanghai').all()
    context = { 'data':data,}
    return render(request, 'ishanghai_select_all.html', context)

def ishanghai_update_inf(request):
    oid=request.GET['a']
    Apinform.objects.using('h3c_ishanghai').filter(ap_oid=oid).update(ap_warnsw='yes')
    return HttpResponse("ok")

def ishanghai_update_page(request):
    return render(request,'ishanghai_update_page.html')

def ishanghai_filter_inf(request):
    return render(request,'ishanghai_filter_page.html')

def ishanghai_filter_inf_display(request):
    filterstr=request.GET['sc']
    data=Apinform.objects.using('h3c_ishanghai').filter(ap_warnsw=filterstr)
    context = { 'data':data,}
    return render(request, 'ishanghai_select_all.html', context)

