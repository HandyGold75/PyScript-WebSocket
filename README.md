# PyScript-WebSocket

A JavaScript WebSocket client meant to be used in PyScript.

Pyodide doesn't support networking so networking actions are relayed to Client.js trough this Client.py script.
When a JS function returns a value a litle to late a "Future" object is returned.
This "Furture" object becomes available when the script calling it die's therefor Client.py returns the return.

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
  * This is not done as import so you have control when the connection is attempted.
* ws.send
  * Send a message to the server.
  * Takes 1 arguments which is the message that needs to be send.
  * Returns the servers response.
  * If server doesn't respond in time then returns the latest msg (defaults to a blank string)
  * Raises ConnectionError if the client or the server has disconnected.
* ws.msg
  * Takes 1 optional argument which can be the message send to the server previously.
  * Returns the latest servers response (defaults to a blank string).
  * Returns false if the received message hasn't changed from the last time it was called.
  * Returns the possilbe dublicate message if the optional argument is the same as the previous send message.
  * Raises ConnectionError if the client or the server has disconnected.
