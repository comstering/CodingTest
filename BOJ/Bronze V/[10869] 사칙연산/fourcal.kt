fun main() {
    var input = readLine()!!.split(" ").map { it.toInt() }
    println(input[0] + input[1])
    println(input[0] - input[1])
    println(input[0] * input[1])
    println(input[0] / input[1])
    println(input[0] % input[1])
}
