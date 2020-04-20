#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyTopology(Topo):
    """
    A basic topology
    """
    def __init__(self):
        Topo.__init__(self)

        # Set Up Topology Here
	switch = self.addSwitch('s1')    ## Adds a Switch
        switch = self.addSwitch('s2')
        switch = self.addSwitch('s3')

        host1 = self.addHost('h1')       ## Adds a Host
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')

	self.addLink(host1, 's1')      ## Add a link
        self.addLink(host3, 's1')
        self.addLink(host2, 's2')
        self.addLink(host4, 's2')
        self.addLink(host5, 's3')
        self.addLink(host6, 's3')
        self.addLink('s1', 's3')
        self.addLink('s2', 's3')
       
if __name__ == '__main__':
    """
    If this script is run as an executable (by chmod +x), this is
    what it will do
    """

    topo = MyTopology()            ## Creates the topology
    net = Mininet( topo=topo )        ## Loads the topology
    net.start()                      ## Starts Mininet

    # Commands here will run on the simulated topology
    CLI(net)

    net.stop()                       ## Stops Mininet
