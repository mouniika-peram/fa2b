from django.shortcuts import render
# Create your views here.
from .models import Cart
from .serializer import CartSerializer
from rest_framework import viewsets
import product.models as prd_models
from rest_framework.response import Response
from rest_framework import status
from .functions import UpdateCartQty,GetAllCartItemsByUserId
from base.views import Record_Exist_Or_Not,Record_Exist_Or_Not_With_MultiParams
from rest_framework.decorators import action


class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace();
        cart_user_detail_dic={"user_id":1,"temp_id":""}

        prd_exist=prd_models.Product.objects.get(id=request.data['id'])
        if prd_exist:
            # import pdb;pdb.set_trace();
            cart_user_detail_dic={"prd_id":prd_exist.id,"user_id":1}
            cart_item_exist=Record_Exist_Or_Not_With_MultiParams(Cart,cart_user_detail_dic)
            # Cart.objects.get(prd_id=prd_exist.id,user_id=1)
            if cart_item_exist:
                udt_qty_dict={"cart":cart_item_exist,"prd_price":prd_exist.price,"type":"increment"}
                UpdateCartQty(udt_qty_dict)
                serializer=CartSerializer(cart_item_exist,context={"request":request})
                return Response(serializer.data,status=status.HTTP_201_CREATED)        
                # return GetAllCartItemsByUserId(request,cart_user_detail_dic) 
            else:
                dict_data={
                    "user_id":1,
                    "prd_id":prd_exist.id,
                    "prd_title":prd_exist.name,
                    "prd_img":prd_exist.image,
                    "prd_price":prd_exist.price,
                    "qty":1,
                    "net_amt":request.data['qty']*prd_exist.price
                }
                serializer = CartSerializer(data=dict_data)
                if serializer.is_valid():
                    serializer.save()
                    # return GetAllCartItemsByUserId(request,cart_user_detail_dic)
                    return Response(serializer.data,status=status.HTTP_201_CREATED)        
        else:
            return Response({"message":"Product does not found"},status=status.HTTP_404_NOT_FOUND)


    @action(detail=False,methods=["post"])
    def udt_cart_qty(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace();
        cart_item_exist=Record_Exist_Or_Not(Cart,id=request.data['id'])
        udt_qty_dict={"cart":cart_item_exist,"prd_price":request.data['prd_price'],"type":request.data['type']}
        UpdateCartQty(udt_qty_dict)
        return Response({"message":"Updated the qty"},status=status.HTTP_200_OK)
    




    





