/*
 如果想要统计字符串中的字符个数，可以访问字符串的属性count。
 访问属性count时，系统会遍历字符串的所有Unicode Scalar。
 */
"🐵🐶🐯".count

"\u{00E1}".count
"\u{0061}\u{0301}".count

"roma".count
("roma" + "\u{0301}").count
