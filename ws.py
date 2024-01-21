from json import loads

from js import eval


class WS:
    def __init__(self, protocol, ip, port) -> None:
        self.PROTO = protocol
        self.IP = ip
        self.PORT = port

        ws = eval(f'new WebSocket("{self.PROTO}://{self.IP}:{self.PORT}")')

        ws.onopen = self.onOpen
        ws.onmessage = self.onMessage
        ws.onerror = self.onError
        ws.onclose = self.onClose

        self.lastMsg = ""
        self.msgDict = {}
        self.msgReply = {}

    def onOpen(self, arg):
        print(f"Opened connection to {self.PROTO}://{self.IP}:{self.PORT}")

    def onMessage(self, arg):
        msg = arg.data
        self.lastMsg = msg

        if msg.startswith("{") and msg.endswith("}"):
            data = loads(msg)

            for dict in data:
                if not dict in self.msgDict:
                    self.msgDict[dict] = {}

                self.msgDict[dict] = {**self.msgDict[dict], **data[dict]}

        print(f"Received message: {msg}")

        if msg.split(" ")[0] in self.msgReply:
            msg = msg.split(" ")[0]
        elif " ".join(msg.split(" ")[:2]) in self.msgReply:
            msg = " ".join(msg.split(" ")[:2])
        else:
            return None

        msgOrFunc, funcArgs, funcKwargs = self.msgReply[msg][1:]
        if self.msgReply[msg][0]:
            self.msgReply.pop(msg)

        if callable(msgOrFunc):
            msgOrFunc(*funcArgs, **funcKwargs)
        else:
            self.ws.send(msgOrFunc)

    def onError(self, arg):
        print(arg)

    def onClose(self, arg):
        print(f"Closed connection to {self.PROTO}://{self.IP}:{self.PORT}")

    def upState(self):
        if self.ws.readyState in [0, 1]:
            return True

        return False

    def send(self, com):
        if not self.upState():
            raise ConnectionError(f"Unable to verify healty connection!")

        self.ws.send(com)

    def onMsg(self, msgRecv: str, msgOrFunc: str, args: tuple = (), kwargs: dict = {}, oneTime: bool = False):
        self.msgReply[msgRecv] = (oneTime, msgOrFunc, args, kwargs)
