fun main() {
    val n = readLine()!!.toInt()
    val numList = readLine()!!.split(" ").map { it.toInt() }
    val v = readLine()!!.toInt()
    println(numList.count { it == v })
}
