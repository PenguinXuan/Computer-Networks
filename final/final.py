#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
    
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
    h1 = self.addHost('h10',mac='00:00:00:00:00:01',ip='10.0.1.10',defaultRoute="h1-eth0")
    h2 = self.addHost('h20',mac='00:00:00:00:00:02',ip='10.0.2.20',defaultRoute="h2-eth0")
    h3 = self.addHost('h30',mac='00:00:00:00:00:03',ip='10.0.3.30',defaultRoute="h3-eth0")
    h4 = self.addHost('h40',mac='00:00:00:00:00:04',ip='10.0.4.40',defaultRoute="h4-eth0")
    h5 = self.addHost('h50',mac='00:00:00:00:00:05',ip='10.0.5.50',defaultRoute="h5-eth0")
    h6 = self.addHost('h60',mac='00:00:00:00:00:06',ip='10.0.6.60',defaultRoute="h6-eth0")
    h7 = self.addHost('h70',mac='00:00:00:00:00:07',ip='10.0.7.70',defaultRoute="h7-eth0")
    h8 = self.addHost('h80',mac='00:00:00:00:00:08',ip='10.0.8.80',defaultRoute="h8-eth0")
    h9 = self.addHost('serv1',mac='00:00:00:00:00:09',ip='10.0.9.10',defaultRoute="h9-eth0")
    hx = self.addHost('untrustedH',mac='00:00:00:00:00:10',ip='10.0.10.11', defaultRoute="h10-eth0")
   
    # Create a switch. No changes here from Lab 1.
    s1 = self.addSwitch('s1') # floor 1 s1
    s2 = self.addSwitch('s2') # floor 1 s2
    s3 = self.addSwitch('s3') # floor 2 s1
    s4 = self.addSwitch('s4') # floor 2 s2
    s5 = self.addSwitch('s5') # core
    s6 = self.addSwitch('s6') # data center

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    self.addLink(s1,h1, port1=1, port2=1)   # s1 to h1
    self.addLink(s1,h2, port1=2, port2=1)   # s1 to h2
    self.addLink(s2,h3, port1=1, port2=1)   # s2 to h3
    self.addLink(s2,h4, port1=2, port2=1)   # s2 to h4
    self.addLink(s3,h5, port1=1, port2=1)   # s3 to h5
    self.addLink(s3,h6, port1=2, port2=1)   # s3 to h6
    self.addLink(s4,h7, port1=1, port2=1)   # s4 to h7
    self.addLink(s4,h8, port1=2, port2=1)   # s4 to h8
    self.addLink(s6,h9, port1=1, port2=1)   # data center to serv1 
    self.addLink(s5,s1, port1=1, port2=3)   # core to s1
    self.addLink(s5,s2, port1=2, port2=3)   # core to s2
    self.addLink(s5,s3, port1=3, port2=3)   # core to s3
    self.addLink(s5,s4, port1=4, port2=3)   # core to s4
    self.addLink(s5,hx, port1=5, port2=1)   # core to untrustedH
    self.addLink(s5,s6, port1=6, port2=3)   # core to data center

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  #net = Mininet(topo=topo)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
