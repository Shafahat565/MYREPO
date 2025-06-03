class Maliks:
    def __init__(self, Mal):
        self.Mal = Mal

class Awans(Maliks):
    def __init__(self, Mal, Awa):  # Adjusted to accept two arguments
        self.Awa = Awa
        super().__init__(Mal)  # Passing Mal to the parent class's __init__

Masar = Awans("Malikho", "Awano")
print(Masar.Mal)
print(Masar.Awa)
