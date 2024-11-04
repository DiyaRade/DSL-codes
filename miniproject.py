"""Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: """

import tkinter as tk
from tkinter import messagebox, font


class Node:
    def __init__(self, name, destination, time, price):
        self.name = name
        self.destination = destination
        self.time = time
        self.price = price
        self.next = None


class AirlineQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name, destination, time, price):
        new_node = Node(name, destination, time, price)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return f"{name} registered for {destination} at {time}. Ticket Price: ₹{price}."

    def dequeue(self):
        if self.front is None:
            return "No passengers in the queue."
        removed_passenger = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return (
            f"{removed_passenger.name} boarded the flight to {removed_passenger.destination} "
            f"at {removed_passenger.time}. Ticket Price: ₹{removed_passenger.price}."
        )

    def display_queue(self):
        if self.front is None:
            return "No passengers in the queue."
        result = "Current Passenger Queue:\n"
        temp = self.front
        while temp:
            result += (
                f"- {temp.name}, Destination: {temp.destination}, Time: {temp.time}, "
                f"Price: ₹{temp.price}\n"
            )
            temp = temp.next
        return result


class AirlineUI:
    PRICES = {
        "India": {
            "06:00 AM": 3000,
            "12:00 PM": 3500,
            "06:00 PM": 4000,
            "10:00 PM": 2500,
        },
        "USA": {
            "06:00 AM": 50000,
            "12:00 PM": 52000,
            "06:00 PM": 55000,
            "10:00 PM": 49000,
        },
        "UK": {
            "06:00 AM": 40000,
            "12:00 PM": 43000,
            "06:00 PM": 45000,
            "10:00 PM": 42000,
        },
        "Japan": {
            "06:00 AM": 45000,
            "12:00 PM": 47000,
            "06:00 PM": 48000,
            "10:00 PM": 44000,
        },
        "Australia": {
            "06:00 AM": 42000,
            "12:00 PM": 44000,
            "06:00 PM": 46000,
            "10:00 PM": 41000,
        },
        "Germany": {
            "06:00 AM": 35000,
            "12:00 PM": 37000,
            "06:00 PM": 39000,
            "10:00 PM": 34000,
        },
        "Canada": {
            "06:00 AM": 48000,
            "12:00 PM": 50000,
            "06:00 PM": 53000,
            "10:00 PM": 47000,
        },
        "France": {
            "06:00 AM": 36000,
            "12:00 PM": 38000,
            "06:00 PM": 40000,
            "10:00 PM": 35000,
        },
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation System")
        self.queue = AirlineQueue()

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.headline = tk.Label(
            self.main_frame,
            text="Airline Reservation System",
            font=font.Font(size=24, weight="bold"),
            pady=10,
        )
        self.headline.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.form_frame = tk.Frame(self.main_frame, pady=10)
        self.form_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.form_frame.columnconfigure(1, weight=1)
        self.name_label = tk.Label(self.form_frame, text="Passenger Name:")
        self.name_entry = tk.Entry(self.form_frame)
        self.destination_label = tk.Label(self.form_frame, text="Destination:")
        self.destination_var = tk.StringVar(value="India")
        self.destination_menu = tk.OptionMenu(
            self.form_frame, self.destination_var, *self.PRICES.keys()
        )
        self.time_label = tk.Label(self.form_frame, text="Time Slot:")
        self.time_var = tk.StringVar(value="06:00 AM")
        self.time_menu = tk.OptionMenu(
            self.form_frame,
            self.time_var,
            "06:00 AM",
            "12:00 PM",
            "06:00 PM",
            "10:00 PM",
        )
        self.name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.destination_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.destination_menu.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.time_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.time_menu.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.buttons_frame = tk.Frame(self.main_frame, pady=10)
        self.buttons_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.enqueue_button = tk.Button(
            self.buttons_frame, text="Register Ticket", command=self.register_ticket
        )
        self.dequeue_button = tk.Button(
            self.buttons_frame, text="Board Passenger", command=self.board_passenger
        )
        self.view_queue_button = tk.Button(
            self.buttons_frame, text="View Passenger Queue", command=self.view_queue
        )
        self.enqueue_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.dequeue_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.view_queue_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        self.result_label = tk.Label(
            self.main_frame, text="", wraplength=400, anchor="w", justify="left"
        )
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    def register_ticket(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a passenger name.")
            return
        destination = self.destination_var.get()
        time = self.time_var.get()
        price = self.PRICES[destination][time]
        result = self.queue.enqueue(name, destination, time, price)
        self.result_label.config(text=result)
        self.name_entry.delete(0, tk.END)

    def board_passenger(self):
        result = self.queue.dequeue()
        self.result_label.config(text=result)

    def view_queue(self):
        result = self.queue.display_queue()
        self.result_label.config(text=result)


def main():
    root = tk.Tk()
    root.geometry("600x400")
    app = AirlineUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
