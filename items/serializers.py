# -*- coding: utf-8 -*-


from rest_framework.serializers import ModelSerializer

from items.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'name',
            'number',
        )

    def __init__(self, *args, **kwargs):
        super(ItemSerializer, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['number'].required = False
