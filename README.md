# Bing Search Automation

This Python script automates Bing searches to accumulate reward points. It interacts with the Microsoft Edge browser to perform searches and earn Bing reward points.

## How it Works

The script utilizes the `pyautogui` library to simulate mouse and keyboard actions. Users need to provide the X and Y coordinates of their Microsoft Edge search box. You can use the [get-cursor-position](https://github.com/aditya-mad/get-cursor-position) tool to find these coordinates.

## Prerequisites

- Python installed
- Microsoft Edge installed
- [get-cursor-position](https://github.com/aditya-mad/get-cursor-position) tool (optional, for finding coordinates)

## Usage
1. Clone the Union Encrypt repository to your local machine:

    ```bash
    git clone https://github.com/your-username/UnionEncrypt.git
    cd UnionEncrypt
    ```

2. Ensure you have the required modules installed:
   - Pyautogui:
     ```bash
     pip install Pyautogui
     ```
3. Run the main file:

    ```bash
    python main.py
    ```
    - Within 5 seconds, open Microsoft Edge and leave it idle.
    - The script will automate searches, earning Bing reward points.

## Customization
Feel free to customize the search list with your preferred search queries.
