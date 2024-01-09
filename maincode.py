import tkinter as tk
from tkinter import ttk

class MatchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matching Program")

        # Pre-loaded set of items with values
        self.items = {
            "Item A": [1, 65, 21],
            "Item B": [10, 50, 30],
            # Add more items here
        }

        # Create variables to store user input
        self.user_values = [tk.DoubleVar() for _ in range(len(self.items["Item A"]))]

        # Create and place sliders
        self.sliders = []
        for i, item in enumerate(self.items.keys()):
            label = tk.Label(root, text=f"{item}:")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            slider = ttk.Scale(root, from_=0, to=100, variable=self.user_values[i], orient="horizontal", length=200)
            slider.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.sliders.append(slider)

        # Button to calculate and display results
        submit_button = tk.Button(root, text="Submit", command=self.calculate_results)
        submit_button.grid(row=len(self.items), column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=len(self.items) + 1, column=0, columnspan=2, pady=10)

    def calculate_results(self):
        # Calculate the closest match for each item
        closest_matches = {item: self.get_closest_match(self.user_values, values) for item, values in self.items.items()}

        # Determine the set with the most closest matches
        result_set = max(closest_matches, key=closest_matches.get)

        # Display the result
        self.result_label.config(text=f"You are more closely matched to Set: {result_set}")

    def get_closest_match(self, user_values, item_values):
        # Calculate the Euclidean distance between user values and item values
        distance = sum((u - v) ** 2 for u, v in zip(user_values, item_values)) ** 0.5
        return distance

if __name__ == "__main__":
    root = tk.Tk()
    app = MatchingApp(root)
    root.mainloop()
