from django.urls import path, register_converter
from monTiGMagasin import views, converts

register_converter(converts.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('incrementStock/<int:tig_id>/<int:number>', views.IncrementProductStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:number>', views.DecrementProductStock.as_view()),
    path('putonsale/<int:tig_id>/<float:newprice>', views.setPriceOnSell.as_view()),
    path('removesale/<int:tig_id>', views.setSaleDiscount.as_view()),
    path('setDiscount/<int:tig_id>/<int:number>', views.setDiscount.as_view()),

]