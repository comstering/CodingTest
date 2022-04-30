fun main() {
    val n: Int = readLine()!!.toInt()
    val q: ArrayList<Int> = ArrayList<Int>()
    for (i in 1..n) {
        val commands = readLine()!!.split(" ")
        when (commands[0]) {
            "push" -> q.add(commands[1].toInt())
            "pop" -> if (q.isEmpty()) println(-1) else println(q.removeAt(0))
            "size" -> println(q.size)
            "empty" -> println(if (q.isEmpty()) 1 else 0)
            "front" -> if (q.isEmpty()) println(-1) else println(q[0])
            "back" -> if (q.isEmpty()) println(-1) else println(q[q.size - 1])
        }
    }
}
