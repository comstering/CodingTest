class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var queue: ArrayList<Int> = priorities.toCollection(ArrayList<Int>())
        var answer = 0
        var idx = location
        while (queue.isNotEmpty()) {
            if (queue[0] == queue.maxByOrNull(){ it }) {
                answer++
                queue.removeAt(0)
                if (idx == 0) break
            } else {
                queue.add(queue.removeAt(0))
            }

            idx--
            if (idx < 0) idx = queue.size - 1
        }
        return answer
    }
}

fun main() {
    val case: Int = readLine()!!.toInt()
    for (i in 1..case) {
        val (n, m) = readLine()!!.split(" ").map { it.toInt() }
        val q = readLine()!!.split(" ").map { it.toInt() }.toIntArray()
        var solution = Solution()
        println(solution.solution(q, m))
    }
}
