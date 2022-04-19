fun main() {
    var abn = readLine()!!.split(" ").map { it.toInt() }
    var tmp = abn[0] % abn[1]
    var decimal: Int = 0
    for (i in 1..abn[2]) {
        decimal = tmp * 10 / abn[1]
        tmp = tmp * 10 % abn[1]
    }
    println(decimal)
}
