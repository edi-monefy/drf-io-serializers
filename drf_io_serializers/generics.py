# -*- coding: utf-8 -*-

from rest_framework import generics, mixins

from .mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin


class GenericAPIView(generics.GenericAPIView):
    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert (
            self.serializer_class is not None or
            getattr(self, 'output_serializer_class', None) is not None
        ), (
            "'%s' should either include one of `serializer_class` and `output_serializer_class` "
            "attribute, or override one of the `get_serializer_class()`, "
            "`get_output_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.serializer_class

    def get_output_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for serializing output.
        """
        serializer_class = self.get_output_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_output_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.output_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        if getattr(self, 'output_serializer_class', None) is None:
            return self.get_serializer_class()

        return self.output_serializer_class

    def get_input_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating
        and deserializing input.
        """
        serializer_class = self.get_input_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_input_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.input_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins can send extra fields, others cannot)
        """
        if getattr(self, 'input_serializer_class', None) is None:
            return self.get_serializer_class()

        return self.input_serializer_class

    def get_list_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating
        and deserializing outputs for lists.
        """
        serializer_class = self.get_list_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_list_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.list_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins can send extra fields, others cannot)
        """
        if getattr(self, 'list_serializer_class', None) is None:
            return self.get_serializer_class()

        return self.list_serializer_class


class CreateAPIView(CreateModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(RetrieveModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListCreateAPIView(ListModelMixin,
                        CreateModelMixin,
                        GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveDestroyAPIView(RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateAPIView(RetrieveModelMixin,
                            UpdateModelMixin,
                            GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(RetrieveModelMixin,
                                   UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
