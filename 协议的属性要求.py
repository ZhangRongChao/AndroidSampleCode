/*
 在协议的定义中可以规定其遵守者必须提供指定要求的属性。
 
 协议的属性要求的语法格式为：
 [static] var 属性名: 属性类型 { get [set] }
 
 在协议的属性要求中，如果要求某个属性是类型属性，使用关键字static进行标识。
 
 必须使用关键字var对属性名进行标识，而不能使用关键字let。
 
 如果要求某个属性是可读写的，在变量的类型声明后添加{ get set }；
 如果要求某个属性是只读的，在变量的类型声明后添加{ get }。
 
 协议的属性要求包括：
 a. 实例属性还是类型属性
 b. 只读的还是可读写的
 协议的属性要求不包括：存储属性还是计算属性。
 */
protocol SomeProtocol {
    var ipgs: String { get set }
    
    var ipg: String { get }
    
    static var tpgs: String { get set }
    
    static var tpg: String { get }
}

struct SomeStruct: SomeProtocol {
    var ipgs: String {
        get {
            return "IPGS"
        }
        
        set {
            
        }
    }
    
    var ipg: String {
        return "IPG"
    }

    static var tpgs: String {
        get {
            return "TPGS"
        }
        
        set {
            
        }
    }
    
    static var tpg: String {
        return "TPG"
    }
}
