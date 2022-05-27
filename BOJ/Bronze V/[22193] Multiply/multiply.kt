import java.math.BigInteger

fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val a = readLine()!!.toBigInteger()
    val b = readLine()!!.toBigInteger()
    println(a.multiply(b))
}
