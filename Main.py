from js import document, wsStart, wsUpState, wsSend, wsMsg, console
from pyodide.ffi import create_proxy

class ws:
    def start():
        return wsStart()

    def send(com):
        if not wsUpState():
            raise ConnectionError(f"Unable to verify healty connection!")

        return wsSend(com)

    def msg():
        if not wsUpState():
            raise ConnectionError(f"Unable to verify healty connection!")

        return wsMsg()

    def msgDict():
        if not wsUpState():
            raise ConnectionError(f"Unable to verify healty connection!")

        return wsMsgDict()

def button(args=None):
    console.log(ws.send("A message for the server.")) # Send a message.
    console.log(ws.msg())                             # Get the latest received message.
    console.log(ws.msgDict())                         # Get all the latest received dicts.


def main():
    ws.start()     # Start the WebSocket.

    element = document.getElementById("main")
    element.innerHTML += f'<button id="button" type="submit">A button</button>'

    proxy = create_proxy(button)
    document.getElementById("button").addEventListener("click", proxy)


if __name__ == "__main__":
    main()