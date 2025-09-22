import paramiko
import time



ssh =paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname= "192.168.24.243",
    port=22,
    username='kali',
    password='kali')

channel = ssh.invoke_shell()

channel.send("ifconfig\n")
time.sleep(1)
output =  channel.recv(9999).decode()
print(output)

channel.close()
ssh.close()