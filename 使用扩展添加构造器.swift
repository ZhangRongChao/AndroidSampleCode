/*
 可以使用扩展为某个已有的结构体、类或枚举类型添加构造器。
 */
struct SomeStruct {
    var someProperty: String = "SomeValue"
}

extension SomeStruct {
    init(sp someProperty: String) {
        self.someProperty = someProperty
    }
}

let someStruct = SomeStruct(sp: "SV")


struct Size {
    var width = 0.0, height = 0.0
}

struct Point {
    var x = 0.0, y = 0.0
}

struct Rect {
    var originPoint = Point()
    var size = Size()
}

extension Rect {
    init(centerPoint: Point, size: Size) {
        let originPointX = centerPoint.x - (size.width / 2)
        let originPointY = centerPoint.y - (size.height / 2)
        self.init(originPoint: Point(x: originPointX, y: originPointY), size: size)
    }
}

let centerRect = Rect(centerPoint: Point(x: 4.0, y: 4.0), size: Size(width: 3.0, height: 3.0))


/*
 只可以使用扩展为某个已有的类类型添加便利构造器，不可以添加指定构造器或析构器。
 */
class SomeClass {
    var someProperty = "SomeValue"
}

extension SomeClass {
    convenience init(someProperty: String) {
        self.init()
        self.someProperty = someProperty
    }
    
    /*
    init(someProperty: String) {
        self.someProperty = someProperty
    }
     */
    
    /*
    deinit {
        print("析构器被调用")
    }
     */
}


/*
 当使用扩展为某个已有的结构体类型添加构造器时，
 （1）如果该结构体类型的原始实现中未提供任何自定义构造器，可以在被添加的构造器里调用默认的逐一成员构造器。
 （2）如果该结构体类型的原始实现中未提供任何自定义构造器，并且该结构体类型的所有实例存储属性都有默认值，还可以在被添加的构造器里调用默认的无参构造器。
 */
struct SomeStruct1 {
    // var someProperty1: String
    // var someProperty2: String
    
    var someProperty1: String = "SomeValue1"
    var someProperty2: String = "SomeValue2"
}

extension SomeStruct1 {
    init(sp1 someProperty1: String, sp2 someProperty2: String) {
        // self.init(someProperty1: "SomeValue1", someProperty2: "SomeValue2")
        
        self.init()
    }
}
