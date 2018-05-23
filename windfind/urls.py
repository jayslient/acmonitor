"""windfind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls',namespace='account',app_name='account')),
    url(r'^$', 'ruckus_ipudong1.views.home_page', name='home'),
    url(r'^ipudong1_select_all_inf/', 'ruckus_ipudong1.views.ipudong1_select_all_inf', name='ipudong1_select_all_inf'),
    url(r'^ipudong1_update_page/', 'ruckus_ipudong1.views.ipudong1_update_page', name='ipudong1_update_page'),
    url(r'^ipudong1_update_inf/', 'ruckus_ipudong1.views.ipudong1_update_inf', name='ipudong1_update_inf'),
    url(r'^ipudong1_filter_inf/', 'ruckus_ipudong1.views.ipudong1_filter_inf', name='ipudong1_filter_inf'),
    url(r'^ipudong1_filter_inf_display/', 'ruckus_ipudong1.views.ipudong1_filter_inf_display',name='ipudong1_filter_inf_display'),

    url(r'^ishanghai_select_all_inf/', 'h3c_ishanghai.views.ishanghai_select_all_inf', name='ishanghai_select_all_inf'),
    url(r'^ishanghai_update_page/', 'h3c_ishanghai.views.ishanghai_update_page', name='ishanghai_update_page'),
    url(r'^ishanghai_update_inf/', 'h3c_ishanghai.views.ishanghai_update_inf', name='ishanghai_update_inf'),
    url(r'^ishanghai_filter_inf/', 'h3c_ishanghai.views.ishanghai_filter_inf', name='ishanghai_filter_inf'),
    url(r'^ishanghai_filter_inf_display/', 'h3c_ishanghai.views.ishanghai_filter_inf_display',name='ishanghai_filter_inf_display'),

    url(r'^ipudong3_select_all_inf/', 'h3c_ipudong3.views.ipudong3_select_all_inf', name='ipudong3_select_all_inf'),
    url(r'^ipudong3_update_page/', 'h3c_ipudong3.views.ipudong3_update_page', name='ipudong3_update_page'),
    url(r'^ipudong3_update_inf/', 'h3c_ipudong3.views.ipudong3_update_inf', name='ipudong3_update_inf'),
    url(r'^ipudong3_filter_inf/', 'h3c_ipudong3.views.ipudong3_filter_inf', name='ipudong3_filter_inf'),
    url(r'^ipudong3_filter_inf_display/', 'h3c_ipudong3.views.ipudong3_filter_inf_display',name='ipudong3_filter_inf_display'),
]
