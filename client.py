import lib as protocol
import random

if __name__ == "__main__":
    n = 22
    g = 42
    # x = random.random()
    # initKey = (g**x) % n
    proto_handler = protocol.socket()
    protocol.connect_to(proto_handler, 'localhost', 50)
    value = protocol.receive(proto_handler)
    # computedKey = (float(protocol.receive(proto_handler))**x) % n
    print(value)

    value = 'second message'
    protocol.send(proto_handler, value)
    val_new = protocol.receive(proto_handler)
    protocol.send(proto_handler, val_new + ' final message')
    print(val_new)
