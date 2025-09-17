import socket

target=input("Hedef IP veya hostname girin:")

start_port=int(input("Başlangıç Portu:"))
end_port=int(input("Bitiş Portu:"))

print(f"\n {target} üzerinde port araması başlatılıyor")

for port in range(start_port,end_port + 1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    result=s.connect_ex((target,port))
    if result==0:
        print(f"Port {port} açık")
    s.close()

if __name__=="__main__":
    main()