class SecurityScanner:
    OWASP_PATTERNS = {
        "SQLi": r"(SELECT|UPDATE|DELETE).*WHERE.*'?\\+-",
        "XSS": r"(<script|alert\(|document\.cookie)",
        "BufferOverflow": r"memcpy\(|strcpy\("
    }

    def scan_code(self, code: str) -> dict:
        report = {"vulnerabilities": []}
        for pattern_name, regex in self.OWASP_PATTERNS.items():
            if re.search(regex, code, re.IGNORECASE):
                report["vulnerabilities"].append({
                    "type": pattern_name,
                    "severity": "CRITICAL",
                    "recommendation": f"Use parameterized queries instead of {pattern_name}"
                })
        return report