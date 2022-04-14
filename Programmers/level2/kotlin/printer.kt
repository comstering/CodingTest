class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var queue: ArrayList<Int> = priorities.toCollection(ArrayList<Int>())
        var answer = 0
        var idx = location
        while(queue.isNotEmpty()) {
            if(queue[0] == queue.maxByOrNull(){ it }) {
                answer++
                queue.removeAt(0)
                if(idx == 0) break
            } else {
                queue.add(queue.removeAt(0))
            }

            idx--
            if(idx < 0) idx = queue.size - 1
        }
        return answer
    }
}

fun main() {
    var solution = Solution()
    println(solution.solution(intArrayOf(2, 1, 3, 2), 2))  // 1
    println(solution.solution(intArrayOf(1, 1, 9, 1, 1, 1), 0))  // 5
}