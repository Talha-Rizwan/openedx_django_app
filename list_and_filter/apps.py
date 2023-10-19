"""
list_and_filter Django application initialization.
"""

from django.apps import AppConfig


class ListAndFilterConfig(AppConfig):
    """
    Configuration for the list_and_filter Django application.
    """

    name = 'list_and_filter'
    
    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "list_and_filter",
                "regex": r"^list",
                'relative_path': 'urls',
            },
            "cms.djangoapp": {
                "namespace": "list_and_filter",
                "regex": r"^list",
                'relative_path': 'urls',
            }
        },
}
