fun main() {
    val (k, n, m) = readLine()!!.split(" ").map { it.toInt() }
    println(if (k * n <= m) 0 else k * n - m)
}
