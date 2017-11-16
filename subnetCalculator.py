#!/usr/bin/python3

given_input = input()

ip,subnet_mask_number = given_input.split('/')

ip = list(map(int,ip.split('.')))
subnet_mask_number = int(subnet_mask_number)

# IP and Subnet Mask Detached

# binary_ip = list(map(bin,ip))

IP_in_binary = [i[2:].zfill(8) for i in list(map(bin,ip))]

IP_binary_string = ''.join(IP_in_binary)

# print('IP string: ', IP_binary_string)

Host_ID = IP_binary_string[0:subnet_mask_number]
# print(Host_ID)

Network_bits = '0'*(32-subnet_mask_number)
Broadcast_bits = '1'*(32-subnet_mask_number)

# print(Network_bits)
# print(Broadcast_bits)

Network_address_binary_string = Host_ID+Network_bits
Broadcast_address_binary_string = Host_ID+Broadcast_bits

# print(Network_address_binary_string)
# print(Broadcast_address_binary_string)


def binaray_To_String(binary_string):
    octate = []
    count = 0
    IP = []

    for i in range(4):
        octate.append(binary_string[count:count+8])
        count += 8

    for i in octate:
        IP.append(str((int(i,2))))

    return '.'.join(IP)


mask_string = ('1'*subnet_mask_number) + '0'*(32-subnet_mask_number)

print(binaray_To_String(Network_address_binary_string))
print(binaray_To_String(Broadcast_address_binary_string))
print(binaray_To_String(mask_string))