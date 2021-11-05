from django.apps import AppConfig


class DRFChatConfig(AppConfig):
    name = "drf_chat"
    verbose_name = "Messages"

    def ready(self):
        from . import signals
