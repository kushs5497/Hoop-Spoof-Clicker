# Referral Click Automation

## Overview
This project is designed to automate referral clicks for various platforms. While the example URL used in the code is for Hoop, the project is not limited to Hoop and can be adapted for other referral systems. The automation leverages Selenium for browser interactions and proxy management to simulate clicks.

## Features
- Automated browser interactions using Selenium.
- Proxy rotation for anonymity.
- Configurable refresh and click counts.
- VPN integration for location-based testing.

## Requirements
- Python 3.7+
- Selenium
- ChromeDriver
- Mullvad VPN (optional, for location-based testing)
- Proxy list API

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure ChromeDriver is installed. The project uses `chromedriver_autoinstaller` to automatically install the latest version.
4. Configure your proxy list in the `proxies/` directory or use the `proxy.py` script to fetch proxies.

## Usage
1. Update the referral URL in `auto_ref.py`:
   ```python
   link = 'https://example.com/referral-link'
   ```
2. Run the script:
   ```bash
   python auto_ref.py
   ```

## Customization
- **Referral URL**: Replace the `link` variable in `auto_ref.py` with your desired referral URL.
- **Proxy Management**: Use `proxy.py` to fetch and rotate proxies.
- **VPN Integration**: Ensure Mullvad VPN is installed and configured for location-based testing.

## Screenshots
Add screenshots of the project in action here:

![Screenshot 1](path/to/screenshot1.png)
![Screenshot 2](path/to/screenshot2.png)

## Disclaimer
This project is intended for educational purposes only. Ensure compliance with the terms and conditions of the referral platform you are using. Misuse of this tool may result in account suspension or legal consequences.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.
