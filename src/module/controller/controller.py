import websockets
import asyncio
import cv2
import numpy as np
import json
import pyautogui
from PIL import ImageGrab
import time
import threading

def process_command(command):
    if command['type'] == 'click':
        x, y = command['x'], command['y']
        pyautogui.click(x, y)
    elif command['type'] == 'keypress':
        pyautogui.press(command['key'])
    elif command['type'] == 'update':
        print('update')

async def handle_connection(websocket, path):
    while True:
        try:
            screenshot = ImageGrab.grab()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            _, buffer = cv2.imencode('.png', screenshot)
            png_data = buffer.tobytes()
            await websocket.send(png_data)  

            message = await websocket.recv()
            command = json.loads(message)
            threading.Thread(target=process_command, args=(command,)).start()

        except websockets.ConnectionClosed as e:
            print(f"Connection closed: {e}")
            break

        except Exception as e:
            print(f"Window Error: {str(e)}")
            break

        except KeyboardInterrupt:
            print("Connection closed")
            break

        except websockets.exceptions.ConnectionClosedOK:
            pass 

