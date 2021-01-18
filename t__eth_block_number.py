import json
import os
import socket
from typing import Optional, Tuple

import websocket
from dotenv import load_dotenv


def eth_block_number(node: str) -> Tuple[str, Optional[int]]:
    data = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1,
    }
    try:
        ws = websocket.create_connection(node, timeout=3)
        ws.send(json.dumps(data))
        res = ws.recv()
        ws.close()
        return "", int(json.loads(res)["result"], 16)
    except socket.timeout:
        return "TIMEOUT", None
    except Exception as err:
        return str(err), None


def main():
    load_dotenv()
    node = os.getenv("NODE")
    print(eth_block_number(node))


if __name__ == "__main__":
    main()
