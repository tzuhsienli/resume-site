from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# from resume.views import hello
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# We should create our API now from here

#ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User
class GroupViewSet(viewsets.ModelViewSet):
    model = Group

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',GroupViewSet)

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'resume.views.home', name='home'),
#     # url(r'^resume/', include('resume.foo.urls')),
# 
#     # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# 
#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
#     
#     # Custom URL configuration should be added here
#     url(r'^hello/$', include('resume.views.hello'), name='hello'),    
#     url(r'^facet/login$',include('resume.facet.login'), name='login'),
    
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browseable API.
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
