# PyScript-WebSocket

A JavaScript WebSocket client meant to be used in PyScript.

Pyodide doesn't support networking so networking actions are done in a JavaScript websocket client.

_Note: I'm not an developer by profession and the code is far from best practice, this is just something I use personaly that I think might be usefull for someone else, if you see any improvements I'm open for suggestions._

## Note

This is meant as a simple template/ demo.

Note that when calling a ws function feedback (if any) can only be read after the hole script finshes, as the received messaged changes don't appear while the script is running.
To work around this events can be used, for eq. use event mousedown or mouseover to send information request to the websocket server, if the server is fast enough then the event mouseup can be used to query the possible received information.

## Functions

* ws.start
  * Set's up the WebSocket connection.
  * This is not done at import so you have control when the connection is attempted.
  * Takes 3 arguments which the protocol, ip and port that the websocket needs to connect to.
* ws.send
  * Send a message to the server.
  * Takes 1 arguments which is the message that needs to be send.
  * Raises ConnectionError if the client or the server has disconnected.
* ws.msg
  * Returns the latest servers response (defaults to a blank string).
  * Raises ConnectionError if the client or the server has disconnected.
* ws.msgDict
  * Returns all latest dicts from servers responses (defaults to a empty dict).
  * First 2 layers are consistent, deeper layers will be removed if not present in the new request when the top layer is updated.
  * Raises ConnectionError if the client or the server has disconnected.
