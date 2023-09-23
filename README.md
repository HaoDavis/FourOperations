| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| :-----------------: |:---------------: |
| 这个作业要求在哪里| [结对项目](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13016) |
| 这个作业的目标 |熟悉多人协作|

成员👨‍💻：**戴子豪**3121004649、**朱俊荣**3121004677

GitHub项目地址🔗：https://github.com/HaoDavis/FourOperations
# 效能分析

# 设计实现过程
# 代码说明
# 测试运行
# 项目小结
朱俊荣：is_same函数一开始用暴力法遍历表达式列表，来寻找是否有与新生成出表达式相同的表达式，但效率很低，因为is_same底层调用了便利二叉树的函数。后来将表达式列表里的每一个表达式都转换为一个hash，然后对于已经产生hash的表达式，在后续的判断中就不需要重新遍历他们，这样就将程序运行时间减半。另外答案检查函数中的zip手法也提高了效率。另外，这个项目非常综合，考察到了很多方面的内容，有一些规则的判定并没有现成的算法可以参考，需要自己试错。我的伙伴有很好的python语法功底，也很熟练地使用git和一些测试工具，让我们的开发效率大大提高。深刻感受到，很多bug若是两个人在一起观察讨论就很容易解决，达到一加一远大于二的效果。
# 附录
## PSP表格
|**PSP2.1**|**Personal Software Process Stages**| **预估耗时（分钟）** |**实际耗时（分钟）**|
| :------------: | :------------: |:------------:| :------------: |
|Planning|计划|      60      |30|
|Estimate|估计这个任务需要多少时间|      30      |10|
|Development|开发|     400      |200|
|Analysis|需求分析 (包括学习新技术)|      60      |30|
|Design Spec|生成设计文档|     120      |45|
|Design Review|设计复审|      60      |15|
|Coding Standard|代码规范 (为目前的开发制定合适的规范)|      30      |10|
|Design| 具体设计|      60      |20|
|Coding|具体编码|     300      |120|
|Code Review|代码复审|      30      |5|
|Test|测试（自我测试，修改代码，提交修改）|      60      |20|
|Reporting|报告|      60      |20|
| Test Repor|测试报告|      30      |10|
| Size Measurement|计算工作量|      20      |5|
|Postmortem & Process Improvement Plan|事后总结, 并提出过程改进计划|      60      |5  |
|Total|合计|     1380     |525|

## 参考
- [Jieba : Python 中文分词组件](https://github.com/fxsjy/jieba)
- [Gensim 中文文档](https://gensim.apachecn.org/)
- [re --- 正则表达式操作](https://docs.python.org/zh-cn/3/library/re.html)
- [unittest --- 单元测试框架](https://docs.python.org/zh-cn/3/library/unittest.html)
