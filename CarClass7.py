class Car:
    def __init__(self ,brand ,model_year):
        self.brand=brand
        self.model_year=model_year
    def Printt(self):
        print(f"Brand is:{self.brand} and model_year is:{self.model_year}")
C1=Car("Speranza",2011)
C1.Printt()
C2=Car("Al-Fattain",2013)
C2.Printt()
