"""1. Basit Başarılı Transaction
BEGIN TRANSACTION

INSERT INTO Ogrenciler (Ad, Soyad) VALUES ('Ahmet', 'Yılmaz')

COMMIT

 2. TRY-CATCH ile Hatalı Transaction
BEGIN TRY
    BEGIN TRANSACTION

    INSERT INTO Ogrenciler (Ad, Soyad) VALUES ('Ali', 'Can')
    -- hata oluşturacak satır
    INSERT INTO Notlar (NotDegeri) VALUES ('Hatalı veri')

    COMMIT
END TRY
BEGIN CATCH
    ROLLBACK
    PRINT ERROR_MESSAGE()
END CATCH

 3. Transaction Rollback Kullanımı
BEGIN TRANSACTION

DELETE FROM Urunler WHERE UrunID = 999

ROLLBACK -- Geri alınır, işlem iptal olur


 4. Sipariş ve Sipariş Detay Ekleme
BEGIN TRANSACTION

DECLARE @SiparisID INT

INSERT INTO Siparis (MusteriID, Tarih) VALUES (5, GETDATE())
SET @SiparisID = SCOPE_IDENTITY()

INSERT INTO SiparisDetay (SiparisID, UrunID, Adet) VALUES (@SiparisID, 3, 2)

COMMIT

 5. İki Tablo Güncelleme
BEGIN TRANSACTION

UPDATE Calisanlar SET Maas = Maas + 1000 WHERE DepartmanID = 1
UPDATE Departmanlar SET Butce = Butce - 50000 WHERE DepartmanID = 1

COMMIT


 6. Not Ekleme ve Ortalama Güncelleme
BEGIN TRANSACTION

INSERT INTO Notlar (OgrenciID, NotDegeri) VALUES (4, 80)

UPDATE Ogrenciler
SET Ortalama = (SELECT AVG(NotDegeri) FROM Notlar WHERE OgrenciID = 4)
WHERE OgrenciID = 4

COMMIT

 7. Stoktan Düş ve Sipariş Oluştur
BEGIN TRANSACTION

UPDATE Urunler SET Stok = Stok - 1 WHERE UrunID = 10

INSERT INTO SiparisDetay (SiparisID, UrunID, Adet) VALUES (1, 10, 1)

COMMIT


 8. Çoklu Satır Silme (Geri Alınabilir)
BEGIN TRANSACTION

DELETE FROM Notlar WHERE NotDegeri < 30

-- kontrol ettikten sonra
COMMIT -- veya ROLLBACK

 9. Eş Zamanlı Güncelleme
BEGIN TRANSACTION

UPDATE BankaHesap SET Bakiye = Bakiye - 1000 WHERE HesapID = 1
UPDATE BankaHesap SET Bakiye = Bakiye + 1000 WHERE HesapID = 2

COMMIT

 10. Tabloda Başarıya Göre Kayıt Durumu Güncelle
BEGIN TRANSACTION

UPDATE Notlar
SET Sonuc = CASE WHEN NotDegeri >= 50 THEN 'Geçti' ELSE 'Kaldı' END

COMMIT


 11. Kullanıcı ve Rolü Ekleme
BEGIN TRANSACTION

INSERT INTO Kullanicilar (KullaniciAdi) VALUES ('mehmet123')
DECLARE @YeniID INT = SCOPE_IDENTITY()

INSERT INTO Roller (KullaniciID, Rol) VALUES (@YeniID, 'Editor')

COMMIT


 12. Aynı Anda Farklı Tablolara Ekleme

BEGIN TRANSACTION

INSERT INTO Kategoriler (KategoriAdi) VALUES ('Elektronik')
INSERT INTO Urunler (UrunAdi, KategoriID) VALUES ('Laptop', SCOPE_IDENTITY())

COMMIT

 13. Hatalı İşlemde Geri Alma
BEGIN TRY
    BEGIN TRANSACTION

    UPDATE Urunler SET Fiyat = -50 WHERE UrunID = 5 -- hatalı fiyat

    COMMIT
END TRY
BEGIN CATCH
    ROLLBACK
    PRINT 'Hata oluştu: ' + ERROR_MESSAGE()
END CATCH


 14. Satın Alma İşlemi
BEGIN TRANSACTION

INSERT INTO Faturalar (MusteriID, Tarih) VALUES (1, GETDATE())
DECLARE @FaturaID INT = SCOPE_IDENTITY()

INSERT INTO FaturaDetay (FaturaID, UrunID, Adet, Fiyat) VALUES (@FaturaID, 10, 2, 1500)

COMMIT


 15. Kullanıcı Silme ve Bağlantılı Verileri Temizleme

BEGIN TRANSACTION

DELETE FROM Roller WHERE KullaniciID = 7
DELETE FROM Kullanicilar WHERE KullaniciID = 7

COMMIT


 16. E-posta Gönderim Kaydı ve Log
BEGIN TRANSACTION

INSERT INTO GonderilenMailler (Alici, Konu) VALUES ('ali@ornek.com', 'Duyuru')
INSERT INTO MailLog (Durum, Tarih) VALUES ('Başarılı', GETDATE())

COMMIT


 17. Ürün Taşıma İşlemi
BEGIN TRANSACTION

UPDATE DepoA SET Stok = Stok - 10 WHERE UrunID = 2
UPDATE DepoB SET Stok = Stok + 10 WHERE UrunID = 2

COMMIT

 18. İzinli Gün Ekleme ve Personel Bilgisi Güncelleme
BEGIN TRANSACTION

INSERT INTO Izinler (PersonelID, Baslangic, Bitis) VALUES (3, '2025-05-01', '2025-05-10')
UPDATE Personeller SET IzinDurumu = 'İzinli' WHERE PersonelID = 3

COMMIT


 19. Otomatik Kod Üretimiyle Ekleme
BEGIN TRANSACTION

DECLARE @Kod NVARCHAR(10) = 'U' + RIGHT('0000' + CAST(NEXT VALUE FOR UrunKodSeq AS NVARCHAR), 5)
INSERT INTO Urunler (Kod, Ad) VALUES (@Kod, 'Tablet')

COMMIT


 20. Kredi Başvurusunda Bakiye ve Başvuru Kaydı
BEGIN TRANSACTION

UPDATE MusteriHesap SET Bakiye = Bakiye + 5000 WHERE MusteriID = 4
INSERT INTO KrediBasvuru (MusteriID, Tutar, Tarih) VALUES (4, 5000, GETDATE())

COMMIT"""