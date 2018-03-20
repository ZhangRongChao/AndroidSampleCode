/*
 可以使用扩展为某个已有的结构体、类或枚举类型添加类型存储属性和计算属性，但是不可以添加实例存储属性。
 */
struct SomeStruct {
    
}

let someStruct = SomeStruct()

extension SomeStruct {
    // var instanceStoredProperty: String = "ISP"
    
    static var typeStoredProperty: String = "TSP"
    
    var instanceComputedProperty: String {
        get {
            return "ICP"
        }
        
        set {
            print(newValue)
        }
    }
    
    static var typeComputedProperty: String {
        get {
            return "TCP"
        }
        
        set {
            print(newValue)
        }
    }
}

someStruct.instanceComputedProperty
SomeStruct.typeComputedProperty
SomeStruct.typeStoredProperty


extension Double {
    var km: Double {
        return self * 1_000.0
    }
    
    var m: Double {
        return self
    }
    
    var cm: Double {
        return self / 100.0
    }
    
    static var pi: Double {
        return 3.1415926
    }
}

let x: Double = 16.8

x.km
x.m
x.cm

Double.pi
