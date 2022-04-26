fun main() {
    var num = readLine()!!.toInt()
    val array: ArrayList<Int> = arrayListOf(0, 0)

    for(i in 2..num) {
        // -1을 했을 때의 count
        var count: Int = array[i - 1] + 1
        // /3을 했을 때의 count
        if(i % 3 == 0) {
            count = if(array[i / 3] + 1 < count) array[i / 3] + 1 else count
        }
        // /2를 했을 때의 count
        if(i % 2 == 0) {
            count = if(array[i / 2] + 1 < count) array[i / 2] + 1 else count
        }
        array.add(count)
    }
    println(array[num])
}
