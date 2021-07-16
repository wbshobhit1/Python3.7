class Electronic_device:
    info = ["touchpad", "Super-fast-Processor", "Size compatibility", "User Friendly"]

    def is_info(self):
        return f"This device has many things like : {self.info} and these all are characteristics of Electronic device"


class Pocket_gadget(Electronic_device):
    ideal = ["Easy access", "large storage", "High-tech"]

    def is_ideal(self):
        return f"This device has many things like : {self.ideal} and these all are characteristics of Pocket gadgets"


class Phone(Pocket_gadget):
    features = ["Calling", "Internet", "Text", "Gaming", "News and Educational stuff"]

    def is_features(self):
        return f"This device has many things like : {self.features} and these all are characteristics of Phone"


Lappi = Electronic_device()
Cisco = Pocket_gadget()
Apple = Phone()
print("Device Name: Apple")

print(Apple.is_info(), end=" \n")
print(Apple.is_ideal(), end=" \n")
print(Apple.is_features())
