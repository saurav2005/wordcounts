
from django.urls import path
from . import view

urlpatterns = [
    path('', view.home, name='homepage'),
    path('count/', view.counts, name='counts')
 ]
#this count name is what is shown after slash for new page
#and name should have same kewword used in action