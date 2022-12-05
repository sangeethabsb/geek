from django.db import models

class Country(models.Model):
    name = models.CharField(max_length = 20)
    capital = models.CharField(max_length = 20, unique=True)
    ISDCode = models.IntegerField(unique=True)
    Timezone = models.TextField(max_length = 10)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    capital = models.CharField(max_length=20)
    districts = models.IntegerField(null = True)
    
    def __str__(self):
        return self.name
