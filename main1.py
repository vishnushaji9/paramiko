import paramiko


hostname = "192.168.24.243"   
port = 22
username = "kali"           
password = "kali"   


local_file = "C:\\Users\\vishnu\\Documents\\ceh.pdf"   #local file path on windows
remote_file = "/home/kali/Documents/ceh.pdf"   #file path on kali linux            

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("Connecting to Kali VM...")
    ssh.connect(hostname, port, username, password)
    print("Connected successfully!")
    
    sftp = ssh.open_sftp()  #start SFTP session

    sftp.put(local_file, remote_file)
    print(f"Uploaded {local_file} to {remote_file}")

    sftp.close()
    ssh.close()
    print("Connection closed.")

except Exception as e:
    print("Error:",str(e)) 