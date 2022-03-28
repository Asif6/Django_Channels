from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer

class MySyncConsumer(SyncConsumer):
    

    def websocket_connect(self,event):
       self.send({
           'type':'websocket.accept'
       })

    print("Connect Success ... ")

    def websocket_receive(self,event):
        print("Massage Recive ", event)

    def websocket_disconnect(self,event):
        print("Data disconnect ",event)


class MyAcyncConsumer(AsyncConsumer):


    async def wevsocket_connect(self,event):
        pass

    async def websocket_receive(self,event):
        pass
    async def websocket_disconnect(self,event):
        pass
