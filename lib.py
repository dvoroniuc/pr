import socket as skt
import json
import hashlib

BUFF_SIZE = 1024


def make_packet(value):
    return json.dumps({
        'checkSum': hashlib.md5(value.encode('utf-8')).hexdigest(),
        'payload': value,
    }).encode('utf-8')


def is_valid(packet):
    value = packet['payload']
    return packet['checkSum'] == hashlib.md5(value.encode('utf-8')).hexdigest()


class Socket:
    def __init__(self, sock):
        self.sock = sock
        self.to_address = None


def socket():
    return Socket(skt.socket(skt.AF_INET, skt.SOCK_DGRAM))


def server_socket(host, port):
    sock = socket()
    sock.sock.bind((host, port))
    return sock


def connect_to(sock, host, port):
    sock.to_address = (host, port)
    print('connecting')
    try:
        send(sock, 'connect')
        return sock
    except sock.timeout:
        print('Timed out')


def send(sock, value):
    sock.sock.sendto(make_packet(value), sock.to_address)
    data, address = sock.sock.recvfrom(BUFF_SIZE)
    packet = json.loads(data.decode('utf-8'))
    try:
        while packet['payload'] == 'Error':
            sock.sock.sendto(make_packet(value), sock.to_address)
            data, address = sock.sock.recvfrom(BUFF_SIZE)
    except socket.timeout:
        print('Timed out')


def receive(sock):
    while True:
        data, address = sock.sock.recvfrom(BUFF_SIZE)
        packet = json.loads(data.decode('utf-8'))
        print("packet received")

        if is_valid(packet):
            sock.sock.sendto(make_packet('ack'), address)
            if packet['payload'] == 'connect':
                sock.to_address = address
                print('connection established')
                return
            else:
                return packet['payload']
        else:
            sock.sock.sendto(make_packet('Error'), address)
