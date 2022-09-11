# obd-scanner


Small program built on top of python-OBD to allow manual querying of OBD2 connections.

## Requirements
- Python 3.9 (Some python-OBD packages appear to break on 3.10 due to changes in the 'collections' module, eg. Pint)
- OBD2 adapter capable of pairing to computer through Bluetooth or USB
- Ubuntu or other Linux distribution with the following packages:
  - bluetoothctl
  - rfcomm

## 1. Pair Bluetooth
```
sudo bluetoothctl
[bluetooth]# scan on
[bluetooth]# devices
[bluetooth]# pair <insert OBD2 device MAC>
[bluetooth]# trust <insert OBD2 device MAC>
[bluetooth]# connect <insert OBD2 device MAC>
[bluetooth]# exit
```

## 2. Bind OBD2 device to Serial Port
```
sudo rfcomm bind 0 <insert OBD2 device MAC> \# 
```
This should result in a connection on /dev/rfcomm0 (hardcoded in main.py) -- use rfcomm -a to confirm


## 3. Run main.py
```
python3 main.py
```

Program first attempts to confirm connection. You should see it initialize and check all 'AT' commands:
```
[obd.obd] ======================= python-OBD (v0.7.1) =======================
[obd.obd] Explicit port defined
[obd.elm327] Initializing ELM327: PORT=/dev/rfcomm0 BAUD=auto PROTOCOL=auto
[obd.elm327] Response from baud 38400: b'\x7f\x7f\r?\r\r>'
[obd.elm327] Choosing baud 38400
[obd.elm327] write: b'ATZ\r'
[obd.elm327] wait: 1 seconds
[obd.elm327] read: b'ATZ\r\r\rELM327 v1.5\r\r>'
[obd.elm327] write: b'ATE0\r'
...
```
