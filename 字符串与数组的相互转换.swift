
/*
 字符串与数组之间可以相互转换：
 （1）把字符串作为Array的构造器的参数，可以把字符串转换为数组。
 */
let str = "acgbedf"
let array = Array(str)

/*
 （2）把数组作为String的构造器的参数，可以把数组转换为字符串。
 */
String(["a", "c", "g", "b", "e", "d", "f"])


/*
 当把字符串转换为数组后，就可以利用数组的各种特性了。
 */
for (index, char) in array.enumerated() {
    print("第\(index)个字符是：\(char)")
}

// 对数组中的所有字符进行排序后再转换为字符串
String(array.sorted())
