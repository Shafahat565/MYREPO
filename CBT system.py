class CBP_Paper:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.points = 0

    def paper(self):
        print("Computer Science Quiz:")
        print("1. What is the time complexity of the Bellman-Ford algorithm?")
        print("   A) O(V)")
        print("   B) O(V^2)")
        print("   C) O(V^3)")
        print("   D) O(EV)")
        answer = input("Your answer: ").lower()
        if answer == "d":
            self.points += 1

        print("2. Which sorting algorithm has the best average-case time complexity?")
        print("   A) Quick sort")
        print("   B) Merge sort")
        print("   C) Heap sort")
        print("   D) Insertion sort")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("3. What is the primary purpose of dynamic programming?")
        print("   A) To solve optimization problems by breaking them into subproblems")
        print("   B) To generate test cases for software testing")
        print("   C) To interpret high-level languages")
        print("   D) To allocate memory dynamically during program execution")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("4. Which data structure is typically used to implement a priority queue?")
        print("   A) Array")
        print("   B) Linked List")
        print("   C) Heap")
        print("   D) Stack")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("5. What is the purpose of the A* search algorithm?")
        print("   A) To find the shortest path in a weighted graph")
        print("   B) To perform pattern matching in strings")
        print("   C) To determine the maximum flow in a network")
        print("   D) To generate permutations of a set")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("6. Which algorithm is used for finding strongly connected components in a graph?")
        print("   A) Dijkstra's algorithm")
        print("   B) Kosaraju's algorithm")
        print("   C) Floyd-Warshall algorithm")
        print("   D) Bellman-Ford algorithm")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("7. What is the main advantage of using a hash table for data storage?")
        print("   A) Constant time complexity for most operations")
        print("   B) Efficient use of memory")
        print("   C) Automatic resizing of the data structure")
        print("   D) Ability to store data in sorted order")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("8. Which graph traversal algorithm is used to detect cycles in a graph?")
        print("   A) Depth-first search")
        print("   B) Breadth-first search")
        print("   C) Dijkstra's algorithm")
        print("   D) Prim's algorithm")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("9. What is the primary advantage of using a self-balancing binary search tree?")
        print("   A) Guaranteed worst-case time complexity for search operations")
        print("   B) Ability to efficiently store large amounts of data")
        print("   C) Automatic resizing of the tree structure")
        print("   D) Balanced height for improved performance")
        answer = input("Your answer: ").lower()
        if answer == "d":
            self.points += 1

        print("10. Which algorithm is used to find the maximum flow in a flow network?")
        print("    A) Kruskal's algorithm")
        print("    B) Prim's algorithm")
        print("    C) Bellman-Ford algorithm")
        print("    D) Ford-Fulkerson algorithm")
        answer = input("Your answer: ").lower()
        if answer == "d":
            self.points += 1
        print("Software Engineering Quiz:")
        print("1. What is the primary goal of software architecture?")
        print("   A) To minimize development costs")
        print("   B) To maximize code readability")
        print("   C) To ensure system reliability")
        print("   D) To improve software maintainability")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("2. Which software development model relies heavily on customer interaction and iterative development?")
        print("   A) Waterfall model")
        print("   B) Spiral model")
        print("   C) Agile model")
        print("   D) V-model")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("3. What is the purpose of version control systems in software engineering?")
        print("   A) To track changes to source code")
        print("   B) To generate test cases automatically")
        print("   C) To analyze software performance")
        print("   D) To execute test cases")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("4. Which software testing technique involves executing the program with the intent of finding errors?")
        print("   A) Black-box testing")
        print("   B) White-box testing")
        print("   C) Integration testing")
        print("   D) System testing")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("5. What is the purpose of a use case diagram in software engineering?")
        print("   A) To describe the interactions between system components")
        print("   B) To visualize the flow of data within the system")
        print("   C) To represent the functionality of the system from a user's perspective")
        print("   D) To model the behavior of individual classes")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("6. Which software development principle states that software components should be open for extension but closed for modification?")
        print("   A) Single Responsibility Principle")
        print("   B) Liskov Substitution Principle")
        print("   C) Open/Closed Principle")
        print("   D) Interface Segregation Principle")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("7. What is the purpose of a UML (Unified Modeling Language) class diagram in software engineering?")
        print("   A) To model the dynamic behavior of a system")
        print("   B) To represent the relationships between classes")
        print("   C) To visualize the sequence of interactions between objects")
        print("   D) To specify the system's internal structure")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("8. Which software development methodology emphasizes the importance of delivering working software frequently?")
        print("   A) Waterfall model")
        print("   B) Scrum")
        print("   C) V-model")
        print("   D) Extreme Programming (XP)")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("9. What is the purpose of a software requirements specification document?")
        print("   A) To describe how the system will be implemented")
        print("   B) To outline the testing procedures for the system")
        print("   C) To define the functional and non-functional requirements of the system")
        print("   D) To document the system's architecture")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("10. Which software design pattern is used to ensure that only one instance of a class is created?")
        print("    A) Singleton pattern")
        print("    B) Factory pattern")
        print("    C) Observer pattern")
        print("    D) Prototype pattern")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1
        print("Computer Engineering Quiz:")
        print("1. Which logic gate is used to perform addition in digital circuits?")
        print("   A) AND gate")
        print("   B) OR gate")
        print("   C) XOR gate")
        print("   D) NOT gate")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("2. What is the function of a multiplexer in digital electronics?")
        print("   A) To perform arithmetic operations")
        print("   B) To combine multiple signals into one")
        print("   C) To synchronize clock signals")
        print("   D) To store data temporarily")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("3. Which type of memory is non-volatile and retains its data even when the power is turned off?")
        print("   A) RAM (Random Access Memory)")
        print("   B) ROM (Read-Only Memory)")
        print("   C) Cache memory")
        print("   D) Virtual memory")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("4. What is the purpose of a finite state machine in digital systems?")
        print("   A) To perform arithmetic calculations")
        print("   B) To control the flow of data")
        print("   C) To synchronize clock signals")
        print("   D) To implement sequential logic")
        answer = input("Your answer: ").lower()
        if answer == "d":
            self.points += 1

        print("5. Which component of a microprocessor is responsible for executing instructions?")
        print("   A) ALU (Arithmetic Logic Unit)")
        print("   B) Control unit")
        print("   C) Cache memory")
        print("   D) Registers")
        answer = input("Your answer: ").lower()
        if answer == "b":
            self.points += 1

        print("6. What is the function of an FPGA (Field-Programmable Gate Array) in computer engineering?")
        print("   A) To implement custom digital logic circuits")
        print("   B) To store large amounts of data permanently")
        print("   C) To convert analog signals to digital signals")
        print("   D) To amplify electrical signals")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("7. Which digital modulation technique is commonly used in wireless communication systems?")
        print("   A) Amplitude modulation (AM)")
        print("   B) Frequency modulation (FM)")
        print("   C) Pulse Code Modulation (PCM)")
        print("   D) Quadrature Amplitude Modulation (QAM)")
        answer = input("Your answer: ").lower()
        if answer == "d":
            self.points += 1

        print("8. What is the function of a clock signal in digital systems?")
        print("   A) To synchronize the operations of different components")
        print("   B) To amplify electrical signals")
        print("   C) To convert digital signals to analog signals")
        print("   D) To store data temporarily")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1

        print("9. Which networking protocol is used to assign IP addresses dynamically to devices on a network?")
        print("   A) TCP (Transmission Control Protocol)")
        print("   B) UDP (User Datagram Protocol)")
        print("   C) DHCP (Dynamic Host Configuration Protocol)")
        print("   D) DNS (Domain Name System)")
        answer = input("Your answer: ").lower()
        if answer == "c":
            self.points += 1

        print("10. What is the purpose of an oscilloscope in computer engineering?")
        print("    A) To measure and display voltage signals")
        print("    B) To perform logic operations")
        print("    C) To debug software code")
        print("    D) To analyze network traffic")
        answer = input("Your answer: ").lower()
        if answer == "a":
            self.points += 1
        return self.points
        
    def function_data(self):
        with open("student_data.txt", "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Roll Number: {self.roll_number}\n")
            file.write(f"Marks: {self.points}\n")    

# Example usage:
student = CBP_Paper("John Doe", 12345)
print("Total points in Computer Science:",student.paper())