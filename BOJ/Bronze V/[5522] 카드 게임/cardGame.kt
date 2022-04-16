fun main() {
    var score: Int = 0
    for (i in 1..5) {
        score += readLine()!!.toInt()
    }
    println(score)
}
