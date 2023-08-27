# # consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class MyConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         self.username = "Anonymous"
#         self.accept()
#         self.send(text_data="[Welcome %s!]" % self.username)
    
#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Process the message and send a response back
#         await self.send(text_data=json.dumps({'response': 'Received: ' + message}))

# myapp/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer

class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle received data
        await self.send(text_data="You said: " + text_data)
