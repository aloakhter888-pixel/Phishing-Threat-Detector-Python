# AI & Logic-Based Phishing Threat Detector

### Project Overview
A lightweight Python application designed to analyze URL structures and identify potential phishing/malicious links.

### How the Analysis Works (মেথডোলজি):
1. **Protocol Verification:** Checks whether the URL uses secure **HTTPS** or insecure **HTTP**.
2. **Heuristic Keyword Filtering:** Scans the URL string for common phishing keywords (e.g., login, verify, update-bank, free-gift).
3. **Direct IP Address Detection:** Checks if a direct IP address is being used instead of a standard domain name.
4. **Automated Risk Scoring:** Evaluates findings to classify the link into High Risk, Medium Risk, or Low Risk.
