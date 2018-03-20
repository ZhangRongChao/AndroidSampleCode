
/*
 可以使用运算符as将变量或常量的编译时类型向下转换为指定的子类类型，其语法格式为：变量或常量 as? 指定的子类类型，或者：变量或常量 as! 指定的子类类型。
 （1）当不确定向下转型是否会成功时，使用运算符as?。如果向下转型成功，返回指定类型的可选值；如果向下转型失败，返回nil。
 （2）当确定向下转型一定会成功时，使用运算符as!。如果向下转型成功，返回指定类型的隐式解包的可选值；如果向下转型失败，会导致运行时错误。
 
 使用运算符as向下转型不会对对象本身做任何改变。
 */
class SuperClass {
    
}

class SubClass1: SuperClass {
    
}

class SubClass2: SuperClass {
    
}

let object: SuperClass = SubClass1()

let a = object as? SubClass1
object as? SubClass2

let b = object as! SubClass1
// object as! SubClass2


class MediaItem {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

class Movie: MediaItem {
    var director: String
    
    init(name: String, director: String) {
        self.director = director
        super.init(name: name)
    }
}

class Song: MediaItem {
    var artist: String
    
    init(name: String, artist: String) {
        self.artist = artist
        super.init(name: name)
    }
}

var library: [MediaItem] = [
    Movie(name: "movie1", director: "director1"),
    Song(name: "song1", artist: "artist1"),
    Movie(name: "movie2", director: "director2"),
    Song(name: "song2", artist: "artist2"),
    Song(name: "song3", artist: "artist3")
]

for item in library {
    if let movie = item as? Movie {
        print("Movie: \(movie.name), \(movie.director)")
    } else if let song = item as? Song {
        print("Song: \(song.name), \(song.artist)")
    }
}

for item in library {
    switch item {
    case let movie as Movie:
        print("Movie: \(movie.name), \(movie.director)")
    case let song as Song:
        print("Song: \(song.name), \(song.artist)")
    default:
        break
    }
}
