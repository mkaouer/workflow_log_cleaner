# workflow_log_cleaner

Large Language Models (LLMs) have recently gained attention for automating software debugging and log analysis, particularly in Continuous Integration and Continuous Deployment (CI/CD) workflows. GitHub Actions (GA), a widely used CI/CD automation tool, generates complex and verbose failure logs, making debugging a time-consuming and error-prone task. Existing studies show that LLMs perform well in explaining simple errors but struggle with complex failure scenarios due to unstructured logs and inadequate reasoning capabilities. 

This research aims to enhance LLM-based analysis to improve CI/CD pipeline reliability by diagnosing failures more efficiently. This will be achieved through log preprocessing, prompt optimization, and analysis of the differences between unfiltered and preprocessed logs, followed by an evaluation of the results.


![Data-Preparation drawio](https://github.com/user-attachments/assets/f99b1e36-d12e-4857-9fb4-1695d05c1dd8)

![Data-PreProcessing-Page-2 drawio](https://github.com/user-attachments/assets/b30e3a8d-0180-402b-9475-cba9a950fd2a)

![prompt-opt drawio](https://github.com/user-attachments/assets/5a83beaa-6b29-4809-a2d9-8f4ddd7b8103)

![Data-PreProcessing-Page-4 drawio (1)](https://github.com/user-attachments/assets/b41f8931-a968-4a72-9b95-af2a7deb60c1)

## Script Execution Guide

This repository contains scripts for diagnosing CI/CD pipeline failures using AI-powered analysis. The current script processes failure logs from GitHub Actions and provides summarized root causes with suggested fixes.

### Usage Instructions for `llama3-8B_failure_explanation.py`

#### Prerequisites
- Install **Python 3.8+**
- Install required dependencies:
  ```bash
  pip install pandas openpyxl

- Ensure **Ollama** is installed and accessible in your system path.
  
#### Execution Steps
- Run the script from the terminal:
  ```bash
  python llama3-8B_failure_explanation.py
- Provide the required input:
1- The script will prompt you to enter the path to the input Excel file.
2- It will also ask for the output Excel file path where the results will be saved.
  
##### Expected Input File Format
- The input file must be an Excel (.xlsx) file.
- It should contain a column named "Error log", where each row includes a failure log from GitHub Actions.
- The script processes each log and generates a summarized root cause analysis.
##### Expected Output
- The output Excel file will be saved at the specified path.
- A new column, "llama_8b", will contain AI-generated diagnoses for each error log.




