# DHCP Distribution Network Project

This project simulates an office network using Cisco Packet Tracer, focused on configuring a centralized DHCP server for different departments segmented by VLANs.

## Objective

Build a segmented network infrastructure using VLANs and centralized DHCP IP address distribution.

---

## Network Topology

- **1x Cisco 2911 Router** (with Internet access and subinterface VLAN configuration)
    - **Access:** root
    - **Password:** E4w2!2s5
- **1x DHCP Server** (IP: 172.168.71.222)
- **1x Access Point (AP)** for wireless access
- **1x Switch**
- **Multiple desktops**
- **Configured VLANs:**
  - VLAN 10 – CORPORATE
  - VLAN 20 – GUESTS
  - VLAN 30 – EXECUTIVE
  - VLAN 40 – DEVELOPMENT
  - VLAN 50 – ADMINISTRATION

---


## Screenshots

![Networking](https://github.com/DanielDSZ/Cisco/blob/main/Networking/Networking%20Basics/Project/DHPC%20Server%20e%20distribui%C3%A7%C3%A3o/DHPC%20Server%20e%20distribui%C3%A7%C3%A3o.png)


## Router Configuration

```bash
enable
configure terminal

interface g0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip helper-address 192.168.10.10
 exit

interface g0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip helper-address 192.168.10.10
 exit

interface g0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ip helper-address 192.168.10.10
 exit

interface g0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ip helper-address 192.168.10.10
 exit

interface g0/0.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
 ip helper-address 192.168.10.10
 exit

interface g0/0
 no shutdown

````
## Switch Configuring
### Trunk Ports
```bash
interface fa0/23
 switchport mode trunk
 exit

interface fa0/24
 switchport mode trunk
 exit
````
### Access Ports by VLAN
```bash
interface range fa0/1 - 3
 switchport mode access
 switchport access vlan 10
 exit

interface fa0/4
 switchport mode access
 switchport access vlan 20
 exit

interface fa0/5
 switchport mode access
 switchport access vlan 30
 exit

interface range fa0/6 - 9
 switchport mode access
 switchport access vlan 40
 exit

interface range fa0/10 - 16
 switchport mode access
 switchport access vlan 50
 exit

interface range fa0/17 - 22
 shutdown
 exit

interface fa0/23
 description Connects to DHCP Server
 switchport mode trunk
 exit

interface fa0/24
 description Connects to Router
 switchport mode trunk
 exit
````

## Notes
All VLANs receive dynamic IP addresses from the centralized DHCP server.

Trunk interfaces (fa0/23 and fa0/24) allow multiple VLANs to communicate between the switch, router, and server.

The network was designed for scalability and traffic segmentation, following best practices for corporate environments.
