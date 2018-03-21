
/*
 如果想要遍历字符串，可以通过两种方式：
 （1）把字符串中的字符作为循环变量
 */
let str = "🐵🐶🐯"

str.forEach { print($0) }

for char in str {
    print(char)
}

/*
 （2）把字符串中字符的索引作为循环变量
 */
let indices = str.indices

indices.forEach { print(str[$0]) }

for index in indices {
    print(str[index])
}

var index = str.startIndex
while index != str.endIndex {
    print(str[index])
    index = str.index(after: index)
}
