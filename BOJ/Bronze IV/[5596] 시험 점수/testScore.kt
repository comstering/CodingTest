fun main() {
    val min = readLine()!!.split(" ").map { it.toInt() }.sum()
    val man = readLine()!!.split(" ").map { it.toInt() }.sum()

    println(if (min >= man) min else man)
}
