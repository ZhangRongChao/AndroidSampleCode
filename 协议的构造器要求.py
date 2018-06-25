/*
 在协议的定义中可以规定其遵守者必须提供指定要求的构造器。
 
 协议的构造器要求的语法格式为：init([形参列表])。

 与具体的构造器实现相比，去掉了其花括号和方法体，并且不能为参数设置默认值。
*/
protocol SomeProtocol {
    init()
}

struct SomeStruct: SomeProtocol {
    var someProperty: String
    
    init() {
        someProperty = "SomeValue"
    }
}
