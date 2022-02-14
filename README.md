# streamlit快速部署的基于AttnGAN的鸟类生成APP

## **AttnGAN论文**

Pytorch implementation for reproducing AttnGAN results in the paper [AttnGAN: Fine-Grained Text to Image Generation
with Attentional Generative Adversarial Networks](http://openaccess.thecvf.com/content_cvpr_2018/papers/Xu_AttnGAN_Fine-Grained_Text_CVPR_2018_paper.pdf) by Tao Xu, Pengchuan Zhang, Qiuyuan Huang, Han Zhang, Zhe Gan, Xiaolei Huang, Xiaodong He. (This work was performed when Tao was an intern with Microsoft Research). 

论文地址：https://arxiv.org/abs/1711.10485

源码地址：https://github.com/taoxugit/AttnGAN

<u>注：目前该鸟类生成APP AttnGAN部分与源码基本一致，源代码在python 2. 的版本上运行，本项目对其做了些许修改使其在python 3.6环境下成功运行。</u>

## **Streamlit 快速部署**

在code_2022/code/文件夹下新建app.py，编写代码

streamlit 代码编写可参考：

[Streamlit：最快的方式建立和分享数据的工具 - 简书 (jianshu.com)](https://www.jianshu.com/p/e13380072bcb)

## 两种运行方式

- ### 在share.streamlit.io上 运行

  ​	1.将该项目Fork至自己的github主页中

  <img src="E:\Attn-1\AttnGAN-master\READMEimg\fork.png" alt="fork" style="zoom: 50%;" />

  ​	2.找到自己github主页中的app.py文件，复制其网址

  <img src="E:\Attn-1\AttnGAN-master\READMEimg\address.png" alt="address" style="zoom:50%;" />

  ​	3.用github账号登录https://share.streamlit.io/，  选择New app->Paste GitHub URL->粘贴刚刚的app.py网址后Deploy!

  ​	Streamlit Cloud官方教程：	https://docs.streamlit.io/streamlit-cloud/get-started

  

- ### 本地运行

  ​	环境需求：python 3.6

  ​	 1.下载该项目到本地

  ​			首先需要跑通AttnGAN代码，数据集等需要另外下载，其下载链接与存放位置参照博文：[(21条消息) AttnGAN代码复现（详细步骤+避坑指南）文本生成图像_心源易码-CSDN博客](https://blog.csdn.net/air__Heaven/article/details/122458499)

  ​	 2.在终端中进入  code_2022/code/ 目录
  
  ​			可优先运行  python main.py --cfg cfg/eval_bird.yml --gpu 0    （gpu的序号可按本地实际情况更改），查看AttnGAN代码是否顺利跑通。文本在data/birds/example_filenames.txt指定的若干个txt中给出（本项目在此处已做改动），图片结果在models/bird_AttnGAN2/下
  
  ​			原example_filenames.txt中指定文本略多，本地算力不足的可更改该txt中指定文件来减少输入文本
  
  ​			<u>注意预先确定AttnGAN已跑通再进行第三步运行app。</u>
  
  ​     3.在该目录下执行 streamlit run app.py，自动弹出网页
  
  <img src="E:\Attn-1\AttnGAN-master\READMEimg\runapp.png" alt="runapp"  />

## 目前网页运行效果

​			（待后期修改）

![app1](E:\Attn-1\AttnGAN-master\READMEimg\app1.png)

![app2](E:\Attn-1\AttnGAN-master\READMEimg\app2.png)

