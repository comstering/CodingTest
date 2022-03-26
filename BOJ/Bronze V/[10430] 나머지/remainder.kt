fun main() {
    val input = readLine()!!.split(" ").map { it.toInt() }
    println((input[0] + input[1]) % input[2])
    println(((input[0] % input[2]) + (input[1] % input[2])) % input[2])
    println((input[0] * input[1]) % input[2])
    println(((input[0] % input[2]) * (input[1] % input[2])) % input[2])
}