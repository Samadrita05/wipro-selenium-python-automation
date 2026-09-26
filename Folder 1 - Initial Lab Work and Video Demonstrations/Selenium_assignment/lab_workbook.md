# 📘 Selenium & Automation Testing Lab Workbook

Welcome to the comprehensive lab workbook for automation engineering. This document serves as a structured log of lab exercises, module completions and implementation details for testing frameworks using Python and Robot Framework.

🔗 **[Click Here to Access the Module Workbook Link](https://drive.google.com/file/d/1-kjDxf7ljixUcLVqxBfqsuSlilMR_At_/view?usp=sharing)** 

---

## 📂 Course Modules & Lab Work

### 🛠️ Module 1 – Automation with Selenium
Focused on core WebDriver interactions, dynamic element locating, and handling native browser components.
* **Multi-Locator Challenge** – Identification and element handling using `By.ID`, `By.NAME`, `By.XPATH` and `By.CSS_SELECTOR`.
* **Synchronization** – Implementing robust element synchronization using **Explicit Waits** (`WebDriverWait` and `expected_conditions`).
* **Windows, Tabs, and iFrames** – Handling multi-window switching, browser tab controls and navigating inside inline frames.

### 🧪 Module 2 – Unit Test Frameworks
Transitioning from standalone scripts to structured test suites with assertions and reporting.
* **PyTest Integration** – Utilizing `pytest` features, implementing flexible **Fixtures** and generating detailed **HTML Reporting**.
* **Page Object Model (POM)** – Designing scalable, low-maintenance test architectures using PyTest and POM.

### 🌐 Module 3 – Python BDD Restful
Implementing Behavior-Driven Development for both UI automation and RESTful API verification.
* **BDD Setup & REST API Validation** – Setting up Gherkin syntax environments and validating API responses using **Python and Behave**.
* **Data-Driven API Automation** – Injecting multiple test datasets directly through feature files to validate API endpoints.
* **Selenium POM with Behave** – Binding front-end Page Object Models with step definitions in a BDD ecosystem.

### 🤖 Module 4 – Robot Framework
Exploring keyword-driven testing architectures using the Robot ecosystem.
* **SeleniumLibrary Essentials** – Interacting with inputs via `Input Text` and verifying DOM structures using `Page Should Contain Element`.
* **Variable Management** – Utilizing scalar, list, and dictionary variables effectively across test suites.
* **User-Defined Keywords** – Creating custom, high-level reusable keywords to abstract complex user workflows.
* **Setup and Teardown** – Orchestrating preconditions and cleanups at both the individual Test and Suite levels.