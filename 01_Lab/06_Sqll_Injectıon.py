""" Basit SQL Injection Örneği
 Hedef Kod (savunmasız):
SELECT * FROM Kullanicilar WHERE KullaniciAdi = 'admin' AND Sifre = '1234';


 Saldırganın Girişi:
KullaniciAdi: ' OR '1'='1
Sifre:        ' OR '1'='1


 Oluşan Sorgu:
SELECT * FROM Kullanicilar WHERE KullaniciAdi = '' OR '1'='1' AND Sifre = '' OR '1'='1';
Bu sorgu her zaman doğru döner → Tüm kullanıcılar listelenir → Saldırgan giriş yapar.


 Korunma Yöntemleri
 1. Hazır (Parametreli) Sorgular Kullanın
PHP (PDO):
$stmt = $db->prepare("SELECT * FROM Kullanicilar WHERE KullaniciAdi = ? AND Sifre = ?");
$stmt->execute([$kadi, $sifre]);
Python (sqlite3):
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (kadi, sifre))


 2. Stored Procedure Kullan
CREATE PROCEDURE KullaniciGiris
    @kadi NVARCHAR(50),
    @sifre NVARCHAR(50)
AS
BEGIN
    SELECT * FROM Kullanicilar WHERE KullaniciAdi = @kadi AND Sifre = @sifre
END


 3. Girişleri Doğrula / Filtrele
', --, ;, /*, xp_ gibi karakterleri engelle.

Yalnızca beklenen karakterleri kabul et (örneğin, sadece harf ve sayı).

 4. ORM Kullan (Entity Framework, Django ORM vs.)
ORM'ler genellikle parametreli sorgular kullandığı için daha güvenlidir.

 5. Minimum Yetki Prensibi
Veritabanı kullanıcılarına sadece ihtiyaç duyduğu yetkileri verin.

Örneğin: SELECT izni olan kullanıcıya DELETE izni vermeyin.

 SQL Injection Testleri

Giriş Denemesi	Açıklama
' OR '1'='1	Koşulu her zaman doğru yapar
' OR 1=1 --	Sorgunun geri kalanını iptal eder
admin' --	Sadece kullanıcı adı kontrolü
'; DROP TABLE Users;--	Tabloyu silmeye çalışır

 Gerçek Dünya Örneği: Login Sayfası Hatası
SELECT * FROM Users WHERE Username = '$user' AND Password = '$pass';
Kötü giriş:
Username: admin' --
Password: (boş)
Sorguya dönüşür:

SELECT * FROM Users WHERE Username = 'admin' --' AND Password = '';
Yani: Şifre kısmı yorum olarak geçer, sadece admin kontrol edilir ve giriş yapılır.

"""