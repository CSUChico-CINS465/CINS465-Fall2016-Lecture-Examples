from django.db import models

# Create your models here.

class Charger(models.Model):
    chargetype = models.CharField(max_length=30)
    chargeRate = models.FloatField()

    def __str__(self):              # __unicode__ on Python 2
	return self.chargetype

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
    chargers = models.ManyToManyField(Charger)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name) + ": " + str(self.latitude) + ", " + str(self.longitude) + ", " + str(self.charger)

class Distance(models.Model):
    start = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='start')
    end = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='end')
    distance = models.FloatField()
    time = models.FloatField()

    def __str__(self):              # __unicode__ on Python 2
	return str(self.start) + " " + str(self.end) + " " + str(self.distance)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)
