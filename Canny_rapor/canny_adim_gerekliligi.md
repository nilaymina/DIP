Eğer resimde çok miktarda gürültü bulunursa bunlar kenar olarak algılanabilir. Gürültü bastırma resmi pürüzsüzleştirerek gürültüyü yumuşatır ve buna engel olur. Bu yüzden gürültü bastırma adımı gereklidir.

Sobel filtresi ile hesaplanan gradyan sonuçları non maximum suppression işleminde kullanılır. Eğer bu gradyan hesaplanmazsa non maximum suppression çalışmaz. 

İnce çizgiler şekillerin algılanmasını kolaylaştırdığı için kalın çizgileri non maximum suppression ile ince çizgilere dönüştürürüz. Eğer dönüştürmezsek çizgiler kalın kaldıkları için diğer çizgilerle birleşik gibi gözükürler ve kenarlar yanlış algılanır.

Hysteresis thresholding adımı olmasaydı kenarların daha hafif gözüken parçaları algılanamazdı ya da tam tersi gürültülü kısımlar kenar olarak algılanırdı. Gerçek kenarların düzgünce algılanabilmesi için bu adım gerekli.