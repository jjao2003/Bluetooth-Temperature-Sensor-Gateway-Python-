# Bluetooth Temperature Sensor Gateway (Python)

## Project Overview

This project demonstrates Bluetooth socket communication between a simulated sensor (client) and a gateway (server) using Python. The client simulates a temperature sensor and periodically sends temperature values to the server over a Bluetooth RFCOMM connection. The server receives the data and displays it in the terminal.

The purpose of the project is to demonstrate how Bluetooth sockets can be used for communication between nearby devices in an IoT-style system.

---

## Technologies Used

- Python 3
- Bluetooth RFCOMM socket communication
- Socket programming

No external Python libraries are required.

---

## Project Structure

```
bluetooth-temperature-sensor/
│
├── server.py
├── client.py
├── requirements.txt
├── README.md
└── screenshots/
     ├── server_running.png
     └── client_running.png
```

### File Descriptions

**server.py**  
Runs the Bluetooth gateway server. It waits for incoming Bluetooth connections and receives temperature data from the client.

**client.py**  
Simulates a Bluetooth temperature sensor that sends temperature values to the server every 5 seconds.

**requirements.txt**  
Lists project requirements (Python 3).

**screenshots/**  
Contains screenshots showing the program running.

---

## System Architecture

The system consists of two components:

1. Bluetooth Sensor (Client)
2. Bluetooth Gateway (Server)

The client sends simulated temperature readings to the server via Bluetooth.

```
Temperature Sensor (Client)
        |
        | Bluetooth RFCOMM
        |
Gateway Server (Python)
        |
Display Received Temperature
```

---

## How the Program Works

1. The server starts and waits for a Bluetooth connection.
2. The client connects to the server using the server's Bluetooth MAC address.
3. The client generates a simulated temperature value.
4. The client sends the temperature value to the server every 5 seconds.
5. The server receives the data and prints it to the terminal.

---

## Running the Project

### Step 1: Start the Server

Run the server script first.

```
python server.py
```

Expected output:

```
Bluetooth server started
Waiting for connection...
```

---

### Step 2: Run the Client

Open another terminal and run:

```
python client.py
```

Expected output:

```
Connected to Bluetooth server
Sent: Temperature: 24.3 C
Sent: Temperature: 25.1 C
Sent: Temperature: 23.8 C
```

---

### Step 3: Server Receives Data

The server terminal will display the received data.

```
Connected to: ('client-device-address', 1)

Received: Temperature: 24.3 C
Received: Temperature: 25.1 C
Received: Temperature: 23.8 C
```

---

## Screenshots

### Server Running

![Server Output](screenshots/server_running.png)

### Client Running

![Client Output](screenshots/client_running.png)

---

## Answer: What is the difference between Bluetooth socket communication and WiFi socket communication in practice?

Bluetooth socket communication and WiFi socket communication both use socket programming, but they differ in several practical aspects.

Bluetooth communication is designed for short-range connections between nearby devices. It typically operates within a range of about 10–100 meters and has lower data transfer speeds compared to WiFi. Bluetooth sockets usually use the RFCOMM protocol, which emulates serial communication between paired devices. Bluetooth is commonly used for communication between sensors, wearable devices, and embedded systems.

WiFi socket communication uses TCP/IP networking over a wireless network. Devices communicate using IP addresses and can connect through local networks or the internet. WiFi provides higher data transfer speeds and a much larger communication range.

In practice, Bluetooth is used mainly for **direct device-to-device communication over short distances**, while WiFi is used for **network communication and internet connectivity**.

---

## Example Use Cases

### Bluetooth Communication
- IoT sensors
- Wearable devices
- Smart home devices
- Device-to-device communication

### WiFi Communication
- Web applications
- Cloud services
- Network servers
- Internet communication

---

## Conclusion

This project demonstrates a simple Bluetooth communication system using Python socket programming. A simulated temperature sensor sends data to a Bluetooth gateway server, illustrating how short-range device communication can be implemented using Bluetooth RFCOMM sockets.

The project shows how Bluetooth sockets can be applied in basic IoT communication between nearby devices.
