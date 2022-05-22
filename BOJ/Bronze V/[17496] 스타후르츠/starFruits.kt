fun main() {
    val fruits = readLine()!!.split(" ").map { it.toInt() }
    println(((fruits[0] - 1) / fruits[1]) * fruits[2] * fruits[3])
}
