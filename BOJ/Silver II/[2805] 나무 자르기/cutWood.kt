fun main() {
    val (_, m) = readLine()!!.split(" ").map { it.toLong() }
    var woods = readLine()!!.split(" ").map { it.toLong() }

    var start: Long = 0
    var end: Long = woods.maxOrNull()?:0
    var result: Long = 0
    
    while (start < end) {
        result = (start + end) / 2
        var sum: Long = 0
        woods.forEach {
            val length = it - result
            sum += if (length >= 0) length else 0
        }
        if (sum < m) {
            end = result
        } else if (sum > m) {
            if (start == result) {
                break
            }
            start = result
        } else {
            break
        }
    }

    println(result)
}
