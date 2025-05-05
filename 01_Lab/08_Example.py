""""###sql example --ders 30
SELECT
     OrderID,
	 FORMAT(OrderDate,'dd.MM.yyyy') as [Order Date],
	 ShipName,
	 ShipCountry
FROM Orders
--tarih formatlama

SELECT
   OrderID,
   UnitPrice,
   Quantity,
   FORMAT(UnitPrice*Quantity*(1-Discount),'C','tr-TR') as Income
FROM [Order Details]

SELECT
    DISTINCT City
fROM Employees

--DISTINCT-->Bir sütundaki verileri tekrar etmeyecek şekilde düzenler
SELECT
     DISTINCT Country
	 FROM Employees

	 --Where:Anahtar sözcüğü ile sorgularımızda filtreler uygulayabiliriz
	 --UNıtprice 20.00 dan büyük olan kayıtları listeleyin



	Select
	ProductName,
	UnitPrice,
	UnitsInStock,
	QuantityPerUnit
	from Products
	where UnitPrice > 20

--	UnitInStock 100 ile 120 arasında olan ürünleri listele
--ProductName,UnitPrice,UnitInStock,QuantityPerUnit

Select
ProductName,
UnitPrice,UnitsInStock,
QuantityPerUnit
from Products
where UnitsInStock BETWEEN 100 and 120
--OrderID,CustomerID,OrderDate gün ay yıl formatında,Freight değeri 32.28 yada 65.83 yada 22.98 olan kayıtlar
SELECT
    OrderID,
    CustomerID,
    OrderDate,
    FORMAT(OrderDate, 'dd.MM.yyyy') AS [Order Date]
FROM Orders
WHERE Freight = 32.28 OR Freight = 65.83 OR Freight = 22.98;
Select*from Orders
--2.yol
SELECT
    OrderID,
    CustomerID,
    CONVERT(nvarchar(10),OrderDate,104)as OrderDate,
	--orderdate sütun verisini sözel bir formata dönüştürdük
	Freight
From Orders
Where Freight In(32.28,65.83,22.98)
--Çok fazla or yazmak yerine in fonk kullanılabilir

--Convert veri tipi değişitrmek için kullanılır
--Çalışanlar içerisinde FirstName Robert olan kaydın
--FullName ve doğum tarihini listeleyin

select
  FirstName+' '+LastName as FullName
  FORMAT(BirthDate, 'dd.MM.yyyy') as BirthDate
from Employees
Where FirstName='Robert'


---Fax ile iletişime geçemediğim müşterileri getir
SELECT
    CompanyName,
	ContactName,
	Region
FROM Customers
WHERE Region IS NULL;

--Country sütunundaki biricik verileri listele,güney amerika harici
--mexico dışında olan müşterilerimin ve regionu null olmayan müşterilerin
--company name,contactname

select

  CompanyName,
  ContactName,
  Region,
  Country
from Customers
WHERE Country NOT IN ('Venezuela', 'Brazil') and Region IS NOT NULL

--Dışarıdan bize gün ay yıl olarak gelen 04.07.1996 ve 04.10.1996 tarihleri arasındaki
--siparişlerin taşıyan kargo firmasının kodu shipvia,shipName,ShipAdress
SELECT
    ShipName,
    ShipAddress,
    ShipVia,
    FORMAT(OrderDate, 'dd.MM.yyyy') AS OrderDate
FROM Orders
WHERE OrderDate BETWEEN '1996-07-04' AND '1996-10-04';

select*from Orders

--Like,AVG(),Min(),Max(),Round() built -in Function

--Dışarıdan bize gün ay yıl olarak gelen yılın ilk çeyreği tarihleri arasındaki rapor
--siparişlerin taşıyan kargo firmasının kodu shipvia,shipName,ShipAdress
---değişken için tip geçiyoruz,kaç karakter barındıracağını belirtiyoruz
DECLARE @startDate NVARCHAR(20)
DECLARE @endDate NVARCHAR(20)

--Değişkene değer atamak için "SET" anahtar kelimesini kullanıyoruz
SET @startDate='01.01.1997'
SET @endDate='31.03.1997'

SELECT
     ShipVia,
	 ShipName,
	 ShipAddress
	 FORMAT(OrderDate, 'dd.MM.yyyy') as OrderDate
FROM Orders
WHERE OrderDate BETWEEN
     Convert(DATETIME,@startDate,104)AND
	 Convert(DATETIME,@endDate,104)

	 --çalışanların yaşlarını hesaplayın,Fullname formatlı,birthdate gene formatlı

	 select
	 FirstName+SPACE(1)+LastName as FullName,
	 FORMAT(BirthDate, 'dd.MM.yyyy') as BirthDate,
	 DATEDIFF(YEAR, BirthDate, GETDATE()) as Age
	 from Employees
	 ORDER BY AGE DESC
	 --Order By ifadesi ile sıralama yapılır
	 --alfabetikde olabilir,asc azdan çoğa,desc çoktan aza

	 select
	 FirstName+SPACE(1)+LastName as FullName,
	 FORMAT(BirthDate, 'dd.MM.yyyy') as BirthDate,
	 DATEDIFF(YEAR, BirthDate, GETDATE()) as Age
	 from Employees
	 WHERE DATEDIFF(YEAR, BirthDate, GETDATE())between 70 and 90

	 --LIKE
	 --like sql de pattern eşleştirmek için kullanılan bir yapıdır
	 --özellikle bir sütun içerisinde bir kalıba yani ifadeye uyan verileri filtrelemetye yarar
	 --bu bağlamda where ifadesi ile birlikte kullanılır
	 --WHERE Column_Name LIKE  '%R'-->örnek bir like kullanımı

	 --soru:Adı r harfi ile başlayan çalışanların fullname,kaç yıldır çalışan olduğunu listele

	 select
	  FirstName + ' ' + LastName AS FullName,
     DATEDIFF(YEAR, HireDate, GETDATE()) AS YearsSinceHire
	 from Employees
	 WHERE FirstName LIKE  'R%'

	 --Select FirstName + SPACE(1) + LastName as FullName, DATEDIFF(
--Year, HireDate, GETDATE()) as YearOfWork, FORMAT(
--HireDate, 'dd/MM/yyyy') as HireDate from Employees where FirstName like 'r%'

select
     FirstName+SPACE(1)+LastName as FullName,
	 FORMAT(HireDate, 'dd.MM.yyyy') as HireDate,
	 DATEDIFF(YEAR, BirthDate, GETDATE()) as Age
from
Employees
WHERE FirstName LIKE  'R%'


--adının son harfi a olan çalışanları listele
select
     FirstName+SPACE(1)+LastName as FullName

   from
Employees
WHERE FirstName LIKE  '%a'

--adının içerisinde a geçen çalışanları listele
---fulname,hiredate,listele
--adan z ye sırala

SELECT
   FirstName+SPACE(1)+LastNamee as FullName,
	 FORMAT(HireDate, 'dd.MM.yyyy') as HireDate
FROM Employees
WHERE FirstName LIKE '%a%'
ORDER BY FullName ASC;


--adının ilk harfi r,3.harfi b,6.harfi t olan çalışanları listele
SELECT
   FirstName+SPACE(1)+LastName as FullName

FROM Employees
WHERE  FirstName LIKE 'R_B__T%';


--ürün adı içinde milk geçmeyen ürünleri stock bilgisine göre sıralayarak listele

select
      ProductName,
	  UnitPrice,
	  UnitsInStock
from Products
where ProductName NOT LIKE'%milk%'
order by UnıtInStock desc


--COLLATE ile büyük küçük harf dengesi


---query performansı nasıl ölçülür ödev



--max
--sum

--Groupby sql de verileri sütuna gör egruplar,grupladığım
--veri kümesini filtrelemek için havıng kullanıyoruz
--hangi kategoride kaç ürün var
select
     CategoryID,
	 Count(ProductID) as ProductAmount
from Products
Group By CategoryID--hangi sütuna göre gruplayacaksan onu burada belirt
order by ProductAmount desc

--havıng
--top
--fetch
--kategorilere göre stok durumu nedir

select
     CategoryID,
	 Sum(ProductID) as TotalStock
from Products
Group By CategoryID
order by TotalStock desc

--hangi tedarikçiden kaç farklı ürün alıyoruz
select*from Products
SELECT
    SupplierID,
    COUNT(DISTINCT ProductID) as ürünsayisi
FROM
    products
GROUP BY SupplierID

ORDER BY
    ürünsayisi DESC;

	--kaç farklı şehirde çalışanım var
	select
	    City,
		COUNT(EmployeeID)as TotalEmployee
	from Employees
	Group by City
	Order by TotalEmployee ASC

	--saydığımız sütunda null varmı dikkat et
	--hangi ülkeden kaç çalışanım var
	select
	Country,

	COUNT(EmployeeID) as ÜlkeSayısı
	from Employees
	Group By Country

	--hangi çalışan kaç tane sipariş vermiş

	select
	   EmployeeID,
	   Count(OrderID) as TotalOrder
	from Orders
	Group by EmployeeID
	Order by TotalOrder desc

	select*from Orders

	--her bir çalışanın gerçekleştirdiği toplam kargo maliyeti

	select
	   EmployeeID,
	   Count(Freight) as TotalPrice
	from Orders
	Group by EmployeeID
	Order by TotalPrice desc

	select*from Orders

	--her bir siparişten ne kadar gelir elde etmişim
	select
	    OrderID,
		SUM(Quantity*UnitPrice*(1-Discount)) as toplamücret

	from [Order Details]
	Group by OrderID


	--kaç farklı ülkeden müşterim var
	select
	top 1
	Country,
	COUNT(Country)as ÜlkeÇeşidi
	from Customers
	Group By Country
	order by ÜlkeÇeşidi


	select*from Customers
	--FETCH NEXT,ROWS
	--Having :groupby sonucunda dönen veri kümesi üzewrinde
	--filtre yapmaya yarar
	--çoğunlukla agreegate fonksiyonlarda

	--soru:100 den fazla sipariş geçtiğim ülkeleri listeleyelim

	SELECt
	     ShipCountry,
		 COUNT(OrderID)as OrderCount
	FROM Orders
	GROUP BY ShipCountry
	HAVING COUNT(OrderID)>100
	ORDER BY OrderCount DESC
	--categorilerime göre 100 ün altındaki stok miktarı


	select
	      CategoryID,
		  SUM(UnitsInStock) as toplamstok
	from Products
	GROUP BY
	     CategoryID
		 HAVING
		 Sum(UnitsInStock)<400
		 order by toplamstok asc

--hangi siparişten ne kadar gelir elde ettik
--geliri 2000 altında olan siparişleri listele
select
    OrderID,
	SUM(UnitPrice*Quantity*(1-Discount))as toplamGelir
from [Order Details]
Group by
    OrderID
HAVING SUM(UnitPrice*Quantity*(1-Discount))<2000
order by toplamGelir desc

--ay ay aylara göre sipariş sayısı nedir
--total sipariş sayısı 200 den büyük ayları listele


select
   MONTH(OrderDate) as Month,
   COUNT(OrderID) as TotalOrder
from Orders
GROUP BY MONTH(OrderDate)
HAVING COUNT(OrderDate)>50
ORDER BY TotalOrder DESC

select*from Orders
--değişkene değer atamak için set
--başlangıç ve bitiş aralıklarını değişkende tanımlayın
--verilen aralıkta sipariş veren müşterileri listeleyin
--örneğin 10 ile 15 sipariş veren müşterileri listele
--pyhtonda string ıdler,sql de nvarchar,int
select*from orders
DECLARE @startQuantity INT
DECLARE @endQuantity INT


SET @startQuantity  =10
SET @endQuantity =15


select CustomerID,
       COUNT(OrderID)as TotalOrder
FROM Orders
Group BY CustomerID
HAVING  COUNT(OrderID)>@startQuantity AND
       COUNT(OrderID)<@endQuantity
ORDER BY TotalOrder desc,CustomerID asc

--çalışanlarımın title bilgisine göre grupla
--yaş ortalamalarını bulalım
select
    Title,
	 AVG(datediff(year, BirthDate, GETDATE())) as OrtalamaYas
FROM  Employees

Group by
     Title
HAVING  AVG(datediff(year, BirthDate, GETDATE())) Between 60 and 80
   --JOIN
   --nedir
   --örnek incele

   --1-inner joın:tablo birleştirme
   --birden fazla tabloya sorgu yazarak veri elde ediyoruz
   --joın işlemi uygulanırken 1.anahtar primary key ve ikinci anahtar
   --foreign key kullanılır
   --inner coin(coin):join edilecek tablolarda eşleşen yada bir başka deyişle kesişen verileri getiir
   --kesişim kümesi
   --2-Left join(left outer join)
   --joine katılan tablolardan soldaki tüm kayıtları ve sağdaki tablodan kesişen kayıtları getiririr
   --3-right coin(right outer join)
   --joine katılan tablolardan sağdaki tüm kayıtları ve sağdaki tablodan kesişen kayıtları getiririr
   --4-Full coin(full outer join) tüm tablolardaki kayıtları getirir
   --eşleşmeyenler null döner
   --5 --cross join :joine katılan tabloları çaprazlar,her bir kayıt biriyle eşleşir

   select
   c.CategoryName,
   p.ProductName,
   p.UnitPrice,
   p.UnitsInStock
   FROM products as p
   INNER JOIN Categories as c ON p.CategoryID=c.CategoryID

   --hangi tedarikçiden hangi ürünü alıyorum
   --supplier tablosundan CompanyName,ContactName,Product tablosundan productname,
   --unıtprice,unıtstock sütunları gelsin

 select
      S.CompanyName,
	  S.ContactName,
	  P.ProductName,
	  P.UnitPrice,
	  P.UnitsInStock
 from Suppliers as S
 JOIN Products as P on S.SupplierID=P.SupplierID
 --hangi siparişi hangi çalışan onaylamış
 --Order tablosundan OrderID,OrderDate gelsin ama formatlı,
 --Employee tablosundan Firstname,lastname gelsin formatlı
 select
   O.OrderID ,
   FORMAT(O.OrderDate,'dd.MM.yyyy')as OrderDate,
  E.FirstName+''+E.LastName as FullName

 from Employees as E
 JOIN Orders as O
 ON E.EmployeeId=O.OrderID

 --hangi siparişi hangi kargo firması taşımış
 --Orders tablosundan OrderID,OrderDate
 --Shıppers Tablosundan CompanyName
 select*from Orders
 select*from Shippers

 SELECT
    O.OrderID,
    O.OrderDate,
	FORMAT(O.OrderDate,'dd.MM.yyyy')as OrderDate,
    S.CompanyName
FROM
    Orders as O
INNER JOIN
    Shippers as S ON O.ShipVia = S.ShipperID

	--hangi kategori altında kaç tane ürünüm var
	SELECT
    C.CategoryName,
    COUNT(P.ProductID) AS ProductSayısı
FROM
    Categories as C
INNER JOIN
    Products as P ON C.CategoryID = P.CategoryID
GROUP BY
    C.CategoryName;

	--hangi ürünü hangi tedarikçiden almışım
	--veriler tekrar etmesin

SELECT
    P.ProductName,
    S.CompanyName
FROM
    Products AS P
INNER JOIN
    Suppliers AS S
	ON P.SupplierID = S.SupplierID
GROUP BY
    P.ProductName,
    S.CompanyName;

	--hangi tedarikçiden ne kadar ürün alıyorum
SELECT
    S.CompanyName,
    COUNT(P.ProductID) AS ProductCount
FROM
    Suppliers AS S
INNER JOIN
    Products AS P
	ON S.SupplierID = P.SupplierID
GROUP BY
    S.CompanyName;
	--kategorilere göre stok durumu nedir
	--kategoriname olmalı,stok bilgisi
	--şu kategoride şu stok var gibi

SELECT
    C.CategoryName,
    SUM(P.UnitsInStock) AS TotalStock
FROM
    Categories AS C
INNER JOIN
    Products AS P
	ON C.CategoryID = P.CategoryID
GROUP BY
    C.CategoryName;

	--en değerli çalışan kim,en çok satışı kim yaptı

select

   E.firstName SPACE(1)+E.LastName as FullName,
   FORMAT(SUM(OD.UnitPrice*OD.Quantity*(1-OD.Dİscount)),'C','tr-TR') as TotalIncome
from employees AS E
JOIN Orders AS O ON E.EmployeeID=O.EmployeeID
JOIN [Order Details] AS OD ON OD.OrderID=O.OrderID
GROUP BY E.EmployeeID,E.FirstName,E.LastName
ORDER BY TotalIncome

-----------------------

	SELECT
    c.CategoryName,
    SUM(OD.Quantity * OD.UnitPrice*(1-OD.Discount)) AS TotalDeğer
FROM [Order Details] AS OD
JOIN Products AS P ON OD.ProductID = P.ProductID
JOIN Categories AS c ON P.CategoryID = c.CategoryID
GROUP BY c.CategoryName
ORDER BY TotalDeğer DESC;

	select*from [Order Details]
--hangi kargocuya ne kadar ödeme yapmışım

select
     s.CompanyName,
	 SUM(O.Freight) as Total
from Orders AS O
JOIN Shippers AS S on O.ShipVia=S.ShipperID
Group BY s.CompanyName
ORDER BY Total DESC


---------------------------------------------
SELECT
    c.CompanyName,
    CAST(SUM(OD.UnitPrice*OD.Quantity*(1-OD.Discount)) AS DECIMAL (18,2) as TotalSales
FROM Customers AS C
JOIN Orders AS O ON C.CustomerID = O.CustomerID
JOIN [Order Details] AS OD  ON OD.OrderID=O.OrderID
GROUP BY c.COmpanyName
HAVING SUM SUM(OD.UnitPrice*OD.Quantity*(1-OD.Discount))<=10000
ORDER BY  SUM(OD.UnitPrice*OD.Quantity*(1-OD.Discount)) DESC

--ÜRÜNLERE GÖRE SATIŞLAR NASIL
SELECT
    P.ProductName,

    SUM(OD.Quantity) AS TotalSatış,
    SUM(OD.Quantity * OD.UnitPrice * (1 - OD.Discount)) AS TotalDeğer
FROM [Order Details] AS OD
JOIN Products AS P ON OD.ProductID = P.ProductID
JOIN Suppliers AS S ON P.SupplierID = S.SupplierID
GROUP BY P.ProductName, S.SupplierName
HAVING  SUM(OD.Quantity)>1000
ORDER BY TotalDeğer DESC;



select*from Products
select*from [Order Details]
select*from Suppliers

-------
---7.ay için hangi müşteriye ne kadar mal satmış
select
      C.CompanyName,
	  SUM(OD.Quantity)as TotalQuantity,
	  FORMAT(SUM(OD.UnitPrice*OD.Quantity*(1-OD.Discount)),'C','en-US')as TotalIncome
from Customers C
JOIN Orders O C.CustomerID=O.CustomerID
JOIN [Order Details] OD ON OD.OrderID=o.OrderID
WHERE O.ShippedDate>=DATEADD(MONTH,-7,GETDATE())
GROUP BY  C.CompanyName
ORDER BY SUM (SUM(OD.UnitPrice*OD.Quantity*(1-OD.Discount))DESC


--left join
SELECT
*
FROM Customers C
LEFT JOIN Orders O  ON O.Customer.ID=C.CustomerID
WHERE O.OrderID is NULL

--tedarikçisi olmayan ürünlerim varmı

SELECT p.ProductID, p.ProductName
FROM Products p
LEFT JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE s.SupplierID IS NULL;
select*from products


--hiç satışı yapılmamış ürünleri listele
select*from [Order Details]
select*from Products
SELECT
   *
FROM Products p
LEFT JOIN [OrderDetails] od ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;
--hiç sipariş gerçekleştirmemiş çalışanlar
SELECT e.EmployeeID, e.FirstName,e.LastName
FROM Orders o
RIGHT JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE o.EmployeeID IS NULL;
select*from Orders
select*from Employees
--Sub Query
--sorgu içinde sorgu yazmamıza imkan veren bir yapıdır.
--nested query diyebiliriz

--en pahalı ürünü yazdırın

SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 1;
select*from Products

SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

SELECT TOP 1  ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC

SELECT CustomerID, CompanyName
FROM Customers
WHERE CustomerID = (
    SELECT CustomerID
    FROM Orders
    GROUP BY CustomerID
    ORDER BY COUNT(OrderID) DESC

	SELECT CustomerID
FROM Customers
WHERE CustomerID= (
    SELECT CustomerID
    FROM Orders
    GROUP BY CustomerID
    ORDER BY COUNT(OrderID) DESC
	select*from Customers
	select*from Orders
	--ortalama fiyatın üstünde satılan ürünleri listele

	SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice> (
    SELECT AVG(UnitPrice)
    FROM Products
)


--en çok sipariş veen müşteri subquery

SELECT TOP 1 CustomerID
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(*) DESC

""""