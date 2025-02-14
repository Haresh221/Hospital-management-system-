# Patient Records Management System

## Overview

This is a simple **Patient Records Management System** implemented in Python. It allows users to add, display, update, and manage patient details such as name, age, gender, blood group, and disease history. The data is stored in a text file (`demo.txt`) to ensure persistence across program restarts.

## Features

- Add new patient records
- Display all stored patient records
- Search for a specific patient by name
- Update patient details
- Store patient records in a file (`demo.txt`)
- Load existing records on startup

## Installation

To run this project, you need Python installed on your system.

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/patient-records.git
   ```
2. Navigate to the project directory:
   ```bash
   cd patient-records
   ```
3. Run the script:
   ```bash
   python patient_records.py
   ```

## Usage

Once you run the script, a menu will appear:

```
1. ADD PATIENT   2. PATIENTS COMPLETE LIST   3. UPDATE PATIENT   4. DISPLAY PATIENT   5. EXIT
```

- Select an option by entering the corresponding number.
- Follow the on-screen prompts to enter or update patient information.
- Patient records are saved automatically to `demo.txt`.

## File Structure

```
patient-records/
│-- patient_records.py   # Main script
│-- demo.txt             # Stores patient records (auto-generated)
│-- README.md            # Project documentation
```

## Contributing

Contributions are welcome! This project was developed in collaboration with my partner, Deepak Ostwal and myself. To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Your changes"
   ```
4. Push to your fork and create a Pull Request.

---



