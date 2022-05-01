fun main() {
    val num: Int = readLine()!!.toInt()
    println("${num - (num * 22 / 100)} ${num - ((num * 20 / 100) * 22 / 100)}")
}
