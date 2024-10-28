import unittest
import templater


class TemplaterTest(unittest.TestCase):

    def test_1(self):
        path = 'networks/'
        result = templater.mikrotik_templater(path)
        a = '/ip firewall address-list\n' +\
            'add list=vpn_list comment="Network ISP-03" address=172.16.1.0/24\n' +\
            'add list=vpn_list comment="Network ISP-03" address=172.16.2.0/24\n' +\
            'add list=vpn_list comment="Network ISP-03" address=172.16.3.0/24\n' +\
            'add list=vpn_list comment="Network ISP-02" address=10.100.1.0/24\n' +\
            'add list=vpn_list comment="Network ISP-02" address=10.100.2.0/24\n' +\
            'add list=vpn_list comment="Network ISP-02" address=10.100.3.0/24\n' +\
            'add list=vpn_list comment="Network ISP-01" address=192.168.100.0/24\n' +\
            'add list=vpn_list comment="Network ISP-01" address=192.168.200.0/24\n' +\
            'add list=vpn_list comment="Network ISP-01" address=192.168.300.0/24\n'
        self.assertEqual(result, a)
