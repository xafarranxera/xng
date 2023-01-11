"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        h11 = self.addHost('h11', mac='20:22:01:00:00:11', ip='10.0.0.11/24')
        h12 = self.addHost('h12', mac='20:22:01:00:00:12', ip='10.0.0.12/24')
        h21 = self.addHost('h21', mac='20:22:01:00:00:21', ip='10.0.0.21/24')
        h22 = self.addHost('h22', mac='20:22:01:00:00:22', ip='10.0.0.22/24')
	# Add EdgeSwitches
        e1 = self.addSwitch( 'e1' )
        e2 = self.addSwitch( 'e2' )
	# Add AgregationCoreSwitches
        a1 = self.addSwitch( 'a1' )
 	# Add links
        self.addLink( h11, e1 )
        self.addLink( h12, e1 )
        self.addLink( h21, e2 )        
        self.addLink( h22, e2 )
        self.addLink( e1, a1, 24, 22 )
        self.addLink( e2, a1, 24, 23 )
topos = { 'mytopo': ( lambda: MyTopo() ) }
