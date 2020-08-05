# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.orders import Orders
from .api.orders_orderID import OrdersOrderid
from .api.payment_orderID import PaymentOrderid
from .api.coffees import Coffees
from .api.coffees_type import CoffeesType


routes = [
    dict(resource=Orders, urls=['/orders'], endpoint='orders'),
    dict(resource=OrdersOrderid, urls=['/orders/<int:orderID>'], endpoint='orders_orderID'),
    dict(resource=PaymentOrderid, urls=['/payment/<int:orderID>'], endpoint='payment_orderID'),
    dict(resource=Coffees, urls=['/coffees'], endpoint='coffees'),
    dict(resource=CoffeesType, urls=['/coffees/<type>'], endpoint='coffees_type'),
]