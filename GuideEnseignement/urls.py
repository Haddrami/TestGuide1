from . import  views
from django.urls import include, path
from django.contrib.auth.decorators import login_required
app_name='GuideEnseignement'
urlpatterns = [
    path('', views.myindex , name='myindex'),
]

"""urlpatterns = [
    path('', views.index,name='index'),
    path('$login', views.login,name='login'),
]"""