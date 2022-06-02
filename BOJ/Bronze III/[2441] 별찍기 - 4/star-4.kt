fun main() {
    val num = readLine()!!.toInt()
    for (i in 0 until num) {
        println("${" ".repeat(i)}${"*".repeat(num - i)}")
    }
}
