fun main() {
    var board: String = readLine().toString()
    board = board.replace("XX", "BB").replace("BBBB", "AAAA")
    if (board.contains("X")) {
        println(-1)
    } else {
        println(board)
    }
}
