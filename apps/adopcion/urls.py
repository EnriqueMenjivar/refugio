from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion

app_name="adopcion"

urlpatterns = [
    url(r'^index/$', index_adopcion)
]