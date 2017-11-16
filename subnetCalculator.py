#!/usr/bin/python3

given_input = input()

ip,subnet_mask = given_input.split('/')

ip = list(map(int,ip.split('.')))
subnet_mask = int(subnet_mask)

# IP and Subnet Mask Detached

binary_ip = list(map(bin,ip))

total_octate = 4
full_octate_number = subnet_mask//8
partial_octate_number = full_octate_number+1
blank_octate_number = total_octate - partial_octate_number



new_subnet_mask = []

for _ in range(subnet_mask):
    new_subnet_mask.append(255)

