/*
 在协议的定义中可以规定其遵守者必须提供指定要求的方法。
 
 协议的方法要求的语法格式为：[static|mutating] func 函数名([形参列表])[->返回值的数据类型]。
 
 如果要求某个方法是类型方法，使用关键字static进行标识。
 
 如果要求某个方法是mutating方法，使用关键字mutating进行标识。
 
 与具体的方法实现相比，去掉了其花括号和方法体，并且不能为参数设置默认值。
 */
protocol SomeProtocol {
    func callInstanceMethod()
    
    static func callTypeMethod()
    
    mutating func callMutatingMethod()
}

struct SomeStruct1: SomeProtocol {
    var someProperty: String = "SomeValue"
    
    func callInstanceMethod() {
        print("callInstanceMethod被调用")
    }
    
    static func callTypeMethod() {
        print("callTypeMethod被调用")
    }
    
    mutating func callMutatingMethod() {
        someProperty = "NewSomeValue"
        print("callMutatingMethod被调用")
    }
}
