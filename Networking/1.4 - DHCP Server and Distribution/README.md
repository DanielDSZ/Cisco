# Office Network (Cisco Packet Tracer) — VLAN Segmentation + Centralized DHCP + Guest ACL 

This project simulates a small office network in **Cisco Packet Tracer** featuring:

- **VLAN segmentation** by department
- **Router-on-a-stick** inter-VLAN routing (802.1Q subinterfaces)
- **Centralized DHCP** (single server distributing leases to all VLANs)
- Two Wi‑Fi networks mapped to different VLANs:
  - `Company` (Corporate Wi‑Fi) → **VLAN 30**
  - `Company-Guest` (Guest Wi‑Fi) → **VLAN 20**
- **ACL policy** to isolate Guest users from internal networks (ACL 1)

---

## 1) Topology Overview

**Core devices**
- **R1 (Router)**: Inter-VLAN routing with subinterfaces (802.1Q).
- **SW0 (Main/Distribution Switch)**: VLAN database, trunk to router, access ports to DHCP server and APs, uplinks to access switches.
- **Server0**: DHCP Server (static IP in VLAN 10).
- **SW1 (Access Switch 01)**: ADMINISTRATION access switch (VLAN 40).
- **SW2 (Access Switch 02)**: DEVELOPMENT access switch (VLAN 50).
- **AP-COR**: SSID `Company` → VLAN 30.
- **AP-GUEST**: SSID `Company-Guest` → VLAN 20.

**Known cabling (confirmed)**
- R1 `Gi0/0` ↔ SW0 `Fa0/24` (**TRUNK**)
- Server0 ↔ SW0 `Fa0/23` (**ACCESS VLAN 10**)

> Note: AP and access-switch uplink port numbers can vary. Use `show cdp neighbors` on SW0 to confirm exact ports.

