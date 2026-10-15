Sobel yapısı, dikey eksende hafif bir Gauss pürüzsüzleştirmesi gerçekleştirdiği için parazitleri kenar olarak algılamaya karşı Prewitt'e kıyasla daha dirençli.

Prewitt yapısı ise çevresel parazite karşı daha hassastır. Görüntüde piksellerin arasında rastgele kirlilikler varsa, Prewitt bu kirlilikleri de kenar olarak algılamaya daha yatkın.

Gauss filtresi görüntüyü önceden yumuşatıp parazitleri azalttığı için her iki operatörün de tespit ettiği kenarlar birbirine oldukça yakın çıkmıştır. Eğer bu Gauss işlemi koda dahil edilmeseydi, Prewitt çıktısında daha fazla istenmeyen parazit görülecekti.

Yatay Sobel ve Dikey Sobel uygulamalarında tuğlaların arasındaki çizgiler kalın görünmektedir. Yatay Sobel yatay çizgileri, Dikey Sobel ise dikey sınırları belirginleştirmiş.

Prewitt filtresi, tuğla duvarı Sobel'e benzer bir şekilde ama daha ince hatlarla göstermiştir. 

Görüntü kendinden parazitliyse, gauss işlemi kısıtlıysa ve kenarların daha belirgin, kalın hatlar halinde vurgulanması hedefleniyorsa Sobel operatörü tercih edilmeli.

Görüntünün kendinden gauss uygulanmış gibi temiz olduğu, parazitten arındırıldığı ve olabildiğince ince, keskin ve daha az yer kaplayan kenar piksellerine ihtiyaç duyulan senaryolarda ise Prewitt operatörü kullanılmalıdır.