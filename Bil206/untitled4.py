from PIL import Image

def resmi_getir(resim):
    goruntu = Image.open(resim)    
    return goruntu
    
def resmi_goster(resim):
    resim.show()

def resmi_farkli_isimle_kaydet():
    yeni_supra = Image
    yeni_supra = resmi_getir() 
    yeni_supra.save("cıktı.png")
    
resmi_goster(resmi_getir("indir.jpg"))

resmi_farkli_isimle_kaydet("yeni.jpg")
