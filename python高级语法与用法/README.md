## 枚举
 * from enum import Enum
 * from enum import IntEnum
 ```buildoutcfg
  class VIP(Enum):
        green: 1
        yellow: 2
        black: 3
        red: 4
 ```
 * 23中设计模式  枚举是单例模式
## 进阶知识
 * 为什么需要高阶知识(基础知识已经可以编码)
 * 业务流程开发者,不考虑太多的封装性
 * 包, 类库开发者, 开发包 类库  可以直接拿来用,节约开发效率
## 一切皆对象
 * 函数式编程
 * 闭包
 * 函数: 只是一段可执行的代码, 并不是对象.C#
 * 函数是另外一个函数的参数, 传递到另外的函数里
 * 把一个函数当作另外一个函数的返回结果
 * 委托
### 闭包
 * 函数 + 环境变量
 * 不受外部的环境变量影响
 * 把函数的一个现场保存住
 * python有块级作用域
 * function.__closure__不是None的情况  那么就是这个function有闭包
 * 查看闭包的属性: function.__closure__[0].cell_contents