# 🚀 Wipro Selenium Python Automation Capstone Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium\&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-Testing-orange)
![Unittest](https://img.shields.io/badge/Unittest-Python%20Framework-blue)
![Page Object Model](https://img.shields.io/badge/Design%20Pattern-Page%20Object%20Model-purple)
![HTML Report](https://img.shields.io/badge/Reporting-HTML%20Report-red)
![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-black?logo=github)

---

## 📌 Project Overview

This project is a **Selenium Python Automation Framework** developed as part of the **Wipro Selenium Capstone Project**.

The framework automates web application functionalities using **Selenium WebDriver, Python, PyTest, Unittest and the Page Object Model (POM)** design pattern.

The primary objective of this project is to develop a structured, reusable, maintainable and scalable automation framework for testing web application functionalities.

The project automates the following major functionalities:

* 🔐 User Login
* 🔍 Product Search
* 📸 Screenshot Capture on Test Failure
* 📊 HTML Test Reporting
* 🧪 Automated Test Execution Using PyTest
* 🗂️ External Test Data Management Using CSV
* ⚙️ Configuration Management
* 🏗️ Page Object Model-Based Framework Design

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To automate web application testing using Selenium WebDriver.
2. To implement the Page Object Model design pattern.
3. To separate test logic from page interaction logic.
4. To use reusable utility classes.
5. To manage configuration values through a configuration file.
6. To read test data from a CSV file.
7. To execute test cases using PyTest and Unittest.
8. To capture screenshots when test cases fail.
9. To generate HTML reports for test execution results.
10. To maintain the project using Git and GitHub.

---

## 🛠️ Technologies and Tools Used

| Technology / Tool     | Purpose                                    |
| --------------------- | ------------------------------------------ |
| 🐍 Python             | Programming language                       |
| 🌐 Selenium WebDriver | Web browser automation                     |
| 🧪 PyTest             | Test execution and test discovery          |
| 🔬 Unittest           | Python unit testing framework              |
| 🏗️ Page Object Model | Design pattern for maintainable automation |
| 📄 CSV                | External test data management              |
| ⚙️ ConfigParser       | Configuration management                   |
| 📊 HTML Reporting     | Test execution result reporting            |
| 📸 Screenshots        | Capturing evidence of test failures        |
| 🔧 Git                | Version control                            |
| ☁️ GitHub             | Source code repository                     |
| 💻 VS Code            | Development environment                    |

---

## 🏛️ Framework Architecture

This project follows a modular automation framework architecture.

The framework is organized into separate components:

* **Configuration Layer:** Stores configurable project values.
* **Page Object Layer:** Contains web page interaction methods.
* **Test Layer:** Contains automated test cases.
* **Utility Layer:** Provides reusable helper functions.
* **Test Data Layer:** Stores external test data.
* **Reporting Layer:** Stores generated HTML reports.
* **Screenshot Layer:** Stores screenshots captured during execution.

This separation improves code readability, maintainability, reusability, and scalability.

---

## 📂 Project Folder Structure

```text
Wipro_Selenium_Capstone_project/
│
├── 📁 config/
│   └── config.ini
│
├── 📁 pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── 📁 tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_product_search.py
│
├── 📁 utilities/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot.py
│
├── 📁 data/
│   ├── test_data.example.csv
│   └── test_data.csv
│
├── 📁 screenshots/
│   └── Failure screenshots
│
├── 📁 reports/
│   ├── report.html
│   └── report.css
│
├── 📄 conftest.py
├── 📄 pytest.ini
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore
```

> 🔒 The actual test data file containing credentials is excluded from version control through `.gitignore`.

---

## 🧩 Framework Components

### 1️⃣ Configuration Management

The `config/config.ini` file is used to store configuration values such as:

* 🌐 Application URL
* ⚙️ Other configurable framework settings

The `config_reader.py` utility reads configuration values so that they can be reused throughout the framework.

**Benefits:**

* Avoids hardcoding configuration values.
* Makes configuration changes easier.
* Improves framework maintainability.

---

### 2️⃣ Page Object Model (POM)

The Page Object Model design pattern is used to separate web page interaction logic from test case logic.

Each page class contains methods for interacting with elements on a specific web page.

#### 🏠 `home_page.py`

Responsible for home page-related interactions.

#### 🔐 `login_page.py`

Responsible for login-related operations, including:

* Entering username.
* Entering password.
* Submitting login credentials.
* Validating login status.

#### 🔍 `search_page.py`

Responsible for product search-related operations, including:

* Entering product search information.
* Performing product searches.
* Interacting with search results.

**Benefits of POM:**

* ♻️ Code reusability
* 🧹 Reduced code duplication
* 🔧 Easier maintenance
* 📖 Improved readability
* 📈 Better scalability

---

### 3️⃣ Test Cases

The `tests/` directory contains the automated test cases.

#### 🔐 Login Test

File:

```text
tests/test_login.py
```

The login test verifies whether the user can log in to the application using the provided test data.

**Test flow:**

1. Launch the browser.
2. Open the application.
3. Navigate to the login page.
4. Read login credentials from the CSV file.
5. Enter the username.
6. Enter the password.
7. Submit the login form.
8. Validate the login result.

---

#### 🔍 Product Search Test

File:

```text
tests/test_product_search.py
```

The product search test verifies the product search functionality.

**Test flow:**

1. Launch the browser.
2. Open the application.
3. Log in using the required credentials.
4. Enter the product name.
5. Perform the product search.
6. Validate the search result.

---

### 4️⃣ Utility Classes

The `utilities/` directory contains reusable helper classes and functions.

| Utility             | Responsibility                    |
| ------------------- | --------------------------------- |
| `config_reader.py`  | Reads configuration values        |
| `csv_reader.py`     | Reads external CSV test data      |
| `driver_factory.py` | Creates and manages the WebDriver |
| `screenshot.py`     | Supports screenshot capture       |

Using utility classes helps avoid repeated code and supports a modular framework design.

---

### 5️⃣ External Test Data Management

The framework uses a CSV file to store test data.

Example structure:

```csv
username,password,product
example@email.com,example_password,MacBook
```

The test data includes:

* 👤 Username
* 🔑 Password
* 💻 Product name

### 🔒 Security Note

Actual credentials are stored locally in:

```text
data/test_data.csv
```

This file is excluded from Git tracking using `.gitignore`.

A sample file is provided for reference:

```text
data/test_data.example.csv
```

⚠️ **Never commit real usernames, passwords, API keys, or other sensitive information to a public repository.**

---

## 🧪 Test Execution

### ✅ Prerequisites

Before running the project, make sure the following are installed:

* Python 3.x
* Google Chrome or another supported browser
* Git
* Visual Studio Code or another Python IDE

---

### 📥 Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd wipro-selenium-capstone-project
```

---

### 🐍 Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

---

### ▶️ Step 3: Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

---

### 📦 Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ⚙️ Step 5: Configure Test Data

Create the local test data file:

```text
data/test_data.csv
```

Use the structure provided in:

```text
data/test_data.example.csv
```

Add valid test credentials locally. Do not commit the file if it contains sensitive information.

---

### 🚀 Step 6: Run All Test Cases

```bash
pytest -v -s
```

This command executes the test cases and displays detailed output in the terminal.

---

### 🔐 Step 7: Run the Login Test

```bash
pytest tests/test_login.py -v -s
```

---

### 🔍 Step 8: Run the Product Search Test

```bash
pytest tests/test_product_search.py -v -s
```

---

## 📊 Test Reporting

The framework generates an HTML report containing test execution results.

The report includes information such as:

* 🧪 Executed test cases
* ✅ Passed tests
* ❌ Failed tests
* ⏱️ Test execution details
* 📋 Test result summary

The report is available at:

```text
reports/report.html
```

The HTML report can be opened in a web browser for easier analysis of the test execution results.

---

## 📸 Screenshot Capture

The framework supports screenshot capture for failed test cases.

Screenshots help with:

* 🔎 Debugging test failures
* 📝 Identifying application issues
* 📊 Providing execution evidence
* 🛠️ Investigating unexpected behavior

Screenshots are stored in:

```text
screenshots/
```

---

## 🧾 Test Execution Summary

The implemented test suite includes:

| Test Case           | Functionality  | Expected Result                           |
| ------------------- | -------------- | ----------------------------------------- |
| Login Test          | User login     | Login functionality is validated          |
| Product Search Test | Product search | Product search functionality is validated |

The test suite has been executed using PyTest, and the HTML report provides the execution results.

---

## 🌟 Key Features

* ✅ Selenium WebDriver automation
* ✅ Python-based framework
* ✅ Page Object Model implementation
* ✅ PyTest test execution
* ✅ Unittest-compatible testing structure
* ✅ Reusable utility classes
* ✅ Configuration file management
* ✅ CSV-based test data
* ✅ Screenshot support
* ✅ HTML test reporting
* ✅ Virtual environment support
* ✅ Git version control
* ✅ GitHub repository integration
* ✅ Modular and maintainable project structure

---

## 💡 Advantages of the Framework

### ♻️ Reusability

Common operations are implemented in reusable page objects and utility classes.

### 🛠️ Maintainability

Changes to web page elements can be managed within the relevant page class.

### 📈 Scalability

The modular structure allows additional test cases and page objects to be added easily.

### 🔍 Debugging Support

Screenshots and HTML reports help analyze test execution results.

### 🔐 Secure Test Data Handling

Sensitive test data is excluded from version control through `.gitignore`.

---

## 🎬 Complete Video Demonstration

### ▶️ Watch the Complete Project Demonstration

🎥 The video demonstrates the complete execution of the Wipro Selenium Python Automation Framework, including login automation, product search, framework components, test execution and HTML reporting.

🔗 **Video Demonstration:**  [Watch the Complete Project Video by tapping below 👇🏼]
 https://drive.google.com/file/d/1JOvYLfLZ9jkDsx9NDNYhfWIGAdrw9clm/view?usp=sharing

> 📌 The video contains the full project explanation as well as framework demonstration, automated test execution and generated structured HTML test report.

---

## 🔮 Future Enhancements

The framework can be extended with the following features:

* 🔄 Data-driven testing with multiple test data sets
* 🌐 Cross-browser testing
* ⚡ Parallel test execution
* 📋 Advanced logging
* 🔁 Retry mechanism for failed tests
* 🔗 Continuous Integration using Jenkins or GitHub Actions
* 📊 Enhanced reporting using Allure Reports
* 🧪 Additional functional and regression test cases

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

* Python programming
* Selenium WebDriver automation
* Page Object Model design pattern
* PyTest test execution
* Unittest framework concepts
* Test data management
* Configuration management
* Exception handling and debugging
* Screenshot capture
* HTML test reporting
* Git and GitHub version control
* Automation framework organization

---

## 👩‍💻 Author

**Samadrita Hazra**

🎓 Wipro Selenium Python Capstone Project

---

## 📜 Disclaimer

This project is developed for educational and automation testing purposes as part of the Wipro Selenium Python Capstone Project.

The project should be used only with authorized applications and test environments.

---

## ⭐ If You Find This Project Useful

If this repository helps you understand Selenium Python automation frameworks, feel free to explore the project structure and implementation.

**Thank you for visiting this project! 🚀**
