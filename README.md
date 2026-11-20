# Network Watchdog

I'm building a home network security tool in Python, one stage at a time. The goal is to know what's on my network and what's open before someone else finds out first.

## Stage 1: Port Scanner (done)

This scanner checks if common ports are open on an IP address you type in.

I picked these ports on purpose:

- 22 (SSH) is remote login. If it's open, it's one of the first things attackers try to brute force.
- 80 (HTTP) is regular web traffic with no encryption.
- 443 (HTTPS) is encrypted web traffic.
- 8000 is a common port for dev servers, and people leave it open by accident all the time.

How it works: I used Python's socket library since it has the networking tools to send and receive data. The script asks for an IP, then loops through each port and tries to connect. I set a half second timeout so it doesn't hang on closed ports. If the connection goes through, it prints OPEN. If not, it prints closed.

To run it:

    python3 scanner.py

Only scan devices you own or have permission to scan.

## Stage 2: Device Discovery (in progress)

Next I'm finding every device connected to my network so I can spot anything that shouldn't be there.
