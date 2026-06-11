# HolbertonSchool.com – Passive Reconnaissance Report (Shodan)

## Scope
This report documents passive reconnaissance findings for the domain **holbertonschool.com**, collected using **Shodan**.  
No active scanning or intrusive techniques were used.

---

## 1. Methodology

The following passive reconnaissance techniques were applied:

- Shodan domain and hostname search
- Shodan IP and organization correlation
- Technology fingerprinting via Shodan banners
- DNS-based subdomain correlation (from Shodan results)

All data was collected from publicly available sources indexed by Shodan.

---

## 2. IP Ranges Associated with holbertonschool.com

Based on Shodan results, the infrastructure of **holbertonschool.com** is distributed across multiple cloud providers and CDNs.

### Identified IP Addresses / Ranges

| IP Address | Provider | Notes |
|------------|---------|------|
| 99.83.190.102 | Amazon AWS | Main domain |
| 75.2.70.75 | Amazon AWS | Load balanced endpoint |
| 63.35.51.142 | Amazon AWS (CloudFront) | www / webflow |
| 52.85.96.0/24 | Amazon AWS (CloudFront) | Static assets |
| 18.66.196.0/24 | Amazon AWS | Staging assets |
| 13.36.0.0/16 | Amazon AWS (EU) | Application services |
| 104.16.0.0/12 | Cloudflare | Support / help services |

> Note: CloudFront and Cloudflare IPs may rotate dynamically.

---

## 3. Subdomains Identified via Shodan

Shodan indexed the following subdomains:

- holbertonschool.com
- www.holbertonschool.com
- apply.holbertonschool.com
- blog.holbertonschool.com
- support.holbertonschool.com
- assets.holbertonschool.com
- read.holbertonschool.com
- v1.holbertonschool.com
- v2.holbertonschool.com
- v3.holbertonschool.com
- staging-apply.holbertonschool.com
- beta.holbertonschool.com
- alpha.holbertonschool.com
- webflow.holbertonschool.com

---

## 4. Technologies and Frameworks Identified

Using Shodan service banners and fingerprints, the following technologies were observed across subdomains.

### Web Servers / Infrastructure

- **Amazon AWS**
- **Amazon CloudFront**
- **Cloudflare**
- **Nginx**
- **Apache**

---

### Frameworks and Platforms

- **Webflow** (Marketing and landing pages)
- **Ruby on Rails** (Application backend)
- **Discourse** (Forum-related services)
- **Zendesk** (Support portal)
- **WordPress** (Blog services)

---

### Security & Networking

- TLS/SSL enabled across all indexed services
- SPF records configured for email security
- CDN-based DDoS mitigation (Cloudflare / CloudFront)

---

## 5. Observations

- Infrastructure is heavily cloud-based (AWS).
- CDN usage indicates scalability and traffic optimization.
- Separation between production, staging, and beta environments is observable.
- No exposed critical services (SSH, databases) were indexed by Shodan.

---

## 6. Conclusion

The domain **holbertonschool.com** demonstrates a mature and distributed cloud infrastructure with strong reliance on managed services and CDNs.  
All information was collected passively using Shodan, without any active probing.

This reconnaissance phase provides valuable insight for further security assessments while maintaining a non-intrusive approach.

---

## 7. Disclaimer

This report was created strictly for educational and authorized reconnaissance purposes as part of a cybersecurity training project.
