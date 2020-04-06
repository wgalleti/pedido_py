from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pedidos.views import(ItensPedidosListView, ItensPedidosDetailView)

app_name = 'pedidos'
urlpatterns = {
    path('', ItensPedidosListView.as_view()),
    path('/<int:pk>', ItensPedidosDetailView.as_view()),
}
urlpatterns = format_suffix_patterns(urlpatterns)
