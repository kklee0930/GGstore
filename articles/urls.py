from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("shop/", views.shop, name="shop"),
    path("cost/", views.cost, name="cost"),
    # path('', views.AllListView.as_view(), name='all_list'),
]
