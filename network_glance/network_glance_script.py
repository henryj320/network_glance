# import scapy.all as scapy

#  from scapy.all import ARP, Ether, srp
import scapy.all as scapy
import socket

def run(): 

    # request = scapy.ARP()  # Creates an Address Resolution Protocol packet (request or response).
    # request.summary()  # Shows this device's IP address.
    # request.show()  # Returns all the fields of the ARP packet.
    # print("hey!")

    # request.pdst = 'x'  # PDST is the target.
    # broadcast = scapy.Ether()

    # broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
    # request_broadcast = broadcast / request
    # clients = scapy.srp(request_broadcast, timeout = 1)[0]
    # for element in clients:
    #     print(element[1].psrc + "      " + element[1].hwsrc)   # PSRC is the target's IP

    # ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2)
    # output = scapy.arping("0.0.0")

    
    #output = scapy.ARP()
    #output = scapy.arping()

    #print(output)


    target_ip = "192.168.1.101/24"  # Destination IP Address.

    arp = scapy.ARP(pdst=target_ip)  # Creates an ARP packet.

    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Creates am Ethernet broadcast packet

    packet = ether/arp  # Stacks the two packets together.

    result = scapy.srp(packet, timeout=3)[0]  # "S"end and "R"eceive "P"ackets.

    




    # a list of clients, we will fill this in the upcoming loop
    clients = []
    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        print(received.psrc[0])
        # print(socket.gethostbyaddr(received.psrc[0]))
        print(received)
    
    print(socket.gethostbyaddr('192.168.1.101'))  # Works: Henry Ideapad ubuntu
    print(socket.gethostname())  # Returns the hostname of this computer.

    # proper_ip = socket.gethostbyname(socket.gethostname())
    # print(socket.gethostbyaddr(proper_ip))  # Works: Henry Ideapad ubuntu

    for client in clients:
        print(client)



if __name__ == '__main__':
    run()