from js import wsStart, wsUpState, wsSend, wsMsg

class ws:
    def start():
        return wsStart()

    def send(com):
        if not wsUpState():
            raise ConnectionError(f"Unable to verify healty connection!")

        wsSend(com)

        return wsMsg(com)

    def msg(com=""):
        if not wsUpState():
            raise ConnectionError(f"Unable to verify healty connection!")

        return wsMsg(com)
