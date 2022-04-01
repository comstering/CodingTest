import kotlin.math.*

fun main() {
    var nQueen = NQueen(readLine()!!.toInt())
    println(nQueen.solve(0))
}

class NQueen (var n: Int) {
    private var board: ArrayList<Int>

    init {
        this.board = ArrayList<Int>()
        for(i in 0 until n) {
            this.board.add(0)
        }
    }

    fun solve(idx: Int): Int {
        if(idx == this.n) {
            return 1
        }

        var result: Int = 0
        for(i in 0 until this.n) {
            this.board[idx] = i
            if(isValid(idx, i)) {
                result += solve(idx + 1)
            }
        }

        return result
    }

    fun isValid(idx: Int, value: Int): Boolean {
        for(i in 0 until idx) {
            if(this.board[i] == value || abs(this.board[i] - value) == (idx - i)) {
                return false
            }
        }

        return true
    }
}
