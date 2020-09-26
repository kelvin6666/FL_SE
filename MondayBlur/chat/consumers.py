# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer): #JS function transmit message over websocket to ChatConsumer
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name'] #consumer information,which is url route,keyword argument,room_name
        self.room_group_name = 'chat_%s' % self.room_name #constructs channels group name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept() #Accept websocket connection

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data) # Conversion of text_data from json to python 
        message = text_data_json['message'] # message will be in python dictionary

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({ # Conversion of text_data from python to json string when sending message
            'message': message
        }))