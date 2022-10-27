# PyScript-WebSocket

A JavaScript WebSocket client meant to be used in PyScript.

Pyodide doesn't support networking so networking actions are relayed to Client.js trough this Client.py script.
When a JS function returns a value a litle to late a "Future" object is returned.
Therefor functions of Client.js are called trough Client.py to make sure a non future object is returned.

_Note: I'm not an developer by profession and the code is far from best practice, this is just something I use personaly that I think might be usefull for someone else, if you see any improvements I'm open for suggestions._

## Note

Currently there are functions missing such as setting the IP and PORT manualy, I might do this later or you can do it yourself.
Note that ws.send and ws.msg can NOT be called before the main script finishes running as the connection only completes when the script has finished! These functions can be used on event calls with buttons.

The last message the server has send can only be read after a event is completed, this makes it so ws.send and ws.msg can only return the message that was recevied on the previous event and as such will lack behind.
If you know a workaround for this I'm happy to hear your fix for this.

There are probably more shortcommings to this set-up, so be carefull when using this and check what your accualy calling.

## Functions

* ws.start
  * Set's up the WebSocket connection.
  * This is not done at import so you have control when the connection is attempted.
* ws.send
  * Send a message to the server.
  * Takes 1 arguments which is the message that needs to be send.
  * Returns the send message.
  * Raises ConnectionError if the client or the server has disconnected.
* ws.msg
  * Returns the latest servers response (defaults to a blank string).
  * Raises ConnectionError if the client or the server has disconnected.
* ws.msgDict
  * Returns all latest dicts from servers responses (defaults to a empty dict).
  * Raises ConnectionError if the client or the server has disconnected.
