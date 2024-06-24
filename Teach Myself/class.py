class Kelas:
    def __init__(self):
        self.murid = {}
    
    def masukinMurid(self, murid) -> None:
        self.murid.add(murid)
    
    def semuaMurid(self):
        return self.murid
    
    def kickMurid(self, murid):
        self.murid.remove(murid)
    
    
        
apel = Kelas()

pisang = Kelas()

apel.masukinMurid("Budi")
apel.masukinMurid("Wati")
apel.masukinMurid("Koko")

pisang.masukinMurid("Albert")
pisang.masukinMurid("Jason")
pisang.masukinMurid("Brili")
pisang.masukinMurid("Brendi")
pisang.masukinMurid("Dio")

print(apel.semuaMurid())
print(pisang.semuaMurid())

pisang.kickMurid("Dio")

print(pisang.semuaMurid())

