# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({ # Inspect the type of connection.
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack( # if ws connection then connection given
        URLRouter( # Examine the HTTP path based on urlpatterns
            chat.routing.websocket_urlpatterns 
        )
    ),
})