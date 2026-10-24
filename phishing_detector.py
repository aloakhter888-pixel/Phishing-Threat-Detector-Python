# Phishing Link & Suspicious Pattern Detector
# Developed by Sukhi Akhter

suspicious_keywords = [
    "login", "verify", "update-bank", "free-gift", 
    "secure-account", "paypal", "signin", "banking"
]

def check_phishing_link(url):
    print(f"\n[Analyzing URL]: {url}")
    threat_score = 0
    
    # Check 1: Insecure Protocol (HTTP instead of HTTPS)
    if url.startswith("http://"):
        print("[-] Warning: Uses insecure HTTP protocol.")
        threat_score += 2
    elif not url.startswith("https://"):
        print("[-] Warning: Missing SSL certificate protocol.")
        threat_score += 1

    # Check 2: Suspicious Keywords in URL
    found_keywords = [word for word in suspicious_keywords if word in url.lower()]
    if found_keywords:
        print(f"[-] Suspicious keywords detected: {', '.join(found_keywords)}")
        threat_score += len(found_keywords) * 2

    # Check 3: IP Address used instead of Domain
    domain_part = url.split("//")[-1].split("/")[0]
    if domain_part.replace(".", "").isdigit():
        print("[-] Suspicious: Direct IP address detected in URL.")
        threat_score += 3

    # Final Result Assessment
    print("\n--- Assessment Result ---")
    if threat_score >= 3:
        return "HIGH RISK: Potential Phishing Threat Detected!"
    elif threat_score > 0:
        return "MEDIUM RISK: Proceed with Caution."
    else:
        return "LOW RISK: URL appears structure-wise Safe."

# Example Usage
if __name__ == "__main__":
    test_url = input("Enter URL to scan: ")
    result = check_phishing_link(test_url)
    print(f"Result: {result}")
