import ws
from js import document, console
from pyodide.ffi import create_proxy # type: ignore


def button(args=None):
    ws.send("Hello Server!")  # Send a message to the server.
    console.log(ws.msg())  # Get the latest servers response.
    console.log(ws.msgDict())  # Get all latest dicts from servers responses.


def main():
    ws.start("ws", "127.0.0.1", "7005")  # Set's up the WebSocket connection.

    document.getElementById("main").innerHTML = f'<button id="button" type="submit">A button</button>'
    document.getElementById("button").addEventListener("click", create_proxy(button))


if __name__ == "__main__":
    main()
