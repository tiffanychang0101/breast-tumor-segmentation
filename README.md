# Breast tumor segmentation using U-Net
乳房磁振造影（MRI）具有極優異軟組織解析度與對比的優點，可用於觀察組織性質、腫瘤顯影特性等有效的特徵，本專題利用磁振造影觀察乳房組織及腫塊顯影特徵，結合深度學習的優勢，使用卷積神經網路架構建立腫瘤的輪廓描繪程序，提供擷取乳房腫瘤重要特徵，提供醫生施行治療的參考，以期提高乳癌治癒的機會，研究目的如下：

1.	提升醫師判讀影像之效率和降低人為差異
2.	幫助患者能得到更加快速、更準確的診斷結果和治療方法
3.	改善醫療院所診療速度以及加速醫療系統流程

## 開發環境及工具
以Keras作為深度學習的工具，它能夠以Tensorflow做為後端運行

## 採用的網路架構：U-Net
損失函數（Loss function）：交叉熵（cross-entropy）
優化器（optimizer）：隨機梯度下降法（SGD）

模型在每一層卷積層後方加入Rectifier Linear Unit（ReLU）作為激活函數，並在兩層卷積層中間加入0.2的dropout。

此神經網路的訓練是在每張影像上採數個patch的方式進行，每個patch的維度是48*48，採取的方式為在每一張訓練影像中設立許多隨機的中心點，每張影像採9500個Patches。

共使用10個乳房磁振造影病例: 每病例各3張，共30張。其中10張做為測試集，20張為訓練集。故每次訓練集中的影像將會有190000個Patches產生，並將其中90%作為訓練用（171000 Patches），10%作為驗證用（19000 Patches）。實驗共訓練150個epoches，mini-batch的大小為32個patches，即以每32個patches作為一個小批次訓練，這樣子的方式會比直接用全部的patches做梯度下降來的快速。

訓練時以循環的方式進行，將所有樣本分為三大群A、B、C，每群為10張。即當A群為測試集時，B與C為訓練集；當B群為測試集時，A與C為訓練集；當C群為測試集時，A與B為訓練集。我們使用的顯示卡為GTX 1070 Ti，每一循環大約花一個禮拜的時間來做訓練。

## 結果
![1](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare1.png)
![2](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare2.png)
![3](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare3.png)
![4](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare4.png)
![5](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare5.png)
![6](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare6.png)
![7](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare7.png)
![8](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare8.png)
![9](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare9.png)
![10](https://github.com/tiffanychang0101/breast-tumor-segmentation/blob/master/breast-tumor-segmentation/tumor_segmentation/150_epoches/testcompare10.png)
