"""
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
   FirstName+SPACE(1)+LastName as FullName,
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
   FirstName+SPACE(1)+LastName as FullName,
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

"""
