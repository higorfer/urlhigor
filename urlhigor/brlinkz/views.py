from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random, string, json
from .models import Urls
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings


def index(request):
    c = {}
    c.update(request)
    return render(request, 'brlinkz/index.html', c)


def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)  # get object, if not        found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(httpurl=url, short_id=short_id)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}),
                        content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id


class UserFormView(View):
    form_class = UserForm
    template_name = 'brlinkz/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #limpa dados antes de salvar
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:

                    login(request, user)
                    return render(request, 'brlinkz/index.html', {'username': username})

        #em caso de erro retorna para a mesma pagina
        return render(request, self.template_name, {'form': form})


class UserLogin(View):
    form_class = LoginForm
    template_name = 'brlinkz/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                    login(request, user)

            return redirect('/')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)

    return redirect('/')