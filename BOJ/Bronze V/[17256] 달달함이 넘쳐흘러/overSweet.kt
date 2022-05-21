fun main() {
    val a = readLine()!!.split(" ").map{ it.toInt() }
    val c = readLine()!!.split(" ").map{ it.toInt() }
    println("${c[0] - a[2]} ${c[1] / a[1]} ${c[2] - a[0]}")
}
