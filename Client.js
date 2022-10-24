function LOGIN() {
    obj.ws.send("<LOGIN_TOKEN> " + obj.AUTHTOKEN)
};
function LOGIN_TOKEN_FAIL() {
    obj.AUTHTOKEN = prompt("AUTH Token");
    LOGIN()
};
function LOGOUT() {
    obj.ws.close()
};
function SHUTDOWN() {
    obj.ws.close()
};


class obj {
    ws;
    IP;
    PORT;
    AUTHTOKEN;
    lastCom;
    lastMsg1;
    lastMsg2;
    fmap;
}

function wsStart() {
    if (obj.ws === undefined) {
        obj.ws = null;
        obj.IP = "127.0.0.1";
        obj.PORT = 6900;
        obj.AUTHTOKEN = "89UibZOFCKmPObSBnBxSNcorbp4eUYAKPX5V5qepEYw7tVwO0nZ3wwXGK48VXBjc";
        obj.lastCom = "";
        obj.lastMsg1 = "";
        obj.lastMsg2 = "";
        obj.fmap = {
            "<LOGIN>": LOGIN,
            "<LOGIN_TOKEN_FAIL>": LOGIN_TOKEN_FAIL,
            "<LOGOUT>": LOGOUT,
            "<SHUTDOWN>": SHUTDOWN
        };

        obj.ws = new WebSocket("ws://" + obj.IP + ":" + obj.PORT);

        obj.ws.onopen = (event) => {
            console.log("Opened connection to ws://" + obj.IP + ":" + obj.PORT)
        };

        obj.ws.onmessage = ({ data }) => {
            obj.lastMsg1 = data;

            if (data in obj.fmap) {
                obj.fmap[data]()
            }
        };
    }
};



function wsUpState() {
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
