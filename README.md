# jailedLFI


# LFI-Scanner

## 📌 Overview
LFI-Scanner is an advanced Local File Inclusion (LFI) vulnerability scanner that automates file inclusion testing and includes various bypass techniques. It supports both Linux and Windows targets, offering multiple encoding options to evade security mechanisms.

## 🚀 Features
- **Automatic LFI Detection**: Scans URLs for LFI vulnerabilities.
- **Bypass Techniques**:
  - Base64 Encoding
  - URL Encoding
  - Null Byte Injection
  - Double Encoding
- **Custom Payload Support**: Add your own payloads for more flexibility.
- **Windows & Linux Support**: Predefined payloads for both operating systems.
- **Multi-threaded Scanning**: Faster testing with parallel requests.

## 🔧 Installation
```bash
git clone https://github.com/youwerejailed/LFI-Scanner.git
cd LFI-Scanner
pip install -r requirements.txt
```

## ⚡ Usage
```bash
python lfi_scanner.py -u "http://target.com/vuln.php?file=../../etc/passwd"
```

### 🔹 Advanced Usage
```bash
python lfi_scanner.py -u "http://target.com/vuln.php?file=../../etc/passwd" --bypass base64 --threads 10
```

## 📜 Payloads
The scanner includes common LFI payloads and bypass techniques. You can modify or extend them in the `payloads.txt` file.

## 🛠️ To-Do
- Add SSH log file injection techniques.
- Implement reverse shell payloads.
- Improve detection with more encoding variations.

## ⚠️ Disclaimer
This tool is intended for **educational and authorized security testing** purposes only. **Use it responsibly!**

---
Made with ❤️ by [youwerejailed](https://github.com/youwerejailed)
