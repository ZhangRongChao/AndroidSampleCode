/*
 可以使用扩展为某个已有的结构体、类或枚举类型添加下标。
 */
class SomeClass {
    
}

extension SomeClass {
    subscript(index: Int) -> String {
        get {
            return "第\(index)个元素的值"
        }
        
        set {
            print("第\(index)个元素的新值是：\(newValue)")
        }
    }
}

var someClass = SomeClass()

someClass[3]
someClass[5] = "18"
