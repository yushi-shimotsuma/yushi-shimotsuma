from django_filters import filters
from django_filters import FilterSet
from app.models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class ItemFilter(FilterSet):


    name = filters.CharFilter(label='name', lookup_expr='contains')
    no = filters.NumberFilter(label='no', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('no', 'no'),
        ),
        field_labels={
            'name': 'name',
            'no': 'no',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ['name', 'no']
