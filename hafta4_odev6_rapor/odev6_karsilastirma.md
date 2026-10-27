Laplacian gauss var filtresinde gauss işlemi parazitleri engellemiş ama sadece parazitleri değil, asıl tespit edilmek istenen keskin hatları ve kenarları da silikleştirmiş. Bu yüzden kenarlar neredeyse görünmez hale gelmiş ve aşırı karanlık kalmış.

Laplacian gauss yok filtresinde, gauss filtresi yapılmadan doğrudan Laplacian uygulandığında görüntüdeki tüm küçük parazitler büyük birer kenar gibi algılanmış. Bu pazaritlerin gücü, gerçek kenarları bastırdığı için geriye kenarlar yerine sadece anlamsız bir parazit topluluğu kalmış.


Sobel ve Prewitt'in Gauss var filtreleri, makro düzeydeki sınırları tespit ederek en temiz ana hat ayrımını sunmuş. 
 Her ikisi de tuğla sınırlarını karanlık zemin üzerinde aydınlık hatlar olarak tespit etmiş ve birbirine oldukça benzer sonuçlar vermiştir.Öncesinde Gauss filtresi uygulandığı için tuğla yüzeyindeki ince detaylar ve gürültüler baskılanmıştır. Bunun sonucunda yüzey pürüzleri ortadan kalkmış, sadece tuğlaları birbirinden ayıran kalın, temiz ve belirgin ana sınır hatları ayrıştırılmıştır.


Sobel ve Prewitt gauss yok filtresinde, Sobel ve Prewitt silinen tuğla yüzeyindeki ince doku pürüzlerini dahi küçük noktacıklar şeklinde kenar olarak algılamış.

LoG filtresi tuğla sınırlarını Sobel ve Prewitt'ten çok daha kesintisiz bir şekilde birleştirmiştir. tuğlaların dikdörtgen formları neredeyse hiçbir kopukluk olmadan izlenebilmektedir. Aynı zamanda LoG doğası gereği yüzeydeki mikro parazitleri filtrelemekte sobel ve prewitt kadar baskın olamamış. LoG işlemi, Düz renkli alanları siyah yaparak sadece görüntüdeki keskin geçişleri ve kenarları ön plana çıkarmış. LoG filtresi, sobel ve prewitte kıyasla parazitlere karşı daha hassas olduğu için   tuğla yüzeyindeki dokular ve pürüzler de kenar olarak algılanmış.