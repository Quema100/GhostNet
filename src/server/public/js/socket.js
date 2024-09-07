let socket;

window.onload = () => {
    let canvas = document.getElementById('screen');
    let ctx = canvas.getContext('2d');
    let imageWidth = 0; 
    let imageHeight = 0;

    socket = new WebSocket('ws://localhost:8765');


    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        const blob = new Blob([event.data], { type: 'image/jpeg' });
        const imgUrl = URL.createObjectURL(blob);
        const img = new Image();

        img.onload = () => {
            imageWidth = img.width;
            imageHeight = img.height;
            canvas.width = imageWidth;
            canvas.height = imageHeight;

            ctx.clearRect(0, 0, canvas.width, canvas.height); 
            ctx.drawImage(img, 0, 0);
        };

        img.src = imgUrl;
    };

    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
        } else {
            console.error('WebSocket connection died');
        }
    };

    socket.onerror = (error) => {
        console.error(`WebSocket error: ${error.message}`);
    };

    canvas.addEventListener('click', (event) => {
        const rect = canvas.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width * imageWidth;
        const y = (event.clientY - rect.top) / rect.height * imageHeight;
        const margin = 12; 
        if (x < margin || x > imageWidth - margin || y < margin || y > imageHeight - margin) {
            return; 
        }
        if (socket && socket.readyState === WebSocket.OPEN) {
            const message = JSON.stringify({ type: 'click', x: Math.round(x), y: Math.round(y) });
            socket.send(message);
        }
    });

    setInterval(()=>{
        if (socket && socket.readyState === WebSocket.OPEN) {
            const message = JSON.stringify({ type: 'update', key: 'update' });
            socket.send(message);
        }
    },1000)

    document.addEventListener('keydown', (event) => {
        if (socket && socket.readyState === WebSocket.OPEN) {
            const message = JSON.stringify({ type: 'keypress', key: event.key });
            socket.send(message);
        }
    });
};

window.onbeforeunload = () => {
    if (socket) {
        socket.close();
    }
};