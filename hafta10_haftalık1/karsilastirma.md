Sparse stereo yöntemi sadece görüntüdeki kenar noktalarını eşleştirdiği için daha az işlem yapıyor ve daha hızlıdır. Ama görüntünün tamamında değil sadece belirli noktalarda disparity değeri oluşturduğu için detaylı bir derinlik haritası elde edilemedi.

Dense stereo yöntemlerinde ise görüntüdeki nerdeyse tüm pikseller eşleştirildiğinden daha detaylı disparity haritaları elde edildi. Ama daha fazla işlem gerektiği için sparse yöntemine göre daha yavaş.

Manuel Block Matching yöntemi her piksel için karşılaştırma yaptığından daha yavaş çalışıyor. OpenCV BM hazır ve optimize edilmiş fonksiyonları kullandığı için manuel BM'ye göre daha hızlı. OpenCV SGBM ise daha fazla hesaplama yapmasına rağmen Manual BM ve OpenCV BM yöntemlerine göre daha düzgün ve doğru sonuçlar verdi.

Yani Sparse stereo hız açısından avantajlıdır ama detay açısından sınırlı. Dense stereo yöntemleri daha detaylı sonuçlar verir. 