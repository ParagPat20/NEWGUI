import asyncio
import websockets
import cv2
import numpy as np

# Set the IP address and port for the WebSocket server
server_host = "192.168.123.101"  # Change to your computer's IP address
server_port = 5588

async def handle_client(websocket, path):
    print(f"New client connected from {websocket.remote_address}")

    try:
        while True:
            # Receive binary data from the WebSocket client
            data = await websocket.recv()
            if not data:
                break

            # Convert the binary data to a NumPy array
            np_data = np.frombuffer(data, dtype=np.uint8)

            # Decode the JPEG image
            image = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

            # Display the image (you may want to customize this part based on your needs)
            cv2.imshow("ESP32-CAM Stream", image)
            cv2.waitKey(1)

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client {websocket.remote_address} disconnected.")

if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_client, server_host, server_port)

    print(f"WebSocket server started at ws://{server_host}:{server_port}")

    # Run the server indefinitely
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
