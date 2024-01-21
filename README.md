# PyScript-WebSocket

A JavaScript WebSocket client excample meant to be used in pyodide or PyScript.

Pyodide doesn't support networking so a JavaScript websocket client object is created and then parsed to the python script.

_Note: I'm not an developer by profession and the code is far from best practice, this is just something I use personaly that I think might be usefull for someone else, if you see any improvements I'm open for suggestions._

## Note

This is meant as a simple template/ demo.

Note that when calling a ws function feedback (if any) can only be read after the current event is finished.
To work around this onMsg can be used, this can be used to setup an function to run or an reply to send to the server when an message is received.

## Functions and variables

* ws.send
  * Send a message to the server.
  * Takes 1 arguments which is the message that needs to be send.
  * Raises ConnectionError if the client or the server has disconnected.
* ws.lastMsg
  * Contains the latest servers response.
* ws.msgDict
  * Returns all latest dicts from servers responses.
  * First 2 layers are consistent, deeper layers will be removed if not present in the new request when the top layer is updated.
* ws.onMsg
  * Set up an function to run when an received message by the server starts with the selected message.
  * Can also be set up to send a message to the server instead of running an function.
  * oneTime determinace if this should be done once or ever time.
