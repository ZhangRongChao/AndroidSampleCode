/*
 在协议的定义中可以规定其遵守者必须提供指定要求的下标。
 
 协议的下标要求的语法格式为：subscript(形参列表) -> 下标值的数据类型 { get [set] }。
 
 与协议的属性要求相似，如果要求某个下标是可读写的，在下标值的数据类型后添加{ get set }；如果要求某个下标是只读的，在下标值的数据类型后添加{ get }。
 */
protocol SomeProtocol {
    subscript(index: Int) -> String { get set }
    
    subscript(index1: Int, index2: Int) -> String { get }
}

struct SomeStruct: SomeProtocol {
    subscript(index: Int) -> String {
        get {
            return "\(index)"
        }
        
        set {
            
        }
    }
    
    subscript(index1: Int, index2: Int) -> String {
        return "\(index1), \(index2)"
    }
}
