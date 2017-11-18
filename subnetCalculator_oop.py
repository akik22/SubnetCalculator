#!/usr/bin/python3

'''
A simple Subnet Calculator prepared by Alamgir Jalil
contact Details: 
Email: akik22@gmail.com
Phone No: +880-1674138363
anyone can use it
'''

class SubnetCalculator(object):

    # Here is this part it takes ip and subnet prefix as IP/prefix format and breaks into 3 parts
    # 1. Subnet Mask prefix
    # 2. Host ID calculated in binary format from given ip address.
    # 3. Calculation bits from prefix

    def __init__(self,given_input):
        IP, subnet_mask_prefix = given_input.split('/')
        IP = map(int, IP.split('.'))
        IP_in_binary = [i[2:].zfill(8) for i in map(bin,IP)]
        IP_binary_string = ''.join(IP_in_binary)
        self._subnet_mask_prefix = int(subnet_mask_prefix)
        self._host_id = IP_binary_string[0:self._subnet_mask_prefix]
        self._calulation_bits = 32 - self._subnet_mask_prefix


    # This function takes a binary string as an input and returns the ip address in x.x.x.x format

    @staticmethod
    def _binary_to_string_ip(binary_string):
        octate = []
        count = 0
        IP = []

        for i in range(4):
            octate.append(binary_string[count:count + 8])
            count += 8

        for i in octate:
            IP.append(str((int(i, 2))))

        return '.'.join(IP)


    # Network bits of an ip address is always zero so by adding host id with network bits we'll get the
    # Network id of that specific address.

    def network_id(self):
        Network_bits = '0'*self._calulation_bits
        Network_address_binary_string = self._host_id + Network_bits
        return self._binary_to_string_ip(Network_address_binary_string)


    # broadcas bits of an ip address is always one so by adding host id with broadcas bits we'll get the
    # broadcas id of that specific address.

    def broadcast_address(self):
        Broadcast_bits = '1' * self._calulation_bits
        Broadcast_address_binary_string = self._host_id + Broadcast_bits
        return self._binary_to_string_ip(Broadcast_address_binary_string)


    # Subnet Mask is calculated from the prefix. (prefix number will be the 1's and rest is 0)

    def subnet_mask(self):
        subnet_mask_binary_string = ('1' * self._subnet_mask_prefix) + '0' * (32 - self._subnet_mask_prefix)
        return self._binary_to_string_ip(subnet_mask_binary_string)


    # First ip address will be all zeroes in calculation bit with a 1 in last
    # Last ip address will be all ones in calculation bit with a 0 in last
    # Both added with host id will give the required address

    def usable_ip_range(self):
        First_IP_bits = '0' * (self._calulation_bits - 1) + '1'
        Last_IP_bits = '1' * (self._calulation_bits - 1) + '0'
        First_IP_address_binary_string = self._host_id + First_IP_bits
        Last_IP_address_binary_string = self._host_id + Last_IP_bits
        return '{} - {}'.format(self._binary_to_string_ip(First_IP_address_binary_string),self._binary_to_string_ip(Last_IP_address_binary_string))


a = SubnetCalculator('192.168.0.2/24')

networkID = a.network_id()
broadcast = a.broadcast_address()
subnetMask = a.subnet_mask()
ipRange = a.usable_ip_range()


print(networkID)
print(broadcast)
print(subnetMask)
print(ipRange)
