from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"

class UnitOfMeasure(models.Model):
    name = models.CharField(max_length = 50)
    suffix = models.CharField(max_length = 5)
    floating = models.BooleanField()
    precision = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.suffix})"

class Measurable(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    unitOfMeasure = models.ForeignKey(UnitOfMeasure,  on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} (categoría: {self.category}, unidad: {self.unitOfMeasure})"

class Entry(models.Model):
    measurable = models.ForeignKey(Measurable,  on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    value = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    #value_float = models.FloatField(null=True)

    def __str__(self):
        return f"{self.measurable}: {self.value} el {self.datetime}"

class Expected(models.Model):
    measurable = models.ForeignKey(Measurable,  on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False)
    value = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    #value_float = models.FloatField(null=True)

    def __str__(self):
        return f"{self.measurable}: {self.value} el {self.datetime}"

