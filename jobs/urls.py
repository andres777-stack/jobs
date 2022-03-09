from django.urls import path
from . import views

app_name = 'jobs'

#jobs/
urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('addjob/', views.add, name='add'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('ver/<int:id>', views.ver, name='ver'),
    path('addingjob/<int:id>', views.adding, name='adding'),
    
    #path('liked/<int:id>', views.liked, name='liked'),
]