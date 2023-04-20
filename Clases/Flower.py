class flower():
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        """Returns the name of the flower"""
        return self._name

    def get_petals(self):
        """Returns the amount of petals of the flower"""
        return self._petals

    def get_price(self):
        """Returns the price of the flower"""
        return self._price

    def set_name(self, newName):
        """Sets the name of the flower"""
        self._name = newName

    def set_petals(self, newPetals):
        """Sets the amount of petals of the flower"""
        self._petals = newPetals

    def set_price(self, newPrice):
        """Sets the price of the flower"""
        self._price = newPrice

    def __str__(self):
        return f"{self._name} is a flower with {self._petals} petals and it costs ${self._price}."
    
#########################################
testFlower = flower("Rose", 5, 12.60)
print(testFlower)
testFlower.set_name("Jazmin")
print(testFlower.get_name())

