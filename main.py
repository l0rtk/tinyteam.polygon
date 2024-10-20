from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List


# Note: Multiple subscriptions can be added to the array 
# For example, if you want to subscribe to AAPL and META,
# you can do so by adding "T.META" to the subscriptions array. ["T.AAPL", "T.META"]
# If you want to subscribe to all tickers, place an asterisk in place of the symbol. ["T.*"]
ws = WebSocketClient(api_key="RMpxIDplF6M4YdH9M1xNIYnxsPLCJwGW", subscriptions=["T.AAPL"])


def handle_msg(msg: List[WebSocketMessage]):
    print('handling messages')
    for m in msg:
        print(m)
        print('-'*50)

ws.run(handle_msg=handle_msg)