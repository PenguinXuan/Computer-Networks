# Final Skeleton
#
# Hints/Reminders from Lab 4:
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 4:
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    #print "Hello, World!"

    h1 = '10.0.1.10'
    h2 = '10.0.2.20'
    h3 = '10.0.3.30'
    h4 = '10.0.4.40'
    h5 = '10.0.5.50'
    h6 = '10.0.6.60'
    h7 = '10.0.7.70'
    h8 = '10.0.8.80'
    serv1 = '10.0.9.10'
    untrustedH ='10.0.10.11'
  
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.idle_timeout = 30
    msg.hard_timeout = 30
    msg.data = packet_in
    
    ip = packet.find('ipv4')
    icmp = packet.find('icmp')
    tcp = packet.find('tcp')

    if ip:   # any ip
      srcIP = ip.srcip
      dstIP = ip.dstip
      if icmp:
        if srcIP == untrustedH:      # untrusted host sends icmp traffic
          self.connection.send(msg) # drop it
        else:
          if switch_id == 1:  # floor 1 switch 1
            if dstIP == h1:  # to h1
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h2: # to h2
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 2:  # floor 1 switch 2
            if dstIP == h3:  # to h3
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h4: # to h4
              msg.actions.append(of.ofp_action_output(port = 2)) 
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 3:  # floor 2 switch 1
            if dstIP == h5:  # to h5
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h6:  # to h6
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 4:  # floor 2 switch 2
            if dstIP == h7:  # to h7
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h8:  # to h8
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core 
              self.connection.send(msg)
          elif switch_id == 5:  # core
            if dstIP == untrustedH:  # to untrustedH
              msg.actions.append(of.ofp_action_output(port = 5)) 
              self.connection.send(msg)
            elif dstIP == h1:  # to h10
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h2:  # to h20
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h3:  # to h30
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            elif dstIP == h4:  # to h40
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            elif dstIP == h5:  # to h50
              msg.actions.append(of.ofp_action_output(port = 3))
              self.connection.send(msg)
            elif dstIP == h6:  # to h60
              msg.actions.append(of.ofp_action_output(port = 3))
              self.connection.send(msg)
            elif dstIP == h7:  # to h70
              msg.actions.append(of.ofp_action_output(port = 4))
              self.connection.send(msg)
            elif dstIP == h8:  # to h80
              msg.actions.append(of.ofp_action_output(port = 4))
              self.connection.send(msg)
            elif dstIP == serv1:   # to serv1
              msg.actions.append(of.ofp_action_output(port = 6))
              self.connection.send(msg)
            else:
              self.connection.send(msg)
          elif switch_id == 6:  # data center
            if dstIP == serv1:  # to server
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
      elif tcp:
        if srcIP == untrustedH and dstIP == serv1:  # untrustedH send tcp traffic to serv1
          self.connection.send(msg)
        else:
          if switch_id == 1:  # floor 1 switch 1
            if dstIP == h1:  # to h1
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h2: # to h2
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 2:  # floor 1 switch 2
            if dstIP == h3:  # to h3
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h4: # to h4
              msg.actions.append(of.ofp_action_output(port = 2)) 
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 3:  # floor 2 switch 1
            if dstIP == h5:  # to h5
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h6:  # to h6
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
          elif switch_id == 4:  # floor 2 switch 2
            if dstIP == h7:  # to h7
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h8:  # to h8
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core 
              self.connection.send(msg)
          elif switch_id == 5:  # core
            if dstIP == untrustedH:  # to untrustedH
              msg.actions.append(of.ofp_action_output(port = 5)) 
              self.connection.send(msg)
            elif dstIP == h1:  # to h10
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h2:  # to h20
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            elif dstIP == h3:  # to h30
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            elif dstIP == h4:  # to h40
              msg.actions.append(of.ofp_action_output(port = 2))
              self.connection.send(msg)
            elif dstIP == h5:  # to h50
              msg.actions.append(of.ofp_action_output(port = 3))
              self.connection.send(msg)
            elif dstIP == h6:  # to h60
              msg.actions.append(of.ofp_action_output(port = 3))
              self.connection.send(msg)
            elif dstIP == h7:  # to h70
              msg.actions.append(of.ofp_action_output(port = 4))
              self.connection.send(msg)
            elif dstIP == h8:  # to h80
              msg.actions.append(of.ofp_action_output(port = 4))
              self.connection.send(msg)
            elif dstIP == serv1:   # to serv1
              msg.actions.append(of.ofp_action_output(port = 6))
              self.connection.send(msg)
            else:
              self.connection.send(msg)
          elif switch_id == 6:  # data center
            if dstIP == serv1:  # to server
              msg.actions.append(of.ofp_action_output(port = 1))
              self.connection.send(msg)
            else:
              msg.actions.append(of.ofp_action_output(port = 3)) # to core
              self.connection.send(msg)
    else:   # otherwise
      msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
      self.connection.send(msg)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
