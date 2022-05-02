fun main() {
    val n: Int = readLine()!!.toInt()
    val baseArray: ArrayList<Int> = ArrayList<Int>()
    for (i in 1..n) {
        baseArray.add(i)
    }
    val resultArray: ArrayList<Int> = ArrayList<Int>()
    val printList: ArrayList<Char> = ArrayList<Char>()
    for (i in 1..n) {
        val num: Int = readLine()!!.toInt()
        if (baseArray.contains(num)) {
            while (baseArray[0] != num) {
                resultArray.add(baseArray.removeAt(0))
                printList.add('+')
            }
            baseArray.removeAt(0)
            printList.add('+')
            printList.add('-')
        }
        else {
            if (resultArray.last() == num) {
                resultArray.removeAt(resultArray.size - 1)
                printList.add('-')
            }
            else {
                printList.add('?')
            }
        }
    }

    if (printList.contains('?')) {
        println("NO")
    }
    else {
        printList.forEach {
            println(it)
        }
    }
}
