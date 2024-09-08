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

    if command['type'] == 'mousemove':
        x, y = command['x'], command['y']
        pyautogui.moveTo(x, y) 
    elif command['type'] == 'click':
        x, y = command['x'], command['y']
        pyautogui.click(x, y)
    elif command['type'] == 'keypress':
        key = command['key']
        if len(key) > 1:
            if key[0] == 'alt' and key[1] == 'Alt':
                pyautogui.press('hangul')
            elif key[0] == 'ctrl' and key[1] == 'control':
                pyautogui.press('ctrl')
            elif key[0] == 'shift' and key[1] == 'Shift':
                pyautogui.press('shift')
            elif key[0] == 'shift' and key[1] == 'Tab':
                pyautogui.hotkey('win','tab')
            else:
                pyautogui.hotkey(*key)
        else:
            if key[0] == 'ArrowUp':
                pyautogui.press('up')
            elif key[0] == 'ArrowDown':
                pyautogui.press('down')
            elif key[0] == 'ArrowLeft':
                pyautogui.press('left')
            elif key[0] == 'ArrowRight':
                pyautogui.press('right')
            elif key[0] == 'F1':
                pyautogui.press('f1')
            elif key[0] == 'F2':
                pyautogui.press('f3')
            elif key[0] == 'F3':
                pyautogui.press('f3')
            elif key[0] == 'F4':
                pyautogui.press('f4')
            elif key[0] == 'F5':
                pyautogui.press('f5')
            elif key[0] == 'F6':
                pyautogui.press('f6')
            elif key[0] == 'F7':
                pyautogui.press('f7')
            elif key[0] == 'F8':
                pyautogui.press('f8')
            elif key[0] == 'F9':
                pyautogui.press('f9')
            elif key[0] == 'F10':
                pyautogui.press('f10')
            elif key[0] == 'F11':
                pyautogui.press('f11')    
            elif key[0] == 'F12':
                pyautogui.press('f12')
            elif key[0] == 'Escape': 
                pyautogui.press('esc')
            elif key[0] == 'Enter':
                pyautogui.press('enter')
            elif key[0] == 'Meta':
                pyautogui.press('win')
            else:   
                pyautogui.press(key)

    elif command['type'] == 'update':
        pass

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

