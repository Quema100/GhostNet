import asyncio
import websockets
from module import controller
from multiprocessing import Process

def websocket():
    try:
        server = websockets.serve(controller.handle_connection, "localhost", 8765)
        print("WebSocket server started on ws://localhost:8765")
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()

    except KeyboardInterrupt:
        print('exit')

def main():
    try:
        process = Process(target=websocket)
        process.start()
        process.join()
    except KeyboardInterrupt:
        print('Exit')

if __name__ == '__main__':
    main()


