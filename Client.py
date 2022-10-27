from js import wsStart, wsUpState, wsSend, wsMsg

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
