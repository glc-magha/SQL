"""1. LIKE — Belirli bir deseni arama
SELECT * FROM Products
WHERE ProductName LIKE 'Apple%';
"Apple" ile başlayan ürünleri getirir.

2. AVG() — Ortalama fiyatı bulma
SELECT AVG(Price) AS AveragePrice
FROM Products;
Tüm ürünlerin ortalama fiyatını döndürür.

3. MIN() — En düşük fiyatı bulma
SELECT MIN(Price) AS MinPrice
FROM Products;

4. MAX() — En yüksek fiyatı bulma
SELECT MAX(Price) AS MaxPrice
FROM Products;

5. ROUND() — Sonuçları yuvarlama
SELECT ROUND(AVG(Price), 2) AS RoundedAverage
FROM Products;
Ortalama fiyatı virgülden sonra 2 basamak olacak şekilde yuvarlar.


SELECT
    ROUND(AVG(Price), 2) AS AvgPrice,
    MIN(Price) AS MinPrice,
    MAX(Price) AS MaxPrice
FROM Products
WHERE ProductName LIKE '%Laptop%';
İsmi “Laptop” içeren ürünler için ortalama, minimum ve maksimum fiyatı verir.

6. GROUP BY ile birlikte AVG()
SELECT Category, AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category;
Her kategori için ortalama fiyatı verir.

7. HAVING ile grupları filtreleme
SELECT Category, AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category
HAVING AVG(Price) > 30000;
Ortalama fiyatı 30.000 TL'den fazla olan kategorileri getirir.

8. LIKE ile belirli ürünleri gruplama
SELECT Category, COUNT(*) AS Total
FROM Products
WHERE ProductName LIKE '%Apple%'
GROUP BY Category;
İsmi "Apple" geçen ürünleri kategorilere göre sayar.

9. Yuvarlama ile fiyat karşılaştırması
SELECT ProductName, ROUND(Price * 1.18, 2) AS PriceWithTax
FROM Products;
Ürün fiyatlarına %18 KDV ekleyerek virgülden sonra 2 haneli sonucu döndürür.

10. Alt sorgu (Subquery) ile MAX() kullanımı
SELECT * FROM Products
WHERE Price = (SELECT MAX(Price) FROM Products);
En pahalı ürünü getirir.

11. CASE ile Koşullu Değer Atama
SELECT ProductName, Price,
    CASE
        WHEN Price < 20000 THEN 'Ucuz'
        WHEN Price BETWEEN 20000 AND 40000 THEN 'Orta'
        ELSE 'Pahalı'
    END AS FiyatDurumu
FROM Products;
Fiyat aralığına göre ürünleri "Ucuz", "Orta", "Pahalı" şeklinde sınıflandırır.

12. ORDER BY ve LIMIT ile en ucuz 3 ürün
SELECT ProductName, Price
FROM Products
ORDER BY Price ASC
LIMIT 3;
En ucuz 3 ürünü listeler.

13. BETWEEN ile fiyat aralığı sorgulama
SELECT * FROM Products
WHERE Price BETWEEN 20000 AND 40000;
Fiyatı 20.000 ile 40.000 TL arasında olan ürünleri getirir.

14. IN kullanarak belirli kategoriler
SELECT * FROM Products
WHERE Category IN ('Computers', 'Electronics');
Belirli kategorilere ait ürünleri seçer.

15. Fonksiyonlarla birlikte DISTINCT
SELECT COUNT(DISTINCT Category) AS UniqueCategories
FROM Products;
Kaç farklı kategori olduğunu gösterir.

16. Fiyatları yuvarlayıp gruplama
SELECT ROUND(Price, -3) AS RoundedPrice, COUNT(*) AS Count
FROM Products
GROUP BY ROUND(Price, -3)
ORDER BY RoundedPrice;
Fiyatları 1000'e yuvarlayarak gruplar ve o gruplardaki ürün sayısını verir.

17. MAX() ile her kategorideki en pahalı ürünü bulma (correlated subquery)
SELECT *
FROM Products p
WHERE Price = (
    SELECT MAX(Price)
    FROM Products
    WHERE Category = p.Category
);

18. JOIN ile birlikte AVG() kullanımı
Varsayalım iki tablon var:

Products(ProductID, ProductName, CategoryID, Price)

Categories(CategoryID, CategoryName)
SELECT c.CategoryName, ROUND(AVG(p.Price), 2) AS AvgPrice
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;
Her kategori için ortalama fiyatı, kategori adını göstererek getirir.

19. Subquery ile AVG üzeri filtreleme
SELECT * FROM Products
WHERE Price > (
    SELECT AVG(Price) FROM Products
);
Fiyatı tüm ürünlerin ortalamasından yüksek olan ürünleri listeler.

20. Alias ile okunabilirlik
SELECT ProductName AS Ürün, ROUND(Price * 1.2, 2) AS 'KDV Dahil Fiyat'
FROM Products;
Sütunlara Türkçe takma adlar verir.

21. LENGTH() ve LIKE birlikte
SELECT ProductName
FROM Products
WHERE LENGTH(ProductName) > 10 AND ProductName LIKE '%Book%';
İsmi “Book” içeren ve uzunluğu 10 harften fazla olan ürünler.

22. NOW(), DATE(), YEAR() ile tarih fonksiyonları
Varsayalım Orders tablosunda sipariş tarihi var:

Orders(OrderID, ProductID, OrderDate)
SELECT * FROM Orders
WHERE YEAR(OrderDate) = 2024;
2024 yılında verilen siparişleri listeler.

23. Güncel ayın ortalama sipariş sayısı
SELECT COUNT(*) AS SiparisSayisi, ROUND(AVG(p.Price), 2) AS OrtalamaFiyat
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
WHERE MONTH(OrderDate) = MONTH(CURDATE()) AND YEAR(OrderDate) = YEAR(CURDATE());
Bu ayki sipariş sayısı ve ortalama ürün fiyatı.

24. CONCAT() ile metin birleştirme
SELECT CONCAT(ProductName, ' - ', Price, ' TL') AS Detay
FROM Products;
Ürün adını ve fiyatını tek sütunda birleştirerek gösterir.

25. TRIM(), UPPER(), LOWER() örneği
SELECT
  TRIM(ProductName) AS TemizAd,
  UPPER(ProductName) AS BüyükAd,
  LOWER(ProductName) AS KüçükAd
FROM Products;
Ürün adlarını büyük harf, küçük harf ve boşluksuz olarak döndürür.

26. Satışlar tablosu için: En çok satan ürün
Varsayalım:
Sales(SaleID, ProductID, Quantity)
SELECT p.ProductName, SUM(s.Quantity) AS TotalSold
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSold DESC
LIMIT 1;

"""