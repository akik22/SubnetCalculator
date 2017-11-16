#!/usr/bin/python3


# This part takes the Input and converts IP,Subnet Mask to Integer.

print()
while True:
    try:
        given_input = input('Please provide IP address in XXX:XXX:XXX:XXX/YY this format: ')
        ip, subnet_mask_number = given_input.split('/')
        ip = list(map(int, ip.split('.')))
        subnet_mask_number = int(subnet_mask_number)
        break
    except:
        print()
        print('Please follow the format')


# This Part converts the whole IP to Binary. zfill is used to complete the octate till 8

IP_in_binary = [i[2:].zfill(8) for i in list(map(bin,ip))]
IP_binary_string = ''.join(IP_in_binary)


# This part separates Host ID and Host Bits

Host_ID = IP_binary_string[0:subnet_mask_number]
Host_bits = 32-subnet_mask_number


# Network, BroadCast, First IP bits, and Last IP bits are calculated

Network_bits = '0'*Host_bits
Broadcast_bits = '1'*Host_bits
First_IP_bits = '0'*(Host_bits-1) + '1'
Last_IP_bits = '1'*(Host_bits-1) + '0'


# Create the Network,Broadcas,IP Binary strings

Network_address_binary_string = Host_ID+Network_bits
Broadcast_address_binary_string = Host_ID+Broadcast_bits
First_IP_address_binary_string = Host_ID+First_IP_bits
Last_IP_address_binary_string = Host_ID+ Last_IP_bits
subnet_mask_binary_string = ('1'*subnet_mask_number) + '0'*(32-subnet_mask_number)


# This function converts IP binary strings to IP addresses

def binary_string_to_IP(binary_string):
    octate = []
    count = 0
    IP = []

    for i in range(4):
        octate.append(binary_string[count:count+8])
        count += 8

    for i in octate:
        IP.append(str((int(i,2))))

    return '.'.join(IP)


# Printing all the output

print()
print('Network ID: {}'.format(binary_string_to_IP(Network_address_binary_string)))
print('Broadcast Address: {}'.format(binary_string_to_IP(Broadcast_address_binary_string)))
print('Subnet Mask: {}'.format(binary_string_to_IP(subnet_mask_binary_string)))
print('Usable IP range: {} - {}'.format(binary_string_to_IP(First_IP_address_binary_string),binary_string_to_IP(Last_IP_address_binary_string)))
print()

