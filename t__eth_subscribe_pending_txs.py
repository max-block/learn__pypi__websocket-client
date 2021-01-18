import json
import os

import websocket
from dotenv import load_dotenv


def on_message(ws, message):
    msg = json.loads(message)
    if msg.get("method") == "eth_subscription":
        tx_hash = msg["params"]["result"]
        print(tx_hash)
        # request
        tx_info_request = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [tx_hash],
            "id": 1,
        }
        ws.send(json.dumps(tx_info_request))
    else:
        print(msg)  # it's already a tx object


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    subscription_request = {
        "jsonrpc": "2.0",
        "method": "eth_subscribe",
        "params": ["newPendingTransactions"],
        "id": 1,
    }
    ws.send(json.dumps(subscription_request))


load_dotenv()
node = os.getenv("NODE")

# websocket.enableTrace(True)
client = websocket.WebSocketApp(
    node,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open,
)
client.run_forever()
