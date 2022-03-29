fun main() {
    var l: Int = readLine()!!.toInt()
    var n: Int = readLine()!!.toInt()
    
    var cake: ArrayList<Boolean> = arrayListOf<Boolean>()

    for (i: Int in 1..l) {
        cake.add(true)
    }

    var guessPiece: Int = 0
    var realPiece: Int = 0
    var guess: Int = 0
    var real: Int = 0
    for (i: Int in 1..n) {
        var piece = readLine()!!.split(" ").map{ it.toInt() }
        if (guessPiece < piece[1] - piece[0]) {
            guessPiece = piece[1] - piece[0]
            guess = i
        }
        var count = 0
        for (p: Int in piece[0]..piece[1]) {
            if (cake[p - 1]) {
                cake[p - 1] = false
                count += 1
            }
        }
        if (count > realPiece) {
            realPiece = count
            real = i
        }
    }

    println(guess)
    println(real)
}
