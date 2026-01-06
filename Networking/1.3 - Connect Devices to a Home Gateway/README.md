# Enterprise Smart House (Cisco Packet Tracer)

A small smart home lab built in **Cisco Packet Tracer** using proper network segmentation and centralized IoT management (no Home Gateway).  
IoT devices connect through dedicated Wi‑Fi/AP infrastructure and are **registered to a Registration Server** for remote monitoring and control.

---

## What this project demonstrates

- **Segmentation** with VLANs (Users vs IoT)
- **Inter-VLAN routing** using *Router-on-a-Stick* (802.1Q trunk + subinterfaces)
- **Centralized IoT management** using a **Registration Server** (Remote Server mode)
- **Wi‑Fi separation** using two APs (one per VLAN/SSID)
- **DHCP** for both VLANs (served by the router)
- *(Optional)* **ACL hardening** to reduce IoT lateral movement

---

## Topology (high level)

**Core:**
- 1× Router (e.g., 2911) – default gateways for VLANs, DHCP, inter-VLAN routing
- 1× Switch (e.g., 2960) – VLANs + trunk to router
- 2× Access Points – one SSID for Users and one SSID for IoT
- 1× Server-PT – IoT **Registration Server** (and optionally DNS)

**Endpoints:**
- Users: Laptop/PC (VLAN 10)
- IoT: Smart devices (fan, door, garage, etc.) (VLAN 30)

> Tip: Export a Packet Tracer screenshot and save it as `assets/topology.png` so the repository has a visual diagram.

---

## IP plan

| Network | VLAN | Subnet | Default Gateway |
|---|---:|---|---|
| Users | 10 | `192.168.10.0/24` | `192.168.10.1` |
| IoT | 30 | `192.168.30.0/24` | `192.168.30.1` |

**Server**
- Registration Server: `192.168.10.10/24`
- GW: `192.168.10.1`

**DHCP**
- Users pool (example): `192.168.10.21–192.168.10.254`
- IoT pool (example): `192.168.30.21–192.168.30.254`

---

## Wi‑Fi SSIDs

- **Users SSID:** `USER-HOME` (WPA2-Personal)
- **IoT SSID:** `IOT-HOME` (WPA2-Personal)

Because Packet Tracer APs can vary by model/version, this design uses **two APs** to keep the VLAN mapping simple and reliable:
- AP-Users is connected to an **access port in VLAN 10**
- AP-IoT is connected to an **access port in VLAN 30**

---
## Build steps (configuration summary)

### 1) Cabling

- Router `G0/0` ↔ Switch `F0/1` (trunk)
- AP-Users ↔ Switch `F0/2` (access VLAN 10)
- AP-IoT ↔ Switch `F0/3` (access VLAN 30)
- Server ↔ Switch `F0/4` (access VLAN 10)

---

### 2) Switch (2960) — VLANs + trunk + access ports

```bash
enable
conf t

vlan 10
 name USERS
vlan 30
 name IOT
exit

interface fa0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,30
exit

interface fa0/2
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
exit

interface fa0/3
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
exit

interface fa0/4
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
exit

end
wr
```

---

### 3) Router — Router-on-a-Stick (802.1Q subinterfaces)

```bash
enable
conf t

interface g0/0
 no shutdown
exit

interface g0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit

interface g0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
exit

end
wr
```

---

### 4) Router — DHCP for Users + IoT

```bash
conf t
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.30.1 192.168.30.20

ip dhcp pool USERS
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.10
exit

ip dhcp pool IOT
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 192.168.10.10
exit

end
wr
```

---

### 5) Server-PT — Registration Server

1. **Desktop → IP Configuration**
   - IP: `192.168.10.10`
   - Mask: `255.255.255.0`
   - Gateway: `192.168.10.1`

2. **Services → IoT / Registration**  
   - Turn the service **ON**
   - Create at least one user (username/password)

> Optional: Enable DNS and create a record like `home.local` → `192.168.10.10`.

---

### 6) Access Points — SSIDs + security

AP-Users
- SSID: `HOME-USERS`
- Security: **WPA2-Personal**
- Strong password

AP-IoT
- SSID: `HOME-IOT`
- Security: **WPA2-Personal**
- Strong password

---

## Connecting and registering devices

### Users (Laptop/PC)
1. Connect to SSID `HOME-USERS`
2. Verify it receives an address in `192.168.10.0/24`
3. Test:
   - `ping 192.168.10.1`
   - `ping 192.168.10.10`

### IoT devices
For each IoT device:
1. Connect to SSID `HOME-IOT`
2. Verify it receives an address in `192.168.30.0/24`
3. In the device settings:
   - Find **IoT Server**
   - Select **Remote Server** (instead of Home Gateway)
   - Set server IP to `192.168.10.10`
   - Log in with the Registration Server credentials
4. Confirm the device appears in the Registration Server dashboard

---

## Optional hardening: ACL to limit IoT lateral movement

Goal:
- Allow IoT → Registration Server (`192.168.10.10`)
- Block IoT → Users subnet (`192.168.10.0/24`)
- Allow other traffic as needed for your lab

```bash
conf t
ip access-list extended IOT_IN
 permit ip 192.168.30.0 0.0.0.255 host 192.168.10.10
 deny   ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
 permit ip 192.168.30.0 0.0.0.255 any
exit

interface g0/0.30
 ip access-group IOT_IN in
exit
end
wr
```

Verification:
- From an IoT device: ping `192.168.10.10` should work
- From an IoT device: ping a Users client (`192.168.10.x`) should fail

---

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Notes

- This lab is meant for learning and demonstration: segmentation, centralized device management, and basic network hardening.
- Packet Tracer feature availability can vary depending on the version and device models used.

---



## Licença

[MIT](https://choosealicense.com/licenses/mit/)

