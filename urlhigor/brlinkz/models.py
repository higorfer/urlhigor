from django.db import models


# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    fav = models.NullBooleanField(default=False)

    def __str__(self):
        return self.httpurl

    def begins_with_http(self):
        return self.httpurl[:4]
