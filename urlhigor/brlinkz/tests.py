from django.utils import timezone
from django.test import TestCase

from .models import Urls


class UrlModelTests(TestCase):

    def create_url(self, httpurl, pub_date, count, fav):
        return Urls.objects.create(httpurl=httpurl, pub_date=pub_date, count=count, fav=fav)

    def test_begins_with_http(self):
        """begins_with_http() returns False for Urls not starting with http://"""
        url = self.create_url(httpurl="https://testhigordjango.com", pub_date=timezone.now(), count=0, fav=False)
        testedurl = Urls.begins_with_http(url)
        self.assertEqual(testedurl, "http")