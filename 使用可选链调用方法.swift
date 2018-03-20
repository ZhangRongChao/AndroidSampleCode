
/*
 可以通过可选链调用方法。
 */
class Person {
    var residence: Residence?
}

class Residence {
    var address: Address?
}

class Address {
    var street: String = "ShengliRoad"
    
    func getStreet() -> String {
        return street
    }
}

let person = Person()
let residence = Residence()
let address = Address()

person.residence = residence
// residence.address = address

person.residence?.address?.getStreet()


/*
 当可选链访问和调用成功时，如果最后一次访问或调用的返回值不是可选类型，Swift会将该返回值包装成可选类型以作为可选链的最终返回值类型。
 */
let street = person.residence?.address?.getStreet()

if var isEndsWithRoad = street?.hasSuffix("Road") {
    if isEndsWithRoad {
        print("街道名称以\"Road\"结尾")
    }
    else {
        print("街道名称不以\"Road\"结尾")
    }
}
