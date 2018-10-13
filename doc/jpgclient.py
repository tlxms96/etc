import cv2
import socket

cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8888))

while True:
    _, frame = cap.read()
    _, converted = cv2.imencode('.jpg', frame)
    '''
    with open("test.jpg", "wb") as binary_file:
        binary_file.write(converted)
    '''
    clientsocket.sendall(converted)
