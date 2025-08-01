 # 🎓 GUI-Based Student Report Card Generator

A Python desktop application built with **Tkinter** that collects student details and marks, validates input, computes total/percentage/grade, displays status messages, and appends each report to a file.

## 🔧 Features
- Input student name and roll number  
- Enter marks for English, Science, and Math  
- Validation for:
  - Empty fields  
  - Numeric marks  
  - Marks between 0 and 100  
- Calculates total marks and percentage  
- Determines grade based on percentage:
  - A: 90+  
  - B: 75–89  
  - C: 60–74  
  - D: 40–59  
  - F: Below 40  
- Displays status/errors via label and popups (`messagebox`)  
- Appends the generated report to `report_card.txt`  
- Clear button to reset all input fields  

## 🖥️ Sample Output (in `report_card.txt`)
