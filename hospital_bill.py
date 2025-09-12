import datetime

hospital_name = "CityCare Hospital"

now = datetime.datetime.now()
dt = now.strftime("%d-%m-%Y %H:%M:%S")

def generate_op_ticket(patient_name, age, doctor, department, fee, set):
    set.write("========== OP TICKET ==========\n")
    set.write("Hospital :"+ hospital_name + "\n")
    set.write("Date & Time:" + dt + "\n")
    set.write("Patient  :"+ patient_name + "| Age:"+ str(age) + "\n")
    set.write("Doctor   :"+ doctor+ "("+ department + ")\n")
    set.write("OP Fee   : Rs."+ str(fee)+ "\n")
    set.write("===============================+\n\n")
    return fee

def generate_pharmacy_bill(medicines, set):
    set.write("====== PHARMACY BILL ======\n")
    set.write("Hospital :"+ hospital_name + "\n")
    set.write("Date & Time:"+ dt + "\n")
    med_total = 0
    for i in medicines:
        total = i["Qty"] * i["Price"]
        med_total = med_total + total
        set.write(i["Name"]+ "x"+ str(i["Qty"]) + "="+ "Rs."+ str(total) + "\n")
    set.write("Total Medicines: Rs."+ str(med_total) + "\n")
    set.write("===========================\n\n")
    return med_total

def generate_overall_bill(patient_name, age, doctor, department, op_fee, med_total, tests, set):
    set.write("====== OVERALL BILL ======\n")
    set.write("Hospital :"+ hospital_name + "\n")
    set.write("Date & Time:"+ dt + "\n")
    set.write("Patient  :"+ patient_name + "| Age:"+ str(age) + "\n")
    set.write("Doctor   :"+ doctor+ "("+ department+ ")\n")
    set.write("---------------------------")
    set.write("OP Fee: Rs."+ str(op_fee) + "\n")
    set.write("Medicines: Rs."+ str(med_total)+ "\n")

    test_total = 0
    if tests:
        set.write("Lab Tests:\n")
        for t in tests:
            test_total = test_total + t["Price"]
            set.write("-"+ t["Test"]+ "="+ "Rs."+ str(t["Price"]) +"\n")
    set.write("---------------------------\n")

    subtotal = op_fee + med_total + test_total
    cgst = subtotal * 0.05
    sgst = subtotal * 0.05
    grand_total = subtotal + cgst + sgst

    set.write("Subtotal: Rs."+ str(subtotal) +"\n")
    set.write("CGST (5%): Rs."+ str(cgst) +"\n")
    set.write("SGST (5%): Rs."+ str(sgst) + "\n")
    set.write("===========================\n")
    set.write("Grand Total: Rs."+ str(grand_total) + "\n")
    set.write("===========================\n")
    set.write("\nEND OF BILL\n")

print("=== Enter Patient Details ===")
name = input("Patient Name: ")
age = int(input("Age: "))
doctor = input("Doctor's Name: ")
dept = input("Department: ")
op_fee = float(input("OP Fee: "))

medicines = []
print("--- Enter Medicines ---")
while True:
    med_name = input("Medicine Name (or 'done'): ")
    if med_name.lower() == "done":
        break
    qty = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    medicines.append({"Name": med_name, "Qty": qty, "Price": price})

tests = []
print("--- Enter Lab Tests ---")
while True:
    test_name = input("Test Name (or 'done'): ")
    if test_name.lower() == "done":
        break
    test_price = float(input("Test Price: "))
    tests.append({"Test": test_name, "Price": test_price})

with open("hospital_bill.txt","w") as set:
    op_total = generate_op_ticket(name, age, doctor, dept, op_fee,set)
    med_total = generate_pharmacy_bill(medicines,set)
    generate_overall_bill(name, age, doctor, dept, op_total, med_total, tests,set)

print("\nBill saved to 'hospital_bill.txt'")

"""
========== OP TICKET ==========
Hospital : CityCare Hospital
Date & Time: 10-09-2025 22:25:35
Patient  : Priya | Age: 20
Doctor   : Pranav ( Cardio )
OP Fee   : Rs. 250.0
===============================
====== PHARMACY BILL ======
Hospital : CityCare Hospital
Date & Time: 10-09-2025 22:25:35
Dolo x 5 = Rs. 30.0
Total Medicines: Rs. 30.0
===========================
====== OVERALL BILL ======
Hospital : CityCare Hospital
Date & Time: 10-09-2025 22:25:35
Patient  : Priya | Age: 20
Doctor   : Pranav ( Cardio )
---------------------------
OP Fee: Rs. 250.0
Medicines: Rs. 30.0
Lab Tests:
- ECG = Rs. 40.0
- Blood Test = Rs. 100.0
---------------------------
Subtotal: Rs. 420.0
CGST (5%): Rs. 21.0
SGST (5%): Rs. 21.0
===========================
Grand Total: Rs. 462.0
===========================
"""