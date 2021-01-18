import time
from threading import Thread

import websocket
from websocket import WebSocketApp


def on_message(ws: WebSocketApp, message):
    print(message)


def on_error(ws: WebSocketApp, error):
    print(error)


def on_close(ws: WebSocketApp):
    print("### closed ###")


def on_open(ws: WebSocketApp):
    def run():
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    Thread(target=run).start()


websocket.enableTrace(True)
client = WebSocketApp(
    "ws://echo.websocket.org/",
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open,
)
client.run_forever()
