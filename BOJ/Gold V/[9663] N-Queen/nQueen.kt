import kotlin.math.*

fun main() {
    var nQueen = NQueen(readLine()!!.toInt())
    println(nQueen.solve(0))
}

class NQueen (var n: Int) {
    private var board: ArrayList<Int>

    // 생성자로 n과 board 초기화
    init {
        this.board = ArrayList<Int>()
        for(i in 0 until n) {
            this.board.add(0)
        }
    }

    fun solve(idx: Int): Int {
        // 끝지점에 도달 했을 경우 1 반환
        if(idx == this.n) {
            return 1
        }

        var result: Int = 0
        for(i in 0 until this.n) {
            // 현재 행의 idx 입력
            this.board[idx] = i
            if(isValid(idx, i)) {
                // 현재 행의 idx 이후로 퀸을 위치할 수 있는 경우의 수 다 더하기
                result += solve(idx + 1)
            }
        }

        return result
    }

    // 현재 행의 idx가 퀸이 위치할 수 있는지 확인
    fun isValid(idx: Int, value: Int): Boolean {
        for(i in 0 until idx) {
            // 상하좌우, 대각선 위치에 다른 퀸이 있는지 검사 있다면 false 반환
            if(this.board[i] == value || abs(this.board[i] - value) == (idx - i)) {
                return false
            }
        }
        // 다른 퀸이 없다면 놓을 수 있는 자리이므로 true 반환
        return true
    }
}
