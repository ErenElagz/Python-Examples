class Telefon:
    
    def __init__(self,numara):
        
        self.numara = numara
        self.arananlar_listesi = []
        self.toplam_konusma_suresi = 0
       
    def arama_gerceklestir(self,aranan_numara):
        
        sure = int(input("ne kadar konusuldu:"))
        self.toplam_konusma_suresi += sure
        self.arananlar_listesi.append(aranan_numara)
        print(f"{self.numara} numarali telefon sahibi{aranan_numara} numarasını aradı. konusma suresi: {sure}")
        print(f"gerceklesen toplam arama suresi: {self.toplam_konusma_suresi}")
        
        return "telefon numaranız: {}".format(self.telefon)
    
    def aranan_numarayi_arananlardan_sil(self,aranan_numara):
        for i in self.arananlar_listesi:
            if i==aranan_numara:
                self.arananlar_listesi.remove(aranan_numara)
               
    def numarani_goster(self):
        print(f"Telefon numaraniz:{self.numara}")
        

telefon=Telefon("5467900420")

telefon.numarani_goster()
   
telefon.arama_gerceklestir("2311234243")
telefon.arama_gerceklestir("3242342342")


telefon.arananlari_listele()
   
telefon.aranan_numarayi_arananlardan_sil;("2311234243")
telefon.arananlari_listele()