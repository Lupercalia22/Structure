
class Pump:
    def __init__(self, pump_type):
        self.pump_type = pump_type

    def find_h(self, k):
        return f"Имеем: {k}\nИщем: h = {-k} ед."

    def find_k(self, h):
        return f"Имеем: {h}\nИщем: k = {-h} ед."

    def pump(self, h=0, k=0):
        if self.pump_type == "centrifugal":
            print("Тип насоса: центробежный")
            print(self.find_h(h if h else k))
        else:
            print("Тип насоса: плунжерный")
            print(self.find_k(h if h else k))
        print()

centrifugal_pump = Pump("centrifugal")
plunger_pump = Pump("plunger")

centrifugal_pump.pump(k=5)
plunger_pump.pump(h=25)


