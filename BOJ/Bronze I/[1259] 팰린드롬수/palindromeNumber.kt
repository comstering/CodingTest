fun main() {
    while (true) {
        val input = readLine()!!
        if (input == "0") {
            break
        }
        if (input == input.reversed()) {
            println("yes")
        } else {
            println("no")
        }
    }
}
