from weather.models import DayWeather

top_three_coldest_days = DayWeather.objects.order_by('-temperature')[:3]