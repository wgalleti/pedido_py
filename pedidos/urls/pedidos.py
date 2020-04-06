from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pedidos.views import(PedidosListView, PedidosDetailView)

app_name = 'pedidos'
urlpatterns = {
    path('', PedidosListView.as_view()),
    path('/<int:pk>', PedidosDetailView.as_view()),
}
urlpatterns = format_suffix_patterns(urlpatterns)
