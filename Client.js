function NEWMESSAGE(data) {
    if (data.startsWith("{") && data.endsWith("}")) {
        for (dict in JSON.parse(data)) {
            obj.msgDict[dict] = { ...obj.msgDict[dict], ...JSON.parse(data)[dict] }
        }
    }

    obj.lastMsg = data;

    console.log("Got message: " + data)
};

class obj {
    ws;
    IP;
    PORT;
    lastCom;
    lastMsg;
    msgDict;
};

function wsStart() {
    if (obj.ws === undefined) {
        obj.IP = "127.0.0.1";
        obj.PORT = 7005;
        obj.lastCom = "";
        obj.lastMsg = "";
        obj.msgDict = {};

        obj.ws = new WebSocket("ws://" + obj.IP + ":" + obj.PORT);

        obj.ws.onopen = (event) => {
            console.log("Opened connection to ws://" + obj.IP + ":" + obj.PORT)
        };

        obj.ws.onmessage = ({ data }) => {
            NEWMESSAGE(data)
        }
    }
};

function wsUpState() {
    if (obj.ws.readyState === 0 || obj.ws.readyState === 1) {
        return true
    }

    else if (obj.ws.readyState === 2 || obj.ws.readyState === 3) {
        return false
    }
};

function wsSend(com) {
    obj.lastCom = com;
    obj.ws.send(com);

    return obj.lastCom
};

function wsMsg() {
    return obj.lastMsg
};

function wsMsgDict() {
    return JSON.stringify(obj.msgDict)
}
