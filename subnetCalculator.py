#!/usr/bin/python3

given_input = input()

ip,subnet_mask = given_input.split('/')

ip = list(map(int,ip.split('.')))
subnet_mask = int(subnet_mask)

# IP and Subnet Mask Detached

binary_ip = list(map(bin,ip))

mask_string = ''

for i in range(32):
    if i < subnet_mask:
        mask_string = mask_string + '1'
    else:
        mask_string = mask_string + '0'


mask_octate = []



count_number = 0

for i in range(4):
    mask_octate.append(mask_string[count_number:count_number+8])
    count_number += 8


new_subnet_mask = []

for i in mask_octate:
    new_subnet_mask.append(int(i,2))

print(new_subnet_mask)


