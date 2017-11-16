#!/usr/bin/python3


while True:
    try:
        given_input = input('Please provide IP address in XXX:XXX:XXX:XXX/YY this format: ')
        ip, subnet_mask_number = given_input.split('/')
        ip = list(map(int, ip.split('.')))
        subnet_mask_number = int(subnet_mask_number)
        break
    except:
        print()
        print('Please follow the format \n')


IP_in_binary = [i[2:].zfill(8) for i in list(map(bin,ip))]

IP_binary_string = ''.join(IP_in_binary)


Host_ID = IP_binary_string[0:subnet_mask_number]
Host_bits = 32-subnet_mask_number


Network_bits = '0'*Host_bits
Broadcast_bits = '1'*Host_bits
First_IP_bits = '0'*(Host_bits-1) + '1'
Last_IP_bits = '1'*(Host_bits-1) + '0'


Network_address_binary_string = Host_ID+Network_bits
Broadcast_address_binary_string = Host_ID+Broadcast_bits
First_IP_address_binary_string = Host_ID+First_IP_bits
Last_IP_address_binary_string = Host_ID+ Last_IP_bits

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


subnet_mask_string = ('1'*subnet_mask_number) + '0'*(32-subnet_mask_number)

print()
print('Network ID: {}'.format(binaray_To_String(Network_address_binary_string)))
print('Broadcast Address: {}'.format(binaray_To_String(Broadcast_address_binary_string)))
print('Subnet Mask: {}'.format(binaray_To_String(subnet_mask_string)))
print('Usable IP range: {} to {}'.format(binaray_To_String(First_IP_address_binary_string),binaray_To_String(Last_IP_address_binary_string)))


