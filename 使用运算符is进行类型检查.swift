
/*
 运算符is可以用于检查变量或常量的运行时类型是否是指定的子类类型，其语法格式为：变量或常量 is 指定的子类类型。
 */
class SuperClass {
    
}

class SubClass: SuperClass {
    
}

let object: SuperClass = SubClass()
object is SubClass


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

var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}

print("媒体库包含\(movieCount)部电影和\(songCount)首歌")
