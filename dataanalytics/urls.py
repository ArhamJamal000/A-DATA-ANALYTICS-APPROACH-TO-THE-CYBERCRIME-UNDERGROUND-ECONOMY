"""dataanalytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user import views as user_views
from fileadmin import views as fileadmin_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$', user_views.index, name="index"),
    url('user/register/$',user_views.register,name="register"),
    url('user/feedback/$',user_views.feedback,name='feedback'),
    url('user/uploadfile/$',user_views.uploadfile,name='uploadfile'),
    url('user/mydetails/$',user_views.mydetails,name='mydetails'),
    url('user/updatedetails/$',user_views.updatedetails,name='updatedetails'),
    url('user/viewdocument/$',user_views.viewdocument,name='viewdocument'),
    url('user/download/$',user_views.download,name='download'),
    url('user/logout/$',user_views.logout,name='logout'),
    url('user/request/(?P<pk>\d+)/$',user_views.request, name="request"),


    url('fileadmin/login/$',fileadmin_views.login,name="login"),
    url('fileadmin/viewpage/$',fileadmin_views.viewpage,name="viewpage"),
    url('fileadmin/viewuploadfile/$',fileadmin_views.viewuploadfile,name="viewuploadfile"),
    url('fileadmin/accept/(?P<pk>\d+)/$',fileadmin_views.accept, name="accept"),
    url('fileadmin/reject/(?P<pk>\d+)/$',fileadmin_views.reject, name="reject"),
    url('admin/deleteobj/(?P<pk>\d+)/$',fileadmin_views.deleteobj, name="deleteobj"),
    url('fileadmin/viewuserrequest/$', fileadmin_views.viewuserrequest, name="viewuserrequest"),
    url('fileadmin/accepts/(?P<pk>\d+)/$',fileadmin_views.accepts, name="accepts"),
    url('fileadmin/rejects/(?P<pk>\d+)/$',fileadmin_views.rejects, name="rejects"),  
    url('admin/deleteobjs/(?P<pk>\d+)/$',fileadmin_views.deleteobjs, name="deleteobjs"),
    url('fileadmin/viewchat/(?P<pk>\d+)/$',fileadmin_views.viewchat,name="viewchat"),
    url('fileadmin/viewfeedbackpage/$',fileadmin_views.viewfeedbackpage,name="viewfeedbackpage"),
    url('admin/chartpage/(?P<chart_type>\w+)/$',fileadmin_views.chartpage,name="chartpage"),
    url('admin/logout/$',fileadmin_views.logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
