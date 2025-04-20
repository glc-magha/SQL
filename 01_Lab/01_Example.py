"""1. Tüm kayıtları listele
SELECT * FROM ogrenciler;


 2. Sadece ad ve soyad kolonlarını listele
SELECT ad, soyad FROM ogrenciler;

 3. Yaşı 20 olan öğrencileri listele
SELECT * FROM ogrenciler WHERE yas = 20;


 4. 20 yaşından büyük öğrencileri listele
SELECT * FROM ogrenciler WHERE yas > 20;

 5. Sınıfı 1 olanları listele ve yaşa göre sırala (artan)
SELECT * FROM ogrenciler WHERE sinif = 1 ORDER BY yas ASC;

 6. Yeni öğrenci ekle
INSERT INTO ogrenciler (id, ad, soyad, yas, sinif)
VALUES (5, 'Ahmet', 'Koç', 23, 4);

 7. Yaşı 22 olan öğrencinin adını güncelle
UPDATE ogrenciler SET ad = 'Hasan' WHERE yas = 22;

 8. Sınıfı 3 olan öğrenciyi sil
DELETE FROM ogrenciler WHERE sinif = 3;

 9. Aynı yaştaki öğrencileri gruplandır (kaç kişi var?)
SELECT yas, COUNT(*) AS ogrenci_sayisi FROM ogrenciler GROUP BY yas;

 10. En yüksek yaşlı öğrenciyi getir
SELECT * FROM ogrenciler ORDER BY yas DESC LIMIT 1;

11.SELECT ogrenciler.ad, ogrenciler.soyad, bolumler.bolum_adi
FROM ogrenciler
JOIN bolumler ON ogrenciler.bolum_id = bolumler.id;


 12. GROUP BY ve HAVING kullanımı
Yaşa göre gruplayıp, aynı yaştan 1’den fazla kişi olanları göster:
SELECT yas, COUNT(*) AS kisi_sayisi
FROM ogrenciler
GROUP BY yas
HAVING COUNT(*) > 1;

 13. IN ile filtreleme
SELECT * FROM ogrenciler
WHERE sinif IN (1, 3);

 14. BETWEEN ile aralık sorgulama
SELECT * FROM ogrenciler
WHERE yas BETWEEN 20 AND 22;

 15. NULL değer sorgulama
SELECT * FROM ogrenciler
WHERE soyad IS NULL;

 16. Alt Sorgu (Subquery)
En yüksek yaşa sahip öğrencileri listele:
SELECT * FROM ogrenciler
WHERE yas = (SELECT MAX(yas) FROM ogrenciler);

 17. VIEW (Görünüm) oluşturma
Sadece 1. sınıf öğrenciler için bir görünüm:
CREATE VIEW birinci_sinif_ogrenciler AS
SELECT * FROM ogrenciler WHERE sinif = 1;


⏱ 18. LIMIT ve OFFSET (sayfalamaya uygun)
SELECT * FROM ogrenciler
ORDER BY ad ASC
LIMIT 3 OFFSET 3;


 19. UNIQUE ve COUNT kombinasyonu
Kaç farklı sınıf var?
SELECT COUNT(DISTINCT sinif) FROM ogrenciler;

 20. INDEX oluşturma (performans artırmak için)
CREATE INDEX idx_yas ON ogrenciler(yas);"""