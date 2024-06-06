import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # Add Contact Frame
        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Name").grid(row=0, column=0)
        tk.Label(self.add_frame, text="Phone").grid(row=0, column=1)
        tk.Label(self.add_frame, text="Email").grid(row=0, column=2)
        tk.Label(self.add_frame, text="Address").grid(row=0, column=3)

        self.name_entry = tk.Entry(self.add_frame)
        self.phone_entry = tk.Entry(self.add_frame)
        self.email_entry = tk.Entry(self.add_frame)
        self.address_entry = tk.Entry(self.add_frame)

        self.name_entry.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=1, column=2)
        self.address_entry.grid(row=1, column=3)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=1, column=4, padx=10)

        # Display Frame
        self.display_frame = tk.Frame(root)
        self.display_frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.display_frame, width=100, height=10)
        self.contact_listbox.pack()

        # Control Frame
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        self.view_button = tk.Button(self.control_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=0, padx=5)

        self.search_button = tk.Button(self.control_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(self.control_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=2, padx=5)

        self.delete_button = tk.Button(self.control_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=3, padx=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and phone are required fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        if not self.contacts:
            self.contact_listbox.insert(tk.END, "No contacts available.")
        else:
            for contact in self.contacts:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts if search_term in contact["name"] or search_term in contact["phone"]]
            self.contact_listbox.delete(0, tk.END)
            if not found_contacts:
                self.contact_listbox.insert(tk.END, "No contacts found.")
            else:
                for contact in found_contacts:
                    self.contact_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        for contact in self.contacts:
            if search_term in contact["name"] or search_term in contact["phone"]:
                self.contact_listbox.delete(0, tk.END)
                self.contact_listbox.insert(tk.END, f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

                name = simpledialog.askstring("Update Name", "Enter new name (leave blank to keep current):") or contact["name"]
                phone = simpledialog.askstring("Update Phone", "Enter new phone number (leave blank to keep current):") or contact["phone"]
                email = simpledialog.askstring("Update Email", "Enter new email (leave blank to keep current):") or contact["email"]
                address = simpledialog.askstring("Update Address", "Enter new address (leave blank to keep current):") or contact["address"]

                contact.update({"name": name, "phone": phone, "email": email, "address": address})
                messagebox.showinfo("Success", f"Contact {name} updated successfully!")
                return
        messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        for contact in self.contacts:
            if search_term in contact["name"] or search_term in contact["phone"]:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", f"Contact {contact['name']} deleted successfully!")
                return
        messagebox.showwarning("Not Found", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
