import kotlin.math.pow

fun main() {
    var numStr: String = readLine()!!
    var num: Int = numStr.toInt()
    var idx: Int = 1
    while(idx < numStr.length) {
        var p: Int = 10.0.pow(idx++).toInt()
        var temp: Int = (num % p) / (p / 10)
        num = num / p * p + when(temp >= 5) {
            true -> p
            false -> 0
        }
        numStr = num.toString()
    }
    println(num)
}
