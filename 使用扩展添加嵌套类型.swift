/*
 可以使用扩展为某个已有的结构体、类或枚举类型添加嵌套类型。
 */
extension Int {
    enum Kind {
        case Negative, Zero, Positive
    }
    
    var kind: Kind {
        switch self {
        case 0:
            return .Zero
        case let x where x > 0:
            return .Positive
        default:
            return .Negative
        }
    }
}

func printIntegerKinds(numbers: [Int]) {
    for number in numbers {
        switch number.kind {
        case .Negative:
            print("-")
        case .Zero:
            print("0")
        case .Positive:
            print("+")
        }
    }
}

printIntegerKinds(numbers: [3, 19, -27, 0, -6, 0, 7])
