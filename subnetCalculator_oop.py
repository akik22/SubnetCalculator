#!/usr/bin/python3

class SubnetCalculator(object):

    def __init__(self,given_input):
        IP, subnet_mask_prefix = given_input.split('/')
        IP = list(map(int, IP.split('.')))
        IP_in_binary = [i[2:].zfill(8) for i in list(map(bin,IP))]
        IP_binary_string = ''.join(IP_in_binary)
        self.subnet_mask_prefix = int(subnet_mask_prefix)
        self.Host_ID = IP_binary_string[0:self.subnet_mask_prefix]
        self.Host_bits = 32 - self.subnet_mask_prefix


    @staticmethod
    def binary_string_to_IP(binary_string):
        octate = []
        count = 0
        IP = []

        for i in range(4):
            octate.append(binary_string[count:count + 8])
            count += 8

        for i in octate:
            IP.append(str((int(i, 2))))

        return '.'.join(IP)


    def network_id(self):
        Network_bits = '0'*self.Host_bits
        Network_address_binary_string = self.Host_ID + Network_bits
        return self.binary_string_to_IP(Network_address_binary_string)

    def broadcast_address(self):
        Broadcast_bits = '1' * self.Host_bits
        Broadcast_address_binary_string = self.Host_ID + Broadcast_bits
        return self.binary_string_to_IP(Broadcast_address_binary_string)

    def subnet_mask(self):
        subnet_mask_binary_string = ('1' * self.subnet_mask_prefix) + '0' * (32 - self.subnet_mask_prefix)
        return self.binary_string_to_IP(subnet_mask_binary_string)

    def usable_ip_range(self):
        First_IP_bits = '0' * (self.Host_bits - 1) + '1'
        Last_IP_bits = '1' * (self.Host_bits - 1) + '0'
        First_IP_address_binary_string = self.Host_ID + First_IP_bits
        Last_IP_address_binary_string = self.Host_ID + Last_IP_bits
        return '{} - {}'.format(self.binary_string_to_IP(First_IP_address_binary_string),self.binary_string_to_IP(Last_IP_address_binary_string))



a = SubnetCalculator('192.168.0.2/24')

networkID = a.network_id()
broadcast = a.broadcast_address()
subnetMask = a.subnet_mask()
ipRange = a.usable_ip_range()


print(networkID)
print(broadcast)
print(subnetMask)
print(ipRange)
