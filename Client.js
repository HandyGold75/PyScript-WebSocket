class obj {
    ws;
    IP;
    PORT;
    lastCom;
    lastMsg1;
    lastMsg2;
}

function wsStart() {
    if (obj.ws === undefined) {
        obj.ws = null;
        obj.IP = "127.0.0.1";
        obj.PORT = 7005;
        obj.lastCom = "";
        obj.lastMsg1 = "";
        obj.lastMsg2 = "";

        obj.ws = new WebSocket("ws://" + obj.IP + ":" + obj.PORT);

        obj.ws.onopen = (event) => {
            console.log("Opened connection to ws://" + obj.IP + ":" + obj.PORT)
        };

        obj.ws.onmessage = ({ data }) => {
            obj.lastMsg1 = data;
            console.log("Got message: " + data)
        };
    }
};



function wsUpState(){
    if (obj.ws.readyState === 0 || obj.ws.readyState === 1) {
        return true
    }

    else if (obj.ws.readyState === 2 || obj.ws.readyState === 3) {
        return false
    }
}
function wsCom(com) {
    obj.lastCom = com
    obj.ws.send(com)
};
function wsMsg(com) {
    if (com == obj.lastCom && com != "") {
        obj.lastMsg2 = obj.lastMsg1;

        return obj.lastMsg1
    }

    else if (obj.lastMsg1 != obj.lastMsg2) {
        obj.lastMsg2 = obj.lastMsg1;
        obj.lastCom = com;

        return obj.lastMsg1
    }
    return false
}
