from django.conf.urls import include, url
from .views import ngothabotView

urlpatterns = [
	url(r'^80009763e9a243ea64cff6ecfc84b9a73a3481b1986497dd68/?$', ngothabotView.as_view())
]