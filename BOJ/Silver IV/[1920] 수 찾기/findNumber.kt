fun main() {
    readLine()!!
    val a = readLine()!!.split(" ").map { it.toInt() }.toSet()
    readLine()!!
    val mArr = readLine()!!.split(" ").map { it.toInt() }

    for (num in mArr) {
        if (a.contains(num)) {
            println(1)
        } else {
            println(0)
        }
    }
}