![App Screenshot](https://github.com/DanielDSZ/Cisco/blob/main/Networking/1.4%20-%20DHCP%20Server%20and%20Distribution/docs/DHCP%20-%20Server%20and%20Distribution.png)
---

## 2) VLANs and IP Addressing Plan

All VLANs use `/24` (**255.255.255.0**).

| VLAN | Name            | Subnet            | Default Gateway   |
|------|------------------|------------------|------------------|
| 10   | IT              | 172.16.10.0/24    | 172.16.10.1      |
| 20   | GUESTS          | 172.16.20.0/24    | 172.16.20.1      |
| 30   | CORPORATE       | 172.16.30.0/24    | 172.16.30.1      |
| 40   | ADMINISTRATION  | 172.16.40.0/24    | 172.16.40.1      |
| 50   | DEVELOPMENT     | 172.16.50.0/24    | 172.16.50.1      |

### DHCP Server (Server0)
- **Static IP**: `172.16.10.10`
- **Mask**: `255.255.255.0`
- **Default Gateway**: `172.16.10.1`
- **DNS in DHCP pools**: `8.8.8.8`

---

## 3) Wireless Design (SSIDs → VLANs)

Two separated Wi‑Fi networks:

- **Corporate Wi‑Fi**
  - SSID: `Company`
  - VLAN: **30 (CORPORATE)**

- **Guest Wi‑Fi**
  - SSID: `Company-Guest`
  - VLAN: **20 (GUESTS)**

This design uses **one AP per VLAN/SSID** connected via **ACCESS ports**, so each AP bridges its wireless clients into the intended VLAN.

---

## 4) Router Configuration (R1) — Router-on-a-Stick + DHCP Relay

R1 provides inter-VLAN routing via subinterfaces on `Gi0/0`.  
VLANs 20/30/40/50 use DHCP relay (`ip helper-address`) to forward DHCP broadcasts to the centralized server in VLAN 10.

```cisco
enable
conf t

interface g0/0
 no shutdown

! VLAN 10 - IT
interface g0/0.10
 encapsulation dot1Q 10
 ip address 172.16.10.1 255.255.255.0

! VLAN 20 - GUESTS
interface g0/0.20
 encapsulation dot1Q 20
 ip address 172.16.20.1 255.255.255.0
 ip helper-address 172.16.10.10

! VLAN 30 - CORPORATE
interface g0/0.30
 encapsulation dot1Q 30
 ip address 172.16.30.1 255.255.255.0
 ip helper-address 172.16.10.10

! VLAN 40 - ADMINISTRATION
interface g0/0.40
 encapsulation dot1Q 40
 ip address 172.16.40.1 255.255.255.0
 ip helper-address 172.16.10.10

! VLAN 50 - DEVELOPMENT
interface g0/0.50
 encapsulation dot1Q 50
 ip address 172.16.50.1 255.255.255.0
 ip helper-address 172.16.10.10

end
wr
```

---

## 5) Main Switch Configuration (SW0) — VLANs + Trunk + Access Ports

### 5.1 VLAN Database

```cisco
enable
conf t

vlan 10
 name IT
vlan 20
 name GUESTS
vlan 30
 name CORPORATE
vlan 40
 name ADMINISTRATION
vlan 50
 name DEVELOPMENT

end
wr
```

### 5.2 Trunk to Router (Fa0/24)

```cisco
conf t
interface fa0/24
 description TRUNK_TO_R1_G0/0
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50
end
wr
```

### 5.3 DHCP Server Port (Fa0/23) — MUST be ACCESS VLAN 10

Packet Tracer Server-PT typically does **not** tag 802.1Q, therefore the server must be connected to an **ACCESS** port.

```cisco
conf t
interface fa0/23
 description DHCP_SERVER_Server0
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
end
wr
```

### 5.4 Access Point Ports (AP-COR and AP-GUEST)

```cisco
conf t
! Corporate AP (SSID: Company) -> VLAN 30
interface fa0/3
 description AP_CORP_SSID_Company
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast

! Guest AP (SSID: Company-Guest) -> VLAN 20
interface fa0/4
 description AP_GUEST_SSID_Company-Guest
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
end
wr
```

### 5.5 Uplinks to Access Switches (SW1 and SW2)

This lab uses a simple “dedicated access switch per VLAN” approach:

- SW1 carries only **VLAN 40**
- SW2 carries only **VLAN 50**

```cisco
conf t
! Uplink to SW1 (ADMIN)
interface fa0/1
 description UPLINK_TO_SW1_ADMIN
 switchport mode access
 switchport access vlan 40

! Uplink to SW2 (DEV)
interface fa0/2
 description UPLINK_TO_SW2_DEV
 switchport mode access
 switchport access vlan 50
end
wr
```

---

## 6) Access Switch 01 (SW1) — ADMINISTRATION (VLAN 40)

```cisco
enable
conf t

vlan 40
 name ADMINISTRATION

interface <uplink-to-SW0>
 switchport mode access
 switchport access vlan 40

interface range fa0/1 - 24
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast

end
wr
```

---

## 7) Access Switch 02 (SW2) — DEVELOPMENT (VLAN 50)

```cisco
enable
conf t

vlan 50
 name DEVELOPMENT

interface fa0/2
 switchport mode access
 switchport access vlan 50

end
wr
```

---

## 8) DHCP Server Configuration (Server0)

### 8.1 Static IP (Desktop > IP Configuration)
- IP Address: **172.16.10.10**
- Subnet Mask: **255.255.255.0**
- Default Gateway: **172.16.10.1**

### 8.2 DHCP Pools (Services > DHCP)

Configured pools (as implemented in the lab):

| Pool Name        | Default Gateway | DNS     | Start IP Address | Subnet Mask     | Max Users |
|------------------|-----------------|---------|------------------|-----------------|----------|
| DEVELOPMENT      | 172.16.50.1     | 8.8.8.8 | 172.16.50.0      | 255.255.255.0   | 20       |
| ADMINISTRATION   | 172.16.40.1     | 8.8.8.8 | 172.16.40.0      | 255.255.255.0   | 20       |
| CORPORATE        | 172.16.30.1     | 8.8.8.8 | 172.16.30.0      | 255.255.255.0   | 10       |
| GUESTS           | 172.16.20.1     | 8.8.8.8 | 172.16.20.0      | 255.255.255.0   | 100      |
| IT               | 172.16.10.1     | 8.8.8.8 | 172.16.10.0      | 255.255.255.0   | 10       |

> Best practice note (real-world): starting DHCP at `.0` is not used in production because `.0` is the network address and `.1` is usually the gateway. In real networks, use `.50` or `.100` onward. Packet Tracer may still function depending on how it handles the start value.

---

## 9) ACL Policy — Guest Isolation (ACL 1)

Goal: **Guests (VLAN 20)** must NOT access internal office VLANs (10/30/40/50), while still allowing DHCP and general outbound traffic (e.g., Internet).

This ACL is applied **inbound** on the VLAN 20 subinterface (`g0/0.20 in`).

```cisco
enable
conf t

ip access-list extended GUESTS_IN
 remark --- Allow DHCP (client -> relay on router) ---
 permit udp any eq 68 any eq 67
 remark --- Allow DNS (optional, but typical) ---
 permit udp any any eq 53
 permit tcp any any eq 53
 remark --- Block access to internal VLANs ---
 deny ip any 172.16.10.0 0.0.0.255
 deny ip any 172.16.30.0 0.0.0.255
 deny ip any 172.16.40.0 0.0.0.255
 deny ip any 172.16.50.0 0.0.0.255
 remark --- Allow everything else ---
 permit ip any any
exit

interface g0/0.20
 ip access-group GUESTS_IN in

end
wr
```

### Quick validation
- A guest client should receive an IP in **172.16.20.0/24**
- Guest can ping its own gateway: `ping 172.16.20.1`
- Guest should NOT reach internal hosts (e.g., DHCP server): `ping 172.16.10.10` **should fail**
- Router counters:
```cisco
show access-lists
show ip interface g0/0.20
```

---

## 10) Verification Commands

### Switch (SW0)
```cisco
show vlan brief
show interfaces trunk
show mac address-table dynamic
show cdp neighbors
```

### Router (R1)
```cisco
show ip interface brief
show run | section interface g0/0
show access-lists
```

### Clients
- Set the NIC to **DHCP**
- Confirm correct subnet per VLAN
- Ping the VLAN gateway (example VLAN 30): `ping 172.16.30.1`
- (Before ACL) ping DHCP server from VLAN 20 should work; (After ACL) it should fail.

---

## 11) Next Improvements (Optional)

- Add an “Internet” router + NAT for realistic guest browsing tests.
- Apply additional ACLs (e.g., restrict which VLANs can access Server0).
- Add a Management VLAN + SSH for switches.
- Implement DHCP Snooping + Dynamic ARP Inspection (DAI) for Layer 2 security.

---

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

