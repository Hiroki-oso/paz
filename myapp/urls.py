from django.urls import path
from .views import (
    TopView, IndexSecondView, IndexDetailView, 
    IndexDeleteView, IndexUpdateView, IndexListView, FirstInputView
)
app_name = 'myapp'
urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('detail/<int:pk>/', IndexDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', IndexDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', IndexUpdateView.as_view(), name='update'),
    path('list/', IndexListView.as_view(), name='list'),
    path('firstinput/', FirstInputView.as_view(), name='firstinput'),
]