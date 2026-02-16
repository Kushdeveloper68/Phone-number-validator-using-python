# 📱 Phone Number Validator Using Python

A powerful command-line tool to validate phone numbers globally using the Veriphone API. Verify phone numbers with detailed validation results, including carrier information and number validity status.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🌟 Features

- ✅ **Global Phone Number Validation** - Validate phone numbers from any country
- 🔍 **Detailed Phone Information** - Get carrier, country, and validity details
- 🎨 **Colored CLI Output** - Beautiful and user-friendly command-line interface
- ⚡ **Fast & Reliable** - Real-time validation using the Veriphone API
- 🛡️ **Error Handling** - Comprehensive error handling for network and API issues
- 🔐 **Secure** - Works with your own API key

---

## 📋 Table of Contents

- [Getting Started](#-getting-started)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Getting an API Key](#-getting-an-api-key)
- [API Reference](#-api-reference)
- [Technologies Used](#-technologies-used)
- [How It Was Created](#-how-it-was-created)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- An active internet connection
- A free or paid Veriphone API key

### Quick Clone & Setup

```bash
# Clone the repository
git clone https://github.com/Kushdeveloper68/Phone-number-validator-using-python.git

# Navigate to the project directory
cd Phone-number-validator-using-python

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python python.py
```

---

## 📦 Installation

### Using pip (from cloned repository)

```bash
pip install -r requirements.txt
```

### Dependencies

The project uses the following Python packages:

- **requests** (2.32.5) - For making HTTP requests to the Veriphone API
- **colorama** (0.4.6) - For colored terminal output
- **charset-normalizer** (3.4.4) - For character encoding detection
- **git-filter-repo** (2.47.0) - For git operations

View the complete dependency list in [requirements.txt](requirements.txt)

---

## 💻 How to Use

### Running the Application

```bash
python python.py
```

### Menu Options

When you run the application, you'll see a menu with three options:

```
1. Validate phone number
2. Help
3. Exit
```

### Validating a Phone Number

1. **Select Option 1** - "Validate phone number"
2. **Enter your Veriphone API key** - Get one from [Veriphone](https://veriphone.io/)
3. **Enter the phone number** - Use the format: `+<country_code><number>`
   - Example: `+919876543210` (for India)
   - Example: `+14155552671` (for USA)
   - Example: `+442071838750` (for UK)

### Example Session

```
=============== COMMANDS ===============
1. Validate phone number
2. Help
3. Exit

Enter command (1,2,3): 1
============== ENTER CREDENTIALS ==============
Enter API key: your_api_key_here
Enter phone number: +919876543210
🔍 Fetching data from server...

✅ PHONE DETAILS

phone_valid: true
country: IN
country_name: India
phone_type: mobile
carrier: Jio
```

### Error Handling

The tool handles various error scenarios:

- **Empty API Key** - ❌ API key cannot be empty
- **Invalid Phone Format** - ❌ Phone must contain only numbers
- **Invalid API Key** - ❌ Invalid or inactive API key
- **Bad Phone Number** - ❌ Invalid phone number format
- **Network Issues** - ❌ Internet or API server unreachable
- **Server Timeout** - ❌ Request timeout — server slow
- **Invalid Response** - ❌ Invalid response from server

---

## 🔑 Getting an API Key

### Step 1: Visit Veriphone Website
Go to [https://veriphone.io/](https://veriphone.io/)

### Step 2: Sign Up
- Click on "Get Started" or "Sign Up"
- Create a free account with your email
- Verify your email address

### Step 3: Generate API Key
- Log in to your dashboard
- Navigate to "API Keys" section
- Click "Generate New Key"
- Copy your API key
- Keep it secure!

### Step 4: Use in the Tool
When prompted in the application, paste your API key:
```
Enter API key: your_generated_api_key_here
```

### Free Tier vs Paid Tiers
- **Free Tier**: Limited API calls per month (perfect for testing)
- **Paid Tiers**: Higher limits for production use
- Check [Veriphone pricing](https://veriphone.io/pricing) for details

---

## 🌐 API Reference

### Veriphone API

**Base URL:** `https://api.veriphone.io/v2/verify`

**Parameters:**
- `phone` - The phone number to validate (digits only)
- `key` - Your Veriphone API key

**Response Example:**
```json
{
  "phone_valid": true,
  "country": "IN",
  "country_name": "India",
  "phone_type": "mobile",
  "carrier": "Jio"
}
```

**Status Codes:**
- `200` - Successfully validated
- `400` - Invalid phone number format
- `401` - Invalid or inactive API key
- `500` - Server error (temporary)

For more details, visit [Veriphone API Documentation](https://veriphone.io/docs/v2)

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Programming Language | 3.8+ |
| **Requests** | HTTP Client Library | 2.32.5 |
| **Colorama** | Terminal Color Output | 0.4.6 |
| **Veriphone API** | Phone Number Validation | v2 |

---

## 📝 How It Was Created

### Development Process

1. **Concept & Planning**
   - Identified the need for a simple, reliable phone number validator
   - Researched available phone validation APIs
   - Selected Veriphone for its global coverage and reliability

2. **Core Development**
   - Built main validation logic using the `requests` library
   - Implemented comprehensive error handling for various failure scenarios
   - Added input validation for API keys and phone numbers

3. **User Interface**
   - Created an interactive CLI menu system
   - Integrated `colorama` for color-coded output
   - Designed ASCII art header for professional appearance
   - Implemented intuitive user prompts

4. **Error Handling & Robustness**
   - Added timeout handling for network requests
   - Implemented specific error messages for different API responses
   - Added validation for empty inputs
   - Handled ConnectionError, Timeout, and JSON parsing errors

5. **Testing & Refinement**
   - Tested with various phone number formats
   - Validated error handling across different scenarios
   - Optimized API response parsing

### Architecture

```
python.py
├── Imports & Initialization
├── UI Colors & Styling (Colorama)
├── ASCII Header
├── verify_number() Function
│   ├── Input Validation
│   ├── API Request
│   ├── Exception Handling
│   └── Response Processing
└── Menu & Command Handler
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Fork the Repository

```bash
git clone https://github.com/Kushdeveloper68/Phone-number-validator-using-python.git
cd Phone-number-validator-using-python
git remote add upstream https://github.com/Kushdeveloper68/Phone-number-validator-using-python.git
```

### Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Make Your Changes

- Write clean, readable code
- Add comments for complex logic
- Follow PEP 8 style guidelines
- Test your changes thoroughly

### Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your feature"
```

### Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### Submit a Pull Request

- Go to the original repository
- Click "Pull Requests"
- Click "New Pull Request"
- Select your branch and describe your changes
- Submit for review

### Contribution Guidelines

- **Bug Reports**: Include error messages and steps to reproduce
- **Feature Requests**: Explain the use case and expected behavior
- **Code Quality**: Follow existing code style and conventions
- **Documentation**: Update README if adding new features
- **Testing**: Ensure all changes work as expected

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features (e.g., batch validation, custom output formats)
- 📚 Documentation improvements
- 🔧 Code optimization
- 🧪 Additional test cases
- 🎨 UI/UX improvements

---

## 👨‍💻 Author

**Kush Pandit**

- GitHub: [@kushdeveloper68](https://github.com/kushdeveloper68/)
- Email: Contact via GitHub profile
- Portfolio: https://github.com/kushdeveloper68/

Feel free to reach out with feedback, questions, or suggestions!

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🎯 Future Enhancements

- [ ] Batch validation from CSV files
- [ ] Custom output formats (JSON, CSV, Excel)
- [ ] Rate limiting and caching
- [ ] GUI version using tkinter or PyQt
- [ ] Unit tests and integration tests
- [ ] Configuration file support
- [ ] Phone number formatting utilities
- [ ] API usage statistics and reporting

---

## ⭐ Show Your Support

If you found this tool helpful, please give it a star on GitHub! Your support motivates continued development.

---

## 🐛 Bug Reports & Feedback

Found a bug or have suggestions? Please open an issue on [GitHub Issues](https://github.com/Kushdeveloper68/Phone-number-validator-using-python/issues).

---

## 📚 Additional Resources

- [Veriphone Documentation](https://veriphone.io/)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [PEP 8 Style Guide](https://pep8.org/)

---

**Last Updated:** February 2026  
**Status:** Active & Maintained

Made with ❤️ by [Kush Pandit](https://github.com/kushdeveloper68/)