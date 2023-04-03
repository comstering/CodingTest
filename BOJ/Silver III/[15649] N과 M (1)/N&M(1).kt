import java.util.Stack

class Solution {
    var n = 0
    var m = 0

    val stack: Stack<Int> = Stack()

    fun solution() {
        val (temp1, temp2) = readLine()!!.split(" ").map { it.toInt() }
        this.n = temp1
        this.m = temp2
        dfs()
    }

    fun dfs() {
        if(this.stack.size == this.m) {
            println(stack.joinToString(separator = " "))
            return
        }
        for (i in 1..n) {
            if (!this.stack.contains(i)) {
                this.stack.push(i)
                dfs()
                this.stack.pop()
            }
        }
    }
}

fun main() {
    Solution().solution()
}
