"""
Generic views, viewsets and mixins that extend the Django REST Framework ones adding
separated serializers for read and write operations.
"""

from __future__ import absolute_import, unicode_literals

__version__ = '1.0.6'

# pylint: disable=invalid-name
default_app_config = 'drf_io_serializers.apps.DrfIoSerializersConfig'
# pylint: enable=invalid-name
