
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializer import CartSerializer

def UpdateCartQty(udt_qty_dict):
    if "type" in udt_qty_dict and udt_qty_dict['type']=="decrement":
        updatedqty=udt_qty_dict['cart'].qty-1
    else:
        updatedqty=udt_qty_dict['cart'].qty+1

    updated=Cart.objects.filter(id=udt_qty_dict['cart'].id).update(prd_price=udt_qty_dict['prd_price'],qty=updatedqty,net_amt=updatedqty*udt_qty_dict['prd_price'])
    return updated


def GetAllCartItemsByUserId(request,cart_user_detail_dic):
    cartItems=Cart.objects.all().order_by('-id')
    cartserializer = CartSerializer(cartItems,many=True, context={"request": request})
    return Response(cartserializer.data, status=status.HTTP_201_CREATED)

