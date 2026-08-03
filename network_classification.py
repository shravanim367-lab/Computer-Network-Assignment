devices = {
    "Switch": {
        "Layer": "Layer 2 (Data Link Layer)",
        "Function": "Connects devices within a LAN using MAC addresses."
    },
    "Router": {
        "Layer": "Layer 3 (Network Layer)",
        "Function": "Routes packets between different networks using IP addresses."
    },
    "Bridge": {
        "Layer": "Layer 2 (Data Link Layer)",
        "Function": "Connects and filters traffic between LAN segments."
    },
    "Access Point": {
        "Layer": "Layer 2 (Data Link Layer)",
        "Function": "Provides wireless connectivity to devices."
    }
}

media = {
    "Twisted Pair Cable": "Copper cable used in LAN communication.",
    "Coaxial Cable": "Used for cable television and broadband networks.",
    "Optical Fiber": "High-speed transmission over long distances.",
    "Wireless": "Uses radio waves for communication."
}

print("=" * 70)
print("NETWORK DEVICE CLASSIFICATION REPORT")
print("=" * 70)

print("\nNetwork Devices:\n")

for device, info in devices.items():
    print(f"Device      : {device}")
    print(f"OSI Layer   : {info['Layer']}")
    print(f"Primary Use : {info['Function']}")
    print("-" * 70)

print("\nTransmission Media:\n")

for medium, desc in media.items():
    print(f"{medium:<20} : {desc}")