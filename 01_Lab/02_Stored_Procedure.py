""" 1. Basit Selamlama
CREATE PROCEDURE Selamla
AS
BEGIN
    PRINT 'Merhaba, bu bir saklı prosedürdür!'
END
 2. Parametre ile Selamlama
CREATE PROCEDURE SelamlaKisi
    @Isim NVARCHAR(50)
AS
BEGIN
    PRINT 'Merhaba ' + @Isim
END

 3. Toplam Hesaplama
CREATE PROCEDURE ToplamHesapla
    @sayi1 INT,
    @sayi2 INT
AS
BEGIN
    PRINT 'Toplam: ' + CAST(@sayi1 + @sayi2 AS VARCHAR)
END

 4. Belirli Bir Öğrenciyi Getirme
CREATE PROCEDURE OgrenciGetir
    @OgrenciID INT
AS
BEGIN
    SELECT * FROM Ogrenciler WHERE OgrenciID = @OgrenciID
END

 5. Yeni Kayıt Ekleme
CREATE PROCEDURE OgrenciEkle
    @Ad NVARCHAR(50),
    @Soyad NVARCHAR(50),
    @DogumTarihi DATE
AS
BEGIN
    INSERT INTO Ogrenciler (Ad, Soyad, DogumTarihi)
    VALUES (@Ad, @Soyad, @DogumTarihi)
END
 6. Kayıt Güncelleme
CREATE PROCEDURE OgrenciGuncelle
    @OgrenciID INT,
    @Ad NVARCHAR(50),
    @Soyad NVARCHAR(50)
AS
BEGIN
    UPDATE Ogrenciler
    SET Ad = @Ad, Soyad = @Soyad
    WHERE OgrenciID = @OgrenciID
END

 7. Kayıt Silme
CREATE PROCEDURE OgrenciSil
    @OgrenciID INT
AS
BEGIN
    DELETE FROM Ogrenciler WHERE OgrenciID = @OgrenciID
END

 8. Toplam Öğrenci Sayısı
CREATE PROCEDURE OgrenciSayisi
AS
BEGIN
    SELECT COUNT(*) AS ToplamOgrenci FROM Ogrenciler
END

🔹 9. Ortalama Not Hesaplama
CREATE PROCEDURE OrtalamaNot
AS
BEGIN
    SELECT AVG(NotDegeri) AS Ortalama FROM Notlar
END

10. Maaşı Belirli Tutarın Üzerinde Olanları Listele
CREATE PROCEDURE YuksekMaasliCalisanlar
    @MaasLimiti MONEY
AS
BEGIN
    SELECT * FROM Calisanlar WHERE Maas > @MaasLimiti
END

 11. Dinamik SQL Kullanımı
CREATE PROCEDURE DinamikSQL
    @TabloAdi NVARCHAR(50)
AS
BEGIN
    EXEC('SELECT * FROM ' + @TabloAdi)
END

 12. Hata Kontrolü ile Kayıt Ekleme
CREATE PROCEDURE HataIleEkle
    @Ad NVARCHAR(50)
AS
BEGIN
    BEGIN TRY
        INSERT INTO Deneme (Ad) VALUES (@Ad)
    END TRY
    BEGIN CATCH
        PRINT 'Bir hata oluştu: ' + ERROR_MESSAGE()
    END CATCH
END

 13. Output Parametresi ile Sonuç Döndürme
CREATE PROCEDURE ToplamDon
    @sayi1 INT,
    @sayi2 INT,
    @sonuc INT OUTPUT
AS
BEGIN
    SET @sonuc = @sayi1 + @sayi2
END
 14. Çoklu Tabloya Ekleme
CREATE PROCEDURE SiparisVeDetayEkle
    @MusteriID INT,
    @UrunID INT,
    @Adet INT
AS
BEGIN
    DECLARE @SiparisID INT

    INSERT INTO Siparis (MusteriID, Tarih)
    VALUES (@MusteriID, GETDATE())

    SET @SiparisID = SCOPE_IDENTITY()

    INSERT INTO SiparisDetay (SiparisID, UrunID, Adet)
    VALUES (@SiparisID, @UrunID, @Adet)
END


 15. IF-ELSE Kullanımı
CREATE PROCEDURE NotDurumu
    @Not INT
AS
BEGIN
    IF @Not >= 50
        PRINT 'Geçtiniz'
    ELSE
        PRINT 'Kaldınız'
END

 16. Tekrarlayan Kayıtları Listeleme
CREATE PROCEDURE TekrarEdenEmail
AS
BEGIN
    SELECT Email, COUNT(*) AS Sayisi
    FROM Kullanicilar
    GROUP BY Email
    HAVING COUNT(*) > 1
END

 17. Tarihe Göre Filtreleme
CREATE PROCEDURE TariheGoreSiparis
    @Baslangic DATE,
    @Bitis DATE
AS
BEGIN
    SELECT * FROM Siparis
    WHERE Tarih BETWEEN @Baslangic AND @Bitis
END

 18. Trigger İle Kullanılan Prosedür
CREATE PROCEDURE LogEkle
    @Aciklama NVARCHAR(100)
AS
BEGIN
    INSERT INTO Loglar (Aciklama, Tarih)
    VALUES (@Aciklama, GETDATE())
END

 19. LIKE Operatörü ile Arama
CREATE PROCEDURE IsmeGoreAra
    @AramaKelimesi NVARCHAR(50)
AS
BEGIN
    SELECT * FROM Ogrenciler
    WHERE Ad LIKE '%' + @AramaKelimesi + '%'
END

 20. View Üzerinden Veri Çekme
CREATE PROCEDURE RaporGetir
AS
BEGIN
    SELECT * FROM vw_OgrenciRaporu
END"""