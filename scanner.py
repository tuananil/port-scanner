import socket
def port_tara(hedef_ip, port):
    try:
        # socket.socket() ile bir ağ bağlantı aracı oluşturuyoruz
        # AF_INET = IPv4 kullanacağız demek
        # SOCK_STREAM = TCP bağlantısı kullanacağız demek
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Hızlı olması için: 1 saniye içinde cevap gelmezse geç (Zaman aşımı)
        s.settimeout(1.0)
        
        # Verilen IP ve Port'a bağlanmayı dene
        sonuc = s.connect_ex((hedef_ip, port))
        
        # connect_ex eğer 0 dönerse bağlantı başarılı (port açık) demektir
        if sonuc == 0:
            print(f" [+] Port {port}: AÇIK")
        
        # İşimiz bitince bağlantıyı kapatıyoruz
        s.close()
        
    except:
        # Eğer bir hata oluşursa hiçbir şey yapma, devam et
        pass
    # Ana program başlangıcı
if __name__ == "__main__":
    # Kullanıcıdan hedefi alıyoruz (Örn: localhost veya kendi test IP'n)
    hedef = input("Taramak istediğiniz IP veya Web Adresini girin: ")
    
    # İsmi IP adresine çeviriyoruz (Örn: google.com yazılırsa IP'sini bulur)
    hedef_ip = socket.gethostbyname(hedef)
    
    print("-" * 50)
    print(f"Hedef IP: {hedef_ip} taranıyor...")
    print("-" * 50)
    
    # 1'den 100'e kadar olan popüler portları sırayla tara (İstersen aralığı değiştirebilirsin)
    for port in range(1, 101):
        port_tara(hedef_ip, port)
        
    print("\nTarama işlemi tamamlandı!")