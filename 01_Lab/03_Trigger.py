"""1. Ekleme Sonrası Log Tutma
CREATE TRIGGER LogEkleme
ON Ogrenciler
AFTER INSERT
AS
BEGIN
    INSERT INTO Log (Aciklama, Tarih)
    SELECT 'Yeni öğrenci eklendi: ' + Ad, GETDATE()
    FROM inserted
END


 2. Güncelleme Sonrası Log

CREATE TRIGGER LogGuncelleme
ON Ogrenciler
AFTER UPDATE
AS
BEGIN
    INSERT INTO Log (Aciklama, Tarih)
    SELECT 'Öğrenci güncellendi: ' + Ad, GETDATE()
    FROM inserted
END


 3. Silme Sonrası Log
CREATE TRIGGER LogSilme
ON Ogrenciler
AFTER DELETE
AS
BEGIN
    INSERT INTO Log (Aciklama, Tarih)
    SELECT 'Öğrenci silindi: ' + Ad, GETDATE()
    FROM deleted
END

 4. Maaş Limiti Aşımı Kontrolü
CREATE TRIGGER MaasKontrol
ON Calisanlar
INSTEAD OF INSERT
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted WHERE Maas > 10000)
        RAISERROR('Maaş limiti aşıldı!', 16, 1)
    ELSE
        INSERT INTO Calisanlar SELECT * FROM inserted
END

 5. İki Tabloyu Senkron Tutma (Ekleme)
CREATE TRIGGER MusteriEkleme
ON Musteriler
AFTER INSERT
AS
BEGIN
    INSERT INTO MusteriDetay (MusteriID)
    SELECT MusteriID FROM inserted
END


 6. Not Güncellemesiyle Ortalamayı Yenileme
CREATE TRIGGER OrtalamaGuncelle
ON Notlar
AFTER INSERT, UPDATE
AS
BEGIN
    UPDATE Ogrenciler
    SET Ortalama = (
        SELECT AVG(NotDegeri)
        FROM Notlar
        WHERE Notlar.OgrenciID = Ogrenciler.OgrenciID
    )
    FROM Ogrenciler
    INNER JOIN inserted ON Ogrenciler.OgrenciID = inserted.OgrenciID
END
 7. Kullanıcı Silinince Girişlerini Sil
CREATE TRIGGER KullaniciSilGirisSil
ON Kullanicilar
AFTER DELETE
AS
BEGIN
    DELETE FROM Girisler
    WHERE KullaniciID IN (SELECT KullaniciID FROM deleted)
END


 8. Güncellenen Alanları Logla
CREATE TRIGGER AlanDegisimiLog
ON Calisanlar
AFTER UPDATE
AS
BEGIN
    INSERT INTO DegisimLog (AlanAdi, EskiDeger, YeniDeger, Tarih)
    SELECT 'Maas', d.Maas, i.Maas, GETDATE()
    FROM inserted i
    JOIN deleted d ON i.CalisanID = d.CalisanID
    WHERE i.Maas != d.Maas
END


 9. Birden Fazla Satır Eklemesini Engelle
CREATE TRIGGER TekSatirEkleme
ON Siparis
INSTEAD OF INSERT
AS
BEGIN
    IF (SELECT COUNT(*) FROM inserted) > 1
        RAISERROR('Aynı anda sadece bir sipariş eklenebilir!', 16, 1)
    ELSE
        INSERT INTO Siparis SELECT * FROM inserted
END
 10. Negatif Stok Kontrolü
CREATE TRIGGER StokKontrol
ON Urunler
AFTER UPDATE
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted WHERE Stok < 0)
        ROLLBACK TRANSACTION
END

 11. Otomatik Tarih Güncellemesi
CREATE TRIGGER TarihGuncelle
ON Siparis
AFTER INSERT
AS
BEGIN
    UPDATE Siparis
    SET Tarih = GETDATE()
    WHERE SiparisID IN (SELECT SiparisID FROM inserted)
END

 12. Email Formatını Kontrol Ete
CREATE TRIGGER EmailKontrol
ON Kullanicilar
INSTEAD OF INSERT
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted WHERE Email NOT LIKE '%@%.%')
        RAISERROR('Geçersiz email formatı!', 16, 1)
    ELSE
        INSERT INTO Kullanicilar SELECT * FROM inserted
END


 13. Silinmeden Önce Onay Logu
CREATE TRIGGER SilmeOncesiLog
ON Urunler
INSTEAD OF DELETE
AS
BEGIN
    INSERT INTO OnayBekleyenSilme (UrunID, Ad, Tarih)
    SELECT UrunID, Ad, GETDATE()
    FROM deleted
END

 14. Fiyat Düşüşünü Logla
CREATE TRIGGER FiyatDususuLog
ON Urunler
AFTER UPDATE
AS
BEGIN
    INSERT INTO FiyatLog (UrunID, EskiFiyat, YeniFiyat, Tarih)
    SELECT i.UrunID, d.Fiyat, i.Fiyat, GETDATE()
    FROM inserted i
    JOIN deleted d ON i.UrunID = d.UrunID
    WHERE i.Fiyat < d.Fiyat
END

 15. Yedek Tabloda Saklama
CREATE TRIGGER SilinenleriYedekle
ON Ogrenciler
AFTER DELETE
AS
BEGIN
    INSERT INTO OgrenciYedek
    SELECT * FROM deleted
END

 16. Kullanıcı Girişi Kaydet
CREATE TRIGGER GirisLog
ON Girisler
AFTER INSERT
AS
BEGIN
    INSERT INTO Loglar (Aciklama, Tarih)
    SELECT 'Kullanıcı girişi: ' + CAST(KullaniciID AS NVARCHAR), GETDATE()
    FROM inserted
END


 17. Aynı Ürün Adını Engelle
CREATE TRIGGER TekilUrunAdi
ON Urunler
INSTEAD OF INSERT
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted WHERE Ad IN (SELECT Ad FROM Urunler))
        RAISERROR('Bu ürün adı zaten mevcut!', 16, 1)
    ELSE
        INSERT INTO Urunler SELECT * FROM inserted
END

 18. Sipariş Miktarı Kontrolü
CREATE TRIGGER SiparisStokKontrol
ON SiparisDetay
AFTER INSERT
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM inserted i
        JOIN Urunler u ON i.UrunID = u.UrunID
        WHERE i.Adet > u.Stok
    )
        ROLLBACK TRANSACTION
END


 19. Güncelleme Zamanını Sakla
CREATE TRIGGER GuncellemeZamani
ON Urunler
AFTER UPDATE
AS
BEGIN
    UPDATE Urunler
    SET GuncellemeTarihi = GETDATE()
    WHERE UrunID IN (SELECT UrunID FROM inserted)
END


 20. Silme İzni Olmayan Kullanıcı Kontrolü
CREATE TRIGGER SilmeYetkisi
ON Calisanlar
INSTEAD OF DELETE
AS
BEGIN
    IF SYSTEM_USER <> 'admin'
        RAISERROR('Sadece admin silme işlemi yapabilir!', 16, 1)
    ELSE
        DELETE FROM Calisanlar WHERE CalisanID IN (SELECT CalisanID FROM deleted)
END"""