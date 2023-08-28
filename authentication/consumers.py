# <your_app>/consumers.py
from channels.consumer import SyncConsumer
import json

class SomeConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("WebSocket Connected..",event)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print("Message Rececived.",event)
    
    def websocket_disconnect(self,event):
        print("Websocket Disconnected.",event)
    