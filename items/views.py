# -*- coding: utf-8 -*-


from rest_framework import viewsets

from items.models import Item
from items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer