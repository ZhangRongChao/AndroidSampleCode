
/*
 如果想要增加字符串中的字符，可以调用以下方法：
 （1）append(_ c: Character)
    该方法用于在字符串的末尾追加参数c指定的字符。
 */
var str = "🐵🐶"
str.append(Character("🐯"))

/*
 （2）append(_ other: String)
    该方法用于在字符串的末尾追加参数other指定的字符串。
 */
str.append("🐂🐑")

/*
 （3）insert(_ newElement: Character, at i: String.Index)
    该方法用于在字符串中参数at指定的位置插入参数newElement指定的字符。
 */
str.insert(Character("🐔"), at: str.index(after: str.startIndex))

/*
 （4）insert<S : Collection where S.Iterator.Element == Character>(contentsOf newElements: S, at i: String.Index)
    该方法用于在字符串中参数at指定的位置插入参数newElements指定的Collection类型。
 */
str.insert(contentsOf: "🐻🐴🐰", at: str.startIndex)


/*
 如果想要增加字符串中的字符，还可以使用运算符+=，该运算符可用于在字符串的末尾追加另一个字符串。
 此外，运算符+可用于连接两个字符串，并且连接后两个字符串都保持不变。
 */
var str1 = "🐵🐶🐯"
str1 += "🐂🐑🐔"

var str2 = "🐻🐴🐰"
str1 + str2
str1
str2
