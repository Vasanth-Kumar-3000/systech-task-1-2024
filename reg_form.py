import tkinter as tk
from tkinter import messagebox
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Function to validate user inputs
def validate_inputs():
    name = name_entry.get()
    aicte_id = aicte_id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    college_name = college_name_entry.get()

    # Regular expressions for validation
    name_regex = r'^[a-zA-Z\s]+$'
    aicte_id_regex = r'^\d+$'
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    phone_regex = r'^\d{10}$'

    # Check if any field is empty
    if not name or not aicte_id or not email or not phone or not college_name:
        messagebox.showerror("Error", "All fields are required.")
        return

    # Validate Name
    if not re.match(name_regex, name):
        messagebox.showerror("Error", "Invalid name format.")
        return

    # Validate AICTE ID
    if not re.match(aicte_id_regex, aicte_id):
        messagebox.showerror("Error", "Invalid AICTE ID format.")
        return

    # Validate Email
    if not re.match(email_regex, email):
        messagebox.showerror("Error", "Invalid email format.")
        return

    # Validate Phone Number
    if not re.match(phone_regex, phone):
        messagebox.showerror("Error", "Invalid phone number format.")
        return

    # If all inputs are valid, generate PDF
    generate_pdf(name, aicte_id, email, phone, college_name)

# Function to generate PDF
def generate_pdf(name, aicte_id, email, phone, college_name):
    doc = SimpleDocTemplate(f"{name}.pdf", pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"Name: {name}", styles["Heading2"]))
    elements.append(Paragraph(f"AICTE ID: {aicte_id}", styles["BodyText"]))
    elements.append(Paragraph(f"Email: {email}", styles["BodyText"]))
    elements.append(Paragraph(f"Phone Number: {phone}", styles["BodyText"]))
    elements.append(Paragraph(f"College Name: {college_name}", styles["BodyText"]))

    doc.build(elements)
    messagebox.showinfo("Success", "PDF generated successfully.")

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

aicte_id_label = tk.Label(root, text="AICTE ID:")
aicte_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
aicte_id_entry = tk.Entry(root)
aicte_id_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

college_name_label = tk.Label(root, text="College Name:")
college_name_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
college_name_entry = tk.Entry(root)
college_name_entry.grid(row=4, column=1, padx=5, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=validate_inputs)
submit_button.grid(row=5, column=1, padx=5, pady=5)

# Run the main event loop
root.mainloop()