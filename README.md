 ICS / OT Security – Fake Factory Attack Detection

This project simulates a fake industrial factory using Conpot honeypot
to emulate real ICS/OT protocols such as Modbus.
It demonstrates real-world cyber attacks against industrial systems and
implements monitoring, detection, and alerting using the PLG stack
(Promtail, Loki, Grafana).

The attacks include Modbus write operations on TCP port 502 and
Denial-of-Service (DoS) attacks targeting Modbus services, with log-based
detection and alerting.

 Project Architecture

Conpot → Fake ICS/OT factory (Modbus, SNMP, etc.)

Attacker Machine → Modbus write & DoS attacks

Promtail → Collects Conpot logs

Loki → Stores logs

Grafana → Visualization & alerting

⚙️ Part 1: Install Docker & Run Conpot Honeypot

🛡️ Part 2: Monitoring & Detection with PLG Stack


🚨 Attacks Implemented

Modbus write attacks on TCP port 502

DoS attacks targeting Modbus services

Traffic analysis using Wireshark

Log-based detection and alerting
