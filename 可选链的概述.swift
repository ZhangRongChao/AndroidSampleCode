
/*
 所谓可选链，就是多次连续访问和调用属性、方法或下标的过程，并且所有的访问者和调用者都是可选类型，这样，所有的访问和调用就可以被链接在一起形成一个可选链。
 
 可选链适用于结构体、类和枚举。
 
 如果可选链上所有的访问者和调用者都不为nil，可选链访问和调用成功；如果可选链上存在某个访问者或调用者为nil，可选链访问和调用失败。
 */
class Person {
    var residence: Residence?
}

class Residence {
    var address: Address?
}

class Address {
    var street: String = "ShengliRoad"
}

let person = Person()
let residence = Residence()
let address = Address()

person.residence = residence
// residence.address = address

// person.residence!.address!.street


/*
 为了防止可选链访问或调用失败导致的运行时错误，可以使用问号代替叹号。这样，当可选链访问或调用成功时，则强制解包；当可选链访问或调用失败时，并不会导致运行时错误，而是将整个可选链返回nil。
 */
person.residence?.address?.street
