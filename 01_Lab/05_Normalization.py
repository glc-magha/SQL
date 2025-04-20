"""SQL Normalizasyon Nedir?
Veritabanı tablolarını bölerek ve ilişkiler kurarak veri tekrarını (redundancy) ortadan kaldırma işlemidir.

Amaç: Veri bütünlüğü sağlamak ve güncelleme/anormallikleri önlemektir (insert/update/delete anomalies).



Normalizasyon Aşamaları (Forms)
 1NF (First Normal Form - Birinci Normal Form)
Tüm sütunlar atomik (bölünemez) olmalı.

Tekrarlayan veri grupları olmamalı.



2NF (Second Normal Form - İkinci Normal Form)
1NF sağlanmış olmalı.

Tüm sütunlar, tüm aday anahtarlara tam bağımlı olmalı. (Kısmi bağımlılık olmamalı)



3NF (Third Normal Form - Üçüncü Normal Form)
2NF sağlanmış olmalı.

Hiçbir sütun transitif bağımlı olmamalı. (Yani, bir alan başka bir alan üzerinden birincil anahtara bağlı olmamalı.)



Ekstra Normal Formlar
BCNF (Boyce–Codd Normal Form): 3NF'e çok benzer ama daha katı.

4NF: Çok değerli bağımlılıkları ortadan kaldırır.

5NF: Parçalanabilirliği ele alır (mükemmel ayrıştırma)."""