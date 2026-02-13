# Script to use cheap KCEVE KC-KVM401CY with pikvm over RS232

## Hardware Setup

Connect the KVM switch with a USB to RS232 cable to pikvm

## Install script and config file

Login as root to your pikvm

Make filesystem writeable
```
rw
```

Clone git repository
```
git clone https://github.com/madon/pikvm-kv401.git
```

Copy files
```
cd pikvm-kv401
cp kv401.py /usr/local/bin/
cp kv401.yaml /etc/kvmd/override.d/
```

Restart kvmd
```
systemctl restart kvmd
```

Make filesystem read-only again
```
ro
```

## check functionality

Now you should see a GPIO menu on the pikvm webinterface where you can switch the 4 inputs of the KVM401.
