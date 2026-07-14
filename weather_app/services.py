import requests
from decouple import config

def get_weather(city):
    API_KEY=config('API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=uk'
    try:
        response = requests.get(url,timeout=10)
        data = response.json()
        if response.status_code == 200:
            return {
                'success': True,
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'country': data['sys']['country']
            }
        elif response.status_code == 404:
            return {'success': False, 'error': 'Місто не знайдено. Перевірте правильність написання.'}
        else:
            return {'success': False, 'error': f'Помилка API (Код: {response.status_code})'}
            
    except requests.exceptions.RequestException:
        return {'success': False, 'error': 'Сервер погоди тимчасово недоступний.'}