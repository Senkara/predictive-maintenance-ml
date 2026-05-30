# Predictive Maintenance Classification Project

## Proje Amacı

Bu projede makine sensör verileri kullanılarak bir makinenin arıza yapıp yapmayacağının tahmin edilmesi amaçlanmıştır.

Endüstriyel ortamlarda makinelerin arızalanmadan önce tespit edilmesi bakım maliyetlerini azaltmakta ve üretim sürekliliğini artırmaktadır. Bu nedenle Predictive Maintenance (Kestirimci Bakım) uygulamaları büyük önem taşımaktadır.

Bu çalışmada farklı makine öğrenmesi algoritmaları uygulanmış ve performansları karşılaştırılmıştır.

---

## Kullanılan Veri Seti

Projede Predictive Maintenance veri seti kullanılmıştır.

Veri setinde aşağıdaki bilgiler bulunmaktadır:

* Product Type
* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear

Hedef değişken:

* 0 → Arıza Yok
* 1 → Arıza Var

---

## Veri Ön İşleme (Preprocessing)

Model eğitimine başlamadan önce veri üzerinde bazı düzenlemeler yapılmıştır.

### 1. Gereksiz Sütunların Kaldırılması

Aşağıdaki sütunlar model eğitimine doğrudan katkı sağlamadığı için kaldırılmıştır:

* UDI
* Product ID
* Failure Type

**Neden kaldırıldı?**

* UDI yalnızca satır numarasıdır.
* Product ID benzersiz ürün kodudur ve tahmin gücü düşüktür.
* Failure Type ise arıza bilgisini doğrudan içerdiğinden veri sızıntısına (data leakage) neden olabilir.

### 2. Kategorik Verinin Sayısallaştırılması

Type sütunu aşağıdaki şekilde dönüştürülmüştür:

* L → 0
* M → 1
* H → 2

**Neden yapıldı?**

Makine öğrenmesi algoritmaları metinsel veriler yerine sayısal veriler ile çalıştığı için kategorik değişkenlerin sayısallaştırılması gerekmektedir.

### 3. Train-Test Ayrımı

Veri seti:

* %80 Eğitim Verisi
* %20 Test Verisi

olarak ayrılmıştır.

Ayrıca veri seti dengesiz olduğu için `stratify=y` kullanılmıştır.

**Neden yapıldı?**

Arızalı örneklerin oranı oldukça düşüktür. Stratify kullanılarak eğitim ve test verilerinde sınıf dağılımının korunması sağlanmıştır.

---

## Kullanılan Modeller ve Seçilme Nedenleri

### Logistic Regression

İlk olarak Logistic Regression modeli kullanılmıştır.

**Neden seçildi?**

Bu model basit ve yorumlanabilir olduğu için diğer modellerle karşılaştırma yapmak amacıyla temel model (baseline) olarak kullanılmıştır.

---

### Decision Tree

Karar ağacı modeli uygulanmıştır.

**Neden seçildi?**

Karar verme süreci kolay yorumlanabilir ve hangi özelliklerin tahmin üzerinde etkili olduğu daha rahat incelenebilir.

---

### Random Forest

Birden fazla karar ağacının birleşiminden oluşan ensemble öğrenme yöntemidir.

**Neden seçildi?**

Tek bir karar ağacına göre daha kararlı ve güçlü sonuçlar vermektedir. Gürültülü verilerde genellikle daha başarılıdır.

---

### Balanced Random Forest

Random Forest modelinin sınıf dengesizliğini dikkate alan versiyonu kullanılmıştır.

**Neden seçildi?**

Veri setinde arızalı örneklerin oranı düşük olduğu için modelin azınlık sınıfını daha iyi öğrenmesi amaçlanmıştır.

---

### Gradient Boosting

Gradient Boosting modeli uygulanmıştır.

**Neden seçildi?**

Zayıf öğrenicileri ardışık şekilde geliştirerek yüksek doğruluk elde edebilen güçlü bir ensemble yöntemidir.

---

## Değerlendirme Kriterleri

Modeller aşağıdaki metrikler ile değerlendirilmiştir:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Accuracy

Toplam doğru tahmin oranını göstermektedir.

### Precision

Arıza olarak tahmin edilen örneklerin ne kadarının gerçekten arıza olduğunu göstermektedir.

### Recall

Gerçek arızaların ne kadarının yakalanabildiğini göstermektedir.

Bu proje için en önemli metriklerden biridir çünkü amaç arızaları kaçırmamaktır.

### F1-Score

Precision ve Recall değerlerinin dengeli bir birleşimidir.

---

## Feature Importance Analizi

Random Forest modeli kullanılarak özellik önemleri hesaplanmıştır.

Bu analiz sayesinde hangi sensör verilerinin arıza tahmininde daha etkili olduğu incelenmiştir.

Ayrıca sonuçlar grafik ile görselleştirilmiştir.

---

## Sonuç

Bu çalışmada farklı makine öğrenmesi algoritmaları kullanılarak makine arızası tahmini gerçekleştirilmiştir.

Logistic Regression temel karşılaştırma modeli olarak kullanılmış, ardından daha güçlü ağaç tabanlı modeller uygulanmıştır.

Özellikle Random Forest, Balanced Random Forest ve Gradient Boosting modelleri başarılı sonuçlar vermiştir.

Veri setinin dengesiz yapısından dolayı yalnızca doğruluk (accuracy) değeri değil, recall ve F1-score değerleri de değerlendirilmiştir.

Bu proje, kestirimci bakım uygulamalarında makine öğrenmesi yöntemlerinin etkili şekilde kullanılabileceğini göstermektedir.
