Secure LLM Gateway with NGINX, Guardrails & Monitoring
Architecture

Architecture Diagram

<!-- ADD ARCHITECTURE IMAGE HERE --> <!-- You can place your architecture diagram image here -->

The architecture follows a layered security approach where the frontend, gateway, policy engine, and LLM backend are isolated and controlled through strict access rules.

Project Overview

This project demonstrates a secure, production-style architecture for hosting a Large Language Model (LLM) using Open WebUI, protected by NGINX Reverse Proxy, rate limiting, LLM guardrails, and security monitoring.

The goal of the project is to prevent common LLM attacks such as:

Prompt injection

Jailbreak attempts (DAN-style prompts)

Abuse via direct API access

Excessive request flooding (DoS / brute force)

Unauthorized backend access

The project is implemented using multiple virtual machines, simulating real-world attacker and defender environments.

Architecture Overview

High-level flow:

User / Attacker
      |
      v
[ NGINX Reverse Proxy ]
  - HTTPS (TLS)
  - Rate Limiting
  - Path Control
      |
      v
[ Open WebUI (Frontend) ]
      |
      v
[ LLM Gateway + Guardrails ]
      |
      v
[ Local LLM (TinyLlama) ]


Monitoring & Detection:

NGINX logs

Rate-limit logs

Guardrail violation logs

AlienVault OSSIM (SIEM)

Virtual Machines Used
VM	Purpose
VM1	Open WebUI + NGINX Reverse Proxy
VM2	LLM Backend + Guardrails
VM3	Attacker Machine (Kali Linux)
VM4	Monitoring (AlienVault OSSIM)
Technologies Used

NGINX – Reverse proxy, SSL termination, rate limiting

Open WebUI – Frontend UI for LLM interaction

Local LLM (TinyLlama) – Model inference

LLM Guardrails – Prompt validation & policy enforcement

curl – CLI-based testing

AlienVault OSSIM – Security monitoring & logs

Debian Linux – Server OS

VMware Workstation – Virtualization

Policy Engine

The project includes a policy engine implemented using Python files, responsible for enforcing security rules before requests reach the LLM.

Example files:

a.py – Implements the core policy engine logic

b.py – Additional policy validation rules

c.py – Request filtering and enforcement logic

These files work together to:

Validate incoming prompts

Enforce security policies

Block restricted or malicious requests

Allow only policy-compliant prompts to reach the LLM

The policy engine acts as a decision layer between the gateway and the LLM.

Security Controls Implemented
1 NGINX Reverse Proxy

Backend never exposed directly

Only /v1/chat/completions allowed

TLS enabled using internal CA

Path-based routing

NGINX hosting website properly


2 Rate Limiting (DoS Protection)

Per-IP request limits applied

Burst handling enabled

Excess requests blocked automatically

Rate limiting logs


Attack stopped due to rate limiting


Attacker testing rate limiting


3 LLM Guardrails (Prompt Injection Protection)

Guardrails block:

Prompt override attempts

Jailbreak commands

System instruction bypass attempts

Local guardrails blocking prompts


Attacker blocked by guardrails


4 CLI vs Web Access Control

CLI access via gateway works securely

Direct backend access is blocked

UI cannot bypass gateway rules

LLM working locally


Frontend tested locally


Attacker can get response only via allowed path


5 Open WebUI Backend Enforcement

Frontend-only access is blocked if backend is not properly routed.

Backend required error


Monitoring & Detection

All NGINX logs forwarded

Rate-limit violations logged

Guardrail violations logged

Integrated with AlienVault OSSIM

OSSIM Integration


Certificate Authority Setup


OWASP Top 10 for LLMs – Mapping
OWASP LLM Risk	Mitigation in Project
LLM01: Prompt Injection	Guardrails block override prompts
LLM02: Insecure Output Handling	JSON-only responses
LLM03: Training Data Poisoning	Local trusted model
LLM04: Model Denial of Service	NGINX rate limiting
LLM05: Supply Chain Vulnerabilities	Local controlled deployment
LLM06: Sensitive Data Exposure	Backend isolation
LLM07: Insecure Plugin Design	No external plugins
LLM08: Excessive Agency	No system-level execution
LLM09: Over-Privileged Access	Strict path control
LLM10: Insufficient Monitoring	OSSIM + logs
Key Outcomes

Backend never directly exposed

Prompt injection attempts blocked

DoS attacks mitigated

Secure CLI & UI access

Full visibility through logs

OWASP-aligned LLM security

Why This Project Matters (Interview Ready)

This project demonstrates:

Real-world LLM security

DevSecOps mindset

Zero-trust architecture

Hands-on OWASP LLM Top 10 understanding

Enterprise-style monitoring & logging

Future Improvements

Add WAF rules

JWT-based authentication

Per-user quotas

Advanced anomaly detection

Model response filtering

Author

Yash Nilkanth Patil
Security | DevSecOps | LLM Security Enthusiast