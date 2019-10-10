# 函数
 * round(a, 2): 保留几位小数,a表示被操作的对象,2表示保留两位小数(四舍五入),可以修改
 * 1.功能性
 * 2.隐藏细节
 * 3.避免编写重复的代码
 * return 后面的代码不执行,停止函数代码
### 如何查看内置函数的作用和功能
 * 打开命令行,输入python,进入python解释器,然后输入help(要查询的内置函数)
### Python之禅: import this

## 序列解包
 * result_a, result_b = function(a, b)
 * a,b,c = [1,2,3]
 * 数量要相等
 
## 参数
 * 必须参数
 * 关键字参数
 ```buildoutcfg
 def add(x, y):
    return x + y
  
 c = add(y=3, x=22)
 ```
 * 默认参数(不用传参,形参有默认值)
 ```buildoutcfg
 def add(x=1, y=1):
    return x + y
  
   add()
```
 