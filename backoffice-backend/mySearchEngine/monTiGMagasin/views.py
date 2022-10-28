from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer

# Create your views here.
class InfoProductList(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
class InfoProductDetail(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)


class IncrementProductStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock = product.quantityInStock + number
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class DecrementProductStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock = product.quantityInStock - number
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class setSaleDiscount(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, newprice, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = True
        product.price_on_sale = newprice
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class removeSaleDiscount(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = False
        product.save()
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)


class autoSaleDiscount(APIView):
    def get(self, request, format=None):
        product = InfoProduct.objects.all()
        for element in product:
            if (element.quantityInStock >= 16 and element.quantityInStock <= 64):
                element.sale = True
                element.discount = element.price * 0.8
                element.save()
            if element.quantityInStock > 64 :
                element.sale = True
                element.discount = element.price * 0.5
                element.save()

        serializer = InfoProductSerializer(product,many=True)
        return Response(serializer.data)

class setPriceOnSell(APIView):
  def get_object(self, tig_id):
    try:
      return InfoProduct.objects.get(tig_id=tig_id)
    except InfoProduct.DoesNotExist:
      raise Http404

  def get(self, request, tig_id, newprice, format=None):
    product = self.get_object(tig_id=tig_id)
    if(product.sale):
      product.price_on_sale = newprice
      product.save()
      serializer = InfoProductSerializer(product)
      return Response(serializer.data)
    else:
      print("produit pas em promo")


class setDiscount(APIView):
  def get_object(self, tig_id):
    try:
      return InfoProduct.objects.get(tig_id=tig_id)
    except InfoProduct.DoesNotExist:
      raise Http404

  def get(self, request, tig_id, number, format=None):
    product = self.get_object(tig_id=tig_id)
    product.discount = number
    product.save()
    serializer = InfoProductSerializer(product)
    return Response(serializer.data)
