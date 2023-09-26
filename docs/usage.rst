=====
Usage
=====

To use Django REST Framework Read & Write Serializers in a project, you just
need to import some of the generic classes and use them to build your own
endpoints the same way you do with Django REST Framework generic views,
viwsets and mixins. The only difference is that instead of defining only one
serializer class for the view, now you can define an output_serializer_class and
a input_serializer_class that be used according to the method you are
implementing.

Eg.:

.. code-block:: python

    from drf_io_serializers import generics
    from .models import MyModel
    from .serializers import MyModelOutputSerializer, MyModelInputSerializer


    class MyModelListCreateView(generics.ListCreateAPIView):
        queryset = MyModel.objects.all()
        output_serializer_class = MyModelOutputSerializer
        input_serializer_class = MyModelInputSerializer


If you need to dynamically override the serializers you can override the
following methods the same way you do with get_serializer_class and
get_serializer from Django REST Framework generic classes:

* get_output_serializer_class
* get_input_serializer_class
* get_output_serializer
* get_input_serializer


The drf_io_serializers classes implementation doesn't break any of the
features Django REST Framework implements, so you can use the same way you
use DRF classes, but with the read and write serializers extra feature.

Eg.:

.. code-block:: python

    from drf_io_serializers import generics
    from .models import MyModel
    from .serializers import MyModelInputSerializer


    class MyModelListCreateView(generics.ListCreateAPIView):
        queryset = MyModel.objects.all()
        # this still works the way it works with DRF ListCreateAPIView
        serializer_class = MyModelInputSerializer
