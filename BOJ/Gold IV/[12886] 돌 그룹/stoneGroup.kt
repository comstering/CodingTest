import java.util.Queue
import java.util.LinkedList

fun main() {
    val (a, b, c) = readLine()!!.split(" ").map { it.toInt() }
    println(stone(a, b, c))
}

fun stone(a: Int, b: Int, c: Int): Int {
    // 전체합 구하기
    val total: Int = a + b + c
    // 전체 합이 3으로 나누어 떨어지지 않으면 0반환
    if (total % 3 != 0) { return 0 }

    // 돌의 순서쌍 체크리스트
    val visited: ArrayList<ArrayList<Boolean>> = ArrayList<ArrayList<Boolean>>()
    for (i in 1..total) {
        val list: ArrayList<Boolean> = ArrayList<Boolean>()
        for (j in 1..total) {
            list.add(false)
        }
        visited.add(list)
    }

    // 돌의 상태를 저장하는 큐
    val queue: Queue<List<Int>> = LinkedList<List<Int>>()
    // 입력된 돌 그룹 중 2개를 큐에 넣기
    queue.add(listOf(a, b))
    // 현재 돌 쌍 체크처리
    visited[a][b] = true

    while (queue.isNotEmpty()) {
        val (x, y) = queue.poll()
        // 현재 3 돌의 상태 확인
        val z = total - x - y
        // 3 돌의 상태가 모두 동일하면 1반환
        if (x == y && y == z) {
            return 1
        }

        // 나올 수 있는 경우의 돌 반복
        listOf(listOf(x, y), listOf(y, z), listOf(x, z)).forEach {
            var (i, j) = it
            // 문제 요구사항
            // 작은돌 X, 큰 돌 Y
            // X = X + X, Y = Y - X
            if (i < j) {
                j -= i
                i += i
            }
            else if (i > j) {
                i -= j
                j += j
            }
            // 같을 경우 패스
            else {
                return@forEach
            }

            // 새로운 3 돌 구하기
            val k = total - i - j
            // 3 돌 중 큰돌과 작은 돌 구하기
            val X = listOf(i, j, k).maxOrNull()?:0
            val Y = listOf(i, j, k).minOrNull()?:0
            // 해당 돌 쌍이 기존에 체크했던 돌 쌍이 아니면 queue에 add
            if (!visited[X][Y]) {
                queue.add(listOf(X, Y))
                // 돌 쌍 체크 처리
                visited[X][Y] = true
            }
        }
    }

    // 모든 탐색이 끝났음에도 완성이 되지 않았다면 0반환
    return 0
}
