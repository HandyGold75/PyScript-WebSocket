# PyScript-WebSocket

A JavaScript WebSocket client meant to be used in PyScript.

Pyodide doesn't support networking so networking actions are relayed to Client.js.
To pythonfy this the class ws is used so interacting with the websocket client is a bit easier.

_Note: I'm not an developer by profession and the code is far from best practice, this is just something I use personaly that I think might be usefull for someone else, if you see any improvements I'm open for suggestions._

## Note

This is meant as a simple template/ demo, therefor basic functions are missing.

Note that when calling a ws function feedback (if any) can only be read after the hole script finshes, as the script stalls Client.js until complete.
To work around this events can be used, for eq. use event mousedown or mouseover to send information request to the websocket server, if the server is fast enough then the event mouseup can be used to query the possible received information.

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
