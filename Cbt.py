import os
import time
import random
import string

class CBTSystem:
    def __init__(self):
        self.points = 0
        self.name = ""
        self.roll_number = 0
        self.user_password = ""
        self.file_name = "studentdata.txt"
        self.accounts_file = "studentlogin.txt"
        
        # Ensure necessary files exist
        self.ensure_file_exists(self.file_name)
        self.ensure_file_exists(self.accounts_file)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title):
        self.clear_screen()
        border = "=" * 40
        print(border)
        print(f"{title:^40}")
        print(border)

    def ensure_file_exists(self, file_path):
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as file:
                # Create an empty file if it does not exist
                pass

    def generate_password(self, length=8):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def create_account(self):
        self.print_header("Create Account")
        self.name = input("Enter your name: ")
        password = self.generate_password()
        print(f"Generated password: {password}")

        with open(self.accounts_file, 'a') as file:
            file.write(f"{self.name}\n{password}\n")
        print("Account created successfully.")
        time.sleep(10)

    def check_login(self):
        self.print_header("Login")
        self.name = input("Enter your name: ")
        self.user_password = input("Enter your password: ")

        with open(self.accounts_file, 'r') as file:
            lines = file.readlines()

        for i in range(0, len(lines), 2):
            file_name = lines[i].strip()
            file_password = lines[i + 1].strip()
            if file_name == self.name and file_password == self.user_password:
                print("Login successful.")
                return True

        print("Login failed.")
        time.sleep(2)
        return False

    def take_quiz(self, time_limit=60):
        self.print_header("Take Quiz")
        start_time = time.time()
        questions = [
            {"question": "What is the time complexity of the Bellman-Ford algorithm?", "options": ["A) O(V)", "B) O(V^2)", "C) O(V^3)", "D) O(EV)"], "answer": "d"},
            {"question": "Which sorting algorithm has the best average-case time complexity?", "options": ["A) Quick sort", "B) Merge sort", "C) Heap sort", "D) Insertion sort"], "answer": "b"},
            {"question": "What is the primary purpose of dynamic programming?", "options": ["A) To solve optimization problems by breaking them into subproblems", "B) To generate test cases for software testing", "C) To interpret high-level languages", "D) To allocate memory dynamically during program execution"], "answer": "a"},
            {"question": "Which data structure is typically used to implement a priority queue?", "options": ["A) Array", "B) Linked List", "C) Heap", "D) Stack"], "answer": "c"},
            {"question": "What is the purpose of the A* search algorithm?", "options": ["A) To find the shortest path in a weighted graph", "B) To perform pattern matching in strings", "C) To determine the maximum flow in a network", "D) To generate permutations of a set"], "answer": "a"},
            {"question": "Which algorithm is used for finding strongly connected components in a graph?", "options": ["A) Dijkstra's algorithm", "B) Kosaraju's algorithm", "C) Floyd-Warshall algorithm", "D) Bellman-Ford algorithm"], "answer": "b"},
            {"question": "What is the primary advantage of using a hash table for data storage?", "options": ["A) Constant time complexity for most operations", "B) Efficient use of memory", "C) Automatic resizing of the data structure", "D) Ability to store data in sorted order"], "answer": "a"},
            {"question": "Which graph traversal algorithm is used to detect cycles in a graph?", "options": ["A) Depth-first search", "B) Breadth-first search", "C) Dijkstra's algorithm", "D) Prim's algorithm"], "answer": "a"},
            {"question": "What is the primary advantage of using a self-balancing binary search tree?", "options": ["A) Guaranteed worst-case time complexity for search operations", "B) Ability to efficiently store large amounts of data", "C) Automatic resizing of the tree structure", "D) Balanced height for improved performance"], "answer": "d"},
            {"question": "Which algorithm is used to find the maximum flow in a flow network?", "options": ["A) Kruskal's algorithm", "B) Prim's algorithm", "C) Bellman-Ford algorithm", "D) Ford-Fulkerson algorithm"], "answer": "d"}
        ]

        for q in questions:
            if time.time() - start_time > time_limit:
                break
            self.print_header("Quiz Question")
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Your answer: ").strip().lower()
            if answer == q["answer"]:
                self.points += 1

        print(f"You scored {self.points} points.")
        with open(self.file_name, 'a') as file:
            file.write(f"Name: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.points}\n")
        time.sleep(2)

    def search_data(self):
        self.print_header("Search Data")
        search_query = input("Enter roll number to check results: ").strip()
        found = False

        with open(self.file_name, 'r') as file:
            lines = file.readlines()

        for i in range(0, len(lines), 4):
            if search_query in lines[i]:
                print("".join(lines[i:i + 4]))
                found = True

        if not found:
            print("No data found for the given roll number.")
        time.sleep(2)

    def view_results(self):
        self.print_header("View Results")
        with open(self.file_name, 'r') as file:
            print(file.read())
        input("Press Enter to continue...")
        time.sleep(2)

    def update_account(self):
        self.print_header("Update Account")
        self.name = input("Enter your name: ")
        new_password = input("Enter your new password: ")

        with open(self.accounts_file, 'r') as file:
            lines = file.readlines()

        with open(self.accounts_file, 'w') as file:
            for i in range(0, len(lines), 2):
                if lines[i].strip() == self.name:
                    file.write(f"{self.name}\n{new_password}\n")
                else:
                    file.write(lines[i])
                    file.write(lines[i + 1])

        print("Password updated successfully.")
        time.sleep(2)

    def delete_account(self):
        self.print_header("Delete Account")
        self.name = input("Enter your name: ")

        with open(self.accounts_file, 'r') as file:
            lines = file.readlines()

        with open(self.accounts_file, 'w') as file:
            for i in range(0, len(lines), 2):
                if lines[i].strip() != self.name:
                    file.write(lines[i])
                    file.write(lines[i + 1])

        print("Account deleted successfully.")
        time.sleep(2)

    def handle_login(self):
        if not self.check_login():
            print("You need to create an account before logging in.")
            self.create_account()

    def show_menu(self):
        while True:
            self.print_header("CBT System Menu")
            print("1. Take Quiz")
            print("2. Search Data")
            print("3. Create Account")
            print("4. Update Account")
            print("5. Delete Account")
            print("6. View Results")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.handle_login()
                self.take_quiz()
            elif choice == '2':
                self.handle_login()
                self.search_data()
            elif choice == '3':
                self.create_account()
            elif choice == '4':
                self.handle_login()
                self.update_account()
            elif choice == '5':
                self.handle_login()
                self.delete_account()
            elif choice == '6':
                self.handle_login()
                self.view_results()
            elif choice == '7':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    system = CBTSystem()
    system.show_menu()
