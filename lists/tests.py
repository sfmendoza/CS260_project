from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home.main_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.session = {}
        response = home.main_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)


class LoginPageTest(TestCase):

    def test_login_page_returns_correct_html(self):
        request = HttpRequest()
        response = home.login(request)
        expected_html = render_to_string('login.html')
        self.assertEqual(response.content.decode(), expected_html)