fun main() {
    var num1 = readLine()!!.toInt()
    var num2 = readLine()!!.toInt()
    println(num1 * (num2 % 10))
    println(num1 * ((num2 % 100) / 10))
    println(num1 * (num2 / 100))
    println(num1 * num2)
}
