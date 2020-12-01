
from scapy.sendrecv import srp
import step2
from scapy.layers.l2 import Ether, ARP
from scapy.config import conf
ipscan = "192.168.100.1/24"

try:
    ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan), timeout=2, verbose=False)
except Exception as e:
    print(str(e))
else:
    for snd, rcv in ans:
        list_mac = rcv.sprintf("%Ether.src% - %ARP.psrc%")
        comp = list_mac.split('-')
        comm = step2.get_company_info(comp[0])
        print(list_mac, comm)


