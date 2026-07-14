from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from .forms import CitySearchForm
from .services import get_weather
from .models import SearchHistory

class WeatherIndexView(View):
    def get(self, request):
        form = CitySearchForm()
        recent_history = SearchHistory.objects.all()[:5]
        return render(request, 'weather/index.html', {
            'form': form,
            'recent_history': recent_history
        })

class WeatherResultView(View):
    def get(self, request):
        city = request.GET.get('city_name', '').strip()
        if not city:
            return redirect('index')

        weather_data = get_weather(city)
        SearchHistory.objects.create(
            city_name=city,
            found=weather_data['success'],
            temp=weather_data.get('temp') if weather_data['success'] else None
        )

        return render(request, 'weather/result.html', {
            'weather': weather_data,
            'city': city
        })

class HistoryListView(View):
    def get(self, request):
        history = SearchHistory.objects.all()
        return render(request, 'weather/history.html', {'history': history})
