"""
list_and_filter Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)

from openedx.core.djangoapps.plugins.constants import ProjectType


class ListAndFilterConfig(AppConfig):
    """
    Configuration for the list_and_filter Django application.
    """

    name = 'list_and_filter'
    
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
               PluginURLs.NAMESPACE: 'list_and_filter',
                PluginURLs.REGEX: r'^api/list_and_filter/',
                PluginURLs.RELATIVE_PATH: 'urls',
            },
        },
    }
