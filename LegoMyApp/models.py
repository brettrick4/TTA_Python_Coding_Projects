from django.db import models

# Create your models here.
LEGO_CATEGORIES = (('Star Wars','Star Wars'), ('Space','Space'), ('Castle','Castle'), ('Pirate','Pirate'), ('City','City'),
                   ('Marvel Heroes','Marvel Heroes'), ('DC Heroes','DC Heroes'), ('Harry Potter','Harry Potter'),('Other','Other'))


class LegoSet(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    category = models.CharField(max_length=20, blank=True, null=False, choices=LEGO_CATEGORIES)
    # ImageField allows me to upload an image
    image = models.ImageField(height_field=None, blank=True, null=False, width_field=None, upload_to='LegoMyApp/')

    LegoSets = models.Manager()

    def __str__(self):
        return self.name

class MiniFig(models.Model):
    character = models.CharField(max_length=30, null=False, blank=False)
    # ImageField allows me to upload an image
    image = models.ImageField(height_field=None, blank=True, null=False, width_field=None, upload_to='LegoMyApp/')

    MiniFigs = models.Manager()

    def __str__(self):
        return self.character



