from django.urls import path
from .views import WeatherIndexView, WeatherResultView, HistoryListView

urlpatterns = [
    path('', WeatherIndexView.as_view(), name='index'),
    path('weather/', WeatherResultView.as_view(), name='weather_result'),
    path('history/', HistoryListView.as_view(), name='history'),
]