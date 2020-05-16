#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class lab3_topo(Topo):
  def build(self):
    s1 = self.addSwitch('s1')
    h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='10.0.1.10/24')
    h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='10.0.1.20/24')
    h3 = self.addHost('h3',mac='00:00:00:00:00:03',ip='10.0.1.30/24')
    h4 = self.addHost('h4',mac='00:00:00:00:00:04',ip='10.0.1.40/24')
    self.addLink(h1,s1)
    self.addLink(h2,s1)
    self.addLink(h3,s1)
    self.addLink(h4,s1)

def configure():
  topo = lab3_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()
  h1, h2, h3, h4 = net.get('h1', 'h2', 'h3', 'h4')
  
  CLI(net)

  net.stop()


if __name__ == '__main__':
  configure()
