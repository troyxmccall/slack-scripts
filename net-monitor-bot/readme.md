# Net Monitor

This Python script monitors your local network and notifies you of known hosts joining and leaving the network on everybody's favourite chat tool: Slack. Yet another good use case for a Raspberry Pi.

The network scan occurs every 60 seconds and the program is required to run as root to capture MAC-addresses of the network devices.

## Installation

```bash
// Install Python modules
pip install requests
pip install python-nmap

// Discover hosts on your local network
// and gather their MAC address for the config
arp -a
// or
sudo nmap -sn 192.168.1.0/24

// Setup the config file
cp example.json config.json
vim config.json
```

If you wish to run the script on system start you can use the prodvided init.d script (Linux only). Make sure you modify the init.d script to fit your needs (correct user and paths).
```bash
chmod +x initd.sh
sudo cp initd.sh /etc/init.d/net-monitor
touch /var/log/net-monitor.log && chown root /var/log/net-monitor.log # CHANGE USER HERE
update-rc.d net-monitor defaults
service \"net-monitor\" start"
```

## Execution

Make sure to run the program as root in order to collect MAC addresses from the network interface.

```bash
sudo python net-monitor.py
```

## Requirements

Make sure you have the following installed and running on your system:
- Python (only tested version 2.7)
- NMap

## Slack Integration

In order to get notified in Slack you have to setup a webhook. Follow the instructions on the Slack website: [https://yourteam.slack.com/services/new/incoming-webhook](https://yourteam.slack.com/services/new/incoming-webhook)
Enter the resulting webhhok URL in the config file.

## Disclaimer & License

Depending on your country of origin, scanning a network might be legal or not. Please research your local laws first. Get the permission of your network administrator and other users on the network before using this script.
