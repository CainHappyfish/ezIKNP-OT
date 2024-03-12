# ezINKP-OT

对于INKP-OT的简单实现

## INKP的基本思路

来源于Mike Rosulek教授在上海期智研究院的密码学学术讲座。

该协议可以使用有限的OTs实现足够多次的OT

假设协议的参与方为接收方Alice和发送方Bob。

- Bob

1. 首先Bob拥有一个随机输入$r$

![](https://pic.imgdb.cn/item/65eff7959f345e8d0389a0b1.png)

2. Bob将其多次扩展为矩阵$R$，矩阵的每一列都相同，宽度可以为128，长度任意

   ![](https://pic.imgdb.cn/item/65eff8069f345e8d038b98c2.png)

3. 对矩阵$R$进行秘密分享，拆分为$T\oplus T'=R$，其中矩阵$T$为随机生成的矩阵。

   ![](https://pic.imgdb.cn/item/65eff8519f345e8d038cd512.png)

- Alice

  1. Alice选择随机串$s$

     ![](https://pic.imgdb.cn/item/65eff8a49f345e8d038e491b.png)

  2. 从列的角度进行OT，Alice得到新的矩阵$Q$

     Alice根据$s_i$从Bob的$(T,T')$选择一列，如果$s_i=0$，从矩阵$T$选择第$i$列，如果$s_i=1$，从矩阵$T'$选择第$i$列，得到矩阵$Q$

     ![](https://pic.imgdb.cn/item/65eff9a29f345e8d0392d299.png)

  3. 我们用$R_{A}$和$R_{B}$分别表示Alice Row和Bob Row，Alice经过128次OT得到的$Q$与Bob拥有的矩阵$T$有如下关系：

     - 当$r_i=0$，有$R_A=R_B$
     - 当$r_i=1$，有$R_A\oplus R_B = s$

     ![](https://pic.imgdb.cn/item/65effaa69f345e8d03975de2.png)

我们再从行的角度来观察Alice和Bob的矩阵。对于每一个$i$，Bob知道$t_i=r_i$，Alice知道$q_i$和$q_i\oplus s$，这两个值中有一个与Bob的$t_i$相同。

![](https://pic.imgdb.cn/item/65effb639f345e8d039a5f30.png)

- Alice不知道Bob的$r_i$值，所以不知道Bob选择的$t_i$到底是和$q_i$相等还是和$q_i\oplus s$相等
- Bob不知道Alice的$s$值，除了知道选择的$t_i$等于$q_i$和$q_i\oplus s$其中一个，而对另一个值一无所知

这里我们需要注意，如果$s_i=0$，则最后的结果与Bob的输入$t_i$无关。

![](https://pic.imgdb.cn/item/65effd619f345e8d03a29bee.png)

由此我们可以得到：

- $r_i = 0 ,q_i = t_i$
- $r_i = 1 , q_i = t_i \oplus s$

不难发现该1-2OT具有一定的线性相关性（Correlation OT），我们需要对这些串执行一个任意的密码学函数$H$：

![](https://pic.imgdb.cn/item/65effd7c9f345e8d03a310fe.png)

由此我们从列的角度坐base OT得到了足够多的行角度的RandomOT。我们只需要将需要进行OT的消息与其进行OTP即可将ROT转化为OT。

## IKNP协议的恶意发送方

- Bob：假设Bob是恶意的

  1. Bob拥有一个输入$r$

  2. 将$r$扩展为矩阵$R$，但恶意翻转$R_2$的第二位bit：

     ![](https://pic.imgdb.cn/item/65effeb89f345e8d03a8540d.png)

  3. 进行秘密分享$(T,T')$，同样$T'$中对应的bit也被翻转

     ![](https://pic.imgdb.cn/item/65effee69f345e8d03a9176c.png)

     我们用$t_i$表示翻转前的行，用$t'_i$表示翻转后的行。

- Alice

  1. 选择随机串$s$

  2. 按IKNP步骤得到矩阵$Q$

     ![](https://pic.imgdb.cn/item/65efffdb9f345e8d03acce98.png)

     由于$r_2 = 0$，本应有$q_i =t_i$，但由于Bob恶意翻转了一位，于是$q_i$和$ t_i$在第二位不同。

所以Alice和Bob使用$H$破坏线性相关性后，Bob会发现得到的$H(Row_2)\neq H(t_2)$，Bob由此得知Alice随机串中的$s_2=1$。以此类推，Bob可以得到完整的$s$。

### 一致性检验

![](https://pic.imgdb.cn/item/65f006979f345e8d03c807bd.png)

## 一般化IKNP OT

将串$r$扩展为矩阵$R$可以看作是一种对$r~bit$的编码方式，所以一般化IKNP的核心思想是用具有差错校正的编码方式对$r$编码。





## 一般化IKNP

