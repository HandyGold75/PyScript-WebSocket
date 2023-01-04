from json import loads
from js import eval, console


class glb:
    PROTO = ""
    IP = ""
    PORT = ""
    ws = None
    lastMsg = ""
    msgDict = {}


class ws:
    def onOpen(arg):
        console.log(f'Opened connection to {glb.PROTO}://{glb.IP}:{glb.PORT}')

    def onMessage(arg):
        msg = arg.data
        glb.lastMsg = msg

        if msg.startswith("{") and msg.endswith("}"):
            data = loads(msg)

            for dict in data:
                if not dict in glb.msgDict:
                    glb.msgDict[dict] = {}

                glb.msgDict[dict] = {**glb.msgDict[dict], **data[dict]}

        print(f'Received message: {msg}')

    def onError(arg):
        console.error(arg)

    def onClose(arg):
        console.log(f'Closed connection to {glb.PROTO}://{glb.IP}:{glb.PORT}')

    def upState():
        if glb.ws.readyState in [0, 1]:
            return True

        elif glb.ws.readyState in [2, 3]:
            return False


def start(protocol: str, ip: str, port: str):
    if not glb.ws is None:
        return None

    glb.PROTO = str(protocol)[:3]
    glb.IP = str(ip[:32])
    glb.PORT = str(port)[:5]

    glb.ws = eval(f'new WebSocket("{glb.PROTO}://{glb.IP}:{glb.PORT}")')

    glb.ws.onopen = ws.onOpen
    glb.ws.onmessage = ws.onMessage
    glb.ws.onerror = ws.onError
    glb.ws.onclose = ws.onClose


def send(com):
    if not ws.upState():
        raise ConnectionError(f"Unable to verify healty connection!")

    glb.ws.send(com)


def msg():
    if not ws.upState():
        raise ConnectionError(f"Unable to verify healty connection!")

    return glb.lastMsg


def msgDict():
    if not ws.upState():
        raise ConnectionError(f"Unable to verify healty connection!")

    return glb.msgDict
