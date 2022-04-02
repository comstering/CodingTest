fun main() {
    var input = readLine()!!.split(" ").map { it.toInt() }.sorted()
    var inputSet = input.toSet().toList()
    if(inputSet.size == 1) {
        println(10000 + input[0] * 1000)
    } else if(inputSet.size == 2) {
        println(1000 + input[1] * 100)
    } else if(inputSet.size == 3) {
        println(input[2] * 100)
    }
}
