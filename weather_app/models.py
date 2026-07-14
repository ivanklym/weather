from django.db import models

from django.db import models

class SearchHistory(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="Назва міста")
    searched_at = models.DateTimeField(auto_now_add=True, verbose_name="Час пошуку")
    found = models.BooleanField(verbose_name="Успішно знайдено")
    temp = models.FloatField(null=True, blank=True, verbose_name="Температура (°C)")

    class Meta:
        verbose_name = "Історія пошуку"
        verbose_name_plural = "Історія пошуків"
        ordering = ['-searched_at'] 

    def __str__(self):
        status = f"{self.temp}°C" if self.found else "Не знайдено"
        return f"{self.city_name} ({status}) — {self.searched_at.strftime('%d.%m.%Y %H:%M')}"