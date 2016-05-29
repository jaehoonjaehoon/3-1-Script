HOST = '127.0.0.1' 			#localhost
PORT = 50007 			#������ ���� ��Ʈ�� �����
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #���� ����
s.connect((HOST,PORT))
s.send(b'Hello, python') 		#���ڸ� ����
data = s.recv(1024) 		#������ ���� ������ ����
s.close()
print('Received', repr(data))