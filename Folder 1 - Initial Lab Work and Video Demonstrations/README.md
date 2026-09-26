# Folder 1 - Initial Lab Work and Video Demonstrations

This folder contains Python automation scripts developed using Selenium WebDriver for core web interaction testing, alongside an official Lab Workbook detailing the practical specifications.

## 📁 Project Structure

*   **`Selenium_assignment/`**
    *   **Python Scripts (`.py`):** Individual test cases covering UI components, browser actions and window handling.
    *   **`Lab_Workbook.[pdf/docx]`:** Document containing project guidelines, objectives and problem statements.
    *   **`video_outputs.md`:** Documentation or links to recorded execution runs.
    *   **`sample.txt`:** Test data file used for file handling scripts.

## 🚀 Key Automation Modules Covered

*   **UI Components:** Interacting with dynamic UI elements (`MinMaxSlider.py`).
*   **User Actions:** Automating complex interactions like drag-and-drop (`dragdrop.py`), hover states (`mousehover.py`) and advanced key entries (`keyboardaction.py`).
*   **Context Switching:** Handling asynchronous browser pop-ups (`alert.py`) and embedded frames (`iframe.py`).
*   **File & Browser Management:** Testing file uploads (`fileuploading.py`), multi-URL handling (`twourls.py`) and tab/page flows (`pagenavigation.py`).

## 🛠️ Prerequisites & Setup

1. **Install Dependencies:**
   Ensure Python 3.x is installed, then install Selenium:
   ```bash
   pip install selenium
   ```

2. **WebDrivers:**
   Ensure the appropriate browser driver (e.g., ChromeDriver, GeckoDriver) is installed and configured in your system environment path (or managed via `webdriver-manager`).

## 💻 Running the Scripts

To execute any specific lab assignment, run the script from the terminal:
```bash
python Assignment_1.py
```