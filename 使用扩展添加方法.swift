
/*
 可以使用扩展为某个已有的结构体、类或枚举类型添加实例方法和类型方法。
 */
class SomeClass {
    
}

extension SomeClass {
    func doSomethingInstance() {
        print("doSomethingInstance()被调用")
    }
    
    static func doSomethingType() {
        print("doSomethingType()被调用")
    }
}

let someClass = SomeClass()
someClass.doSomethingInstance()

SomeClass.doSomethingType()


extension Int {
    func repeatTask(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}

5.repeatTask { print("Hello!") }


/*
 对于使用扩展为结构体类型或枚举类型添加的实例方法，如果希望在该实例方法中修改实例属性或self属性，必须在该实例方法的关键字func前面添加关键字mutating。
 */
extension Int {
    var instanceComputedProperty: String {
        get {
            return "ICP"
        }
        
        set {
            print(newValue)
        }
    }
    
    mutating func doSomething() {
        instanceComputedProperty = "NewICP"
    }
    
    mutating func changeToSquare() {
        self = self * self
    }
}
