# import websocket libraries
import asyncio
import websockets

# websocket handler


async def websocketsHandler(websocket, path):
    async for msg in websocket:
        print(msg)

# websockets server
start_server = websockets.serve(websocketsHandler, "0.0.0.0", 8443)
print("Websockets Server is active at localhost:8443")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
