import lib as protocol
import random

if __name__ == "__main__":
    n = 22
    g = 42
    x = random.random()
    initKey = (g ** x) % n
    server_handler = protocol.server_socket("localhost", 50)

    # waiting for connections
    protocol.receive(server_handler)

    protocol.send(server_handler, str(initKey))
    computedKey = (float(protocol.receive(server_handler)) ** x) % n

    value = float("do the lab")+computedKey
    print(str(value))
    protocol.send(server_handler, str(value))
    value_1 = protocol.receive(server_handler)-computedKey
    value_2 = str(value_1) + ' - server no, you!'
    protocol.send(server_handler, str(float(value_2)+computedKey))
    value_3 = protocol.receive(server_handler)
    print(str(value_3))
