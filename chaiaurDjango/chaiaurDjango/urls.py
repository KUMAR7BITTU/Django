"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" urls.py file is a routing file which tells you where you can go."""

from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('chai/',include('chai.urls')),

    path("__reload__/",include("django_browser_reload.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

""" urls ko batana padega ki konsa view kisme jaayga."""
"""Here we do routing of all the files. routing means in which url you will go and what will happen after going to that url will be discussed in seperate file. That file is views.py and it defines all the views. views means controller where all functionality and bussiness logic is written ."""


""" admin route is bydefault given to us ."""


"""we have to also create one model file where we will keep all the database models."""

"""first we hit this urls.py file and then it govern which route will handle it and then the entire control of the files will go the views.we write bussiness logic in views and you can return from there any html5 or just hello world. Apart from that how things are structured in Database and how all that will work will be written in models.py file ."""





