from js import document
from pyodide.ffi import create_proxy  # type: ignore

from ws import WS

websocket = WS("ws", "127.0.0.1", "7005")  # Set's up the WebSocket connection.


def button(args=None):
    websocket.send("Hello Server!")  # Send a message to the server.
    print(websocket.msg())  # Get the latest servers response.
    print(websocket.msgDict())  # Get all latest dicts from servers responses.

    websocket.onMsg("Pong", lambda: print(websocket.msg()))  # Log the latest servers response after receiving an message starting with Pong
    websocket.send("Ping")  # Send a message to the server.


def main():
    document.getElementById("body").innerHTML = f'<button id="button" type="submit">A button</button>'
    document.getElementById("button").addEventListener("click", create_proxy(button))


if __name__ == "__main__":
    main()
