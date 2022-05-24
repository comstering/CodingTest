fun main() {
    val numbers = readLine()!!.split(" ").map { it.toInt() }.sorted()
    println("${numbers[0]} ${numbers[1]} ${numbers[2]}")
}
