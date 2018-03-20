
/*
 可以通过可选链访问属性（获取和修改属性的值）。
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

// 通过可选链获取属性的值
person.residence?.address?.street


/*
 通过可选链修改属性的值时，整个赋值表达式的返回值类型是Void？。
 如果运算符=左边的可选链访问失败，整个赋值表达式返回nil，并且Swift不会对运算符=右边进行计算。
 */
person.residence?.address?.street = "GuangMingRoad"


func getAddress() -> String {
    print("getAddress()被调用")
    
    return "GuangMingRoad"
}

person.residence?.address?.street = getAddress()


/*
 当可选链访问和调用成功时，如果最后一次访问或调用的返回值不是可选类型，Swift会将该返回值包装成可选类型以作为可选链的最终返回值类型。
 */
let street = person.residence?.address?.street
