# drf-chat 
Simple async and sync messaging app for Django Rest Framework

Features:
+ Facebook-style chat API
+ Websocket-based chat
+ Words blacklist
+ Files attachments
+ Firebase Messaging notifycations


### Installation

```
pip install drf-chat
```

```python
# REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'EXCEPTION_HANDLER': 'drf_chat.exceptions.api_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}
```
  * ASGI and Channels
```python
# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
ASGI_APPLICATION = "drf_chat.routing.application"
```
  * Add drf_chat to your installed apps
 ```python
INSTALLED_APPS = [
	...
    'channels',
    'rest_framework',
    'rest_framework.authtoken',

	...
	
    'drf_chat'
]
```
