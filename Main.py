from Client import ws
from js import document, console
from pyodide.ffi import create_proxy


def button(args=None):
    console.log(ws.send("A message for the server.")) # Send a message.
    console.log(ws.msg())                             # Get the latest received message.


def main():
    ws.start()     # Start the WebSocket.

    element = document.getElementById("main")
    element.innerHTML += f'<button id="button" type="submit">A button</button>'

    proxy = create_proxy(button)
    document.getElementById("button").addEventListener("click", proxy)


if __name__ == "__main__":
    main()