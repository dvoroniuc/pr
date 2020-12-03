import lib as protocol
import random

if __name__ == "__main__":
    n = 22
    g = 42
    x = random.random()

    proto_handler = protocol.socket()
    protocol.connect_to(proto_handler, 'localhost', 50)
    initKey = (g**x) % n
    computedKey = (float(protocol.receive(proto_handler))**x) % n
    protocol.send(proto_handler, str(initKey))
    value = float(protocol.receive(proto_handler))-computedKey
    value_1 = str(value)+' - client no, you!'
    protocol.send(proto_handler, str(float(value_1)+computedKey))
    value_2 = float(protocol.receive(proto_handler))-computedKey
    value_3 = str(value_2)+' - nope'
    protocol.send(proto_handler, str(float(value_3)+computedKey))
    print(value_3)
