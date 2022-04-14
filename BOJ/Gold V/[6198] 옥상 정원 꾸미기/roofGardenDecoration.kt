fun main() {
    var n: Long = readLine()!!.toLong()

    val buildings: ArrayList<Long> = ArrayList<Long>()

    for(i in 0 until n) {
        buildings.add(readLine()!!.toLong())
    }

    val nextBuildings: ArrayList<Array<Long>> = ArrayList<Array<Long>>()
    var count: Long = 0

    for(i in 1 until n) {
        nextBuildings.add(arrayOf(buildings.removeAt(buildings.size - 1), i))
        while(!nextBuildings.isEmpty() && nextBuildings.last()[0] < buildings.last()) {
            nextBuildings.removeAt(nextBuildings.size - 1)
        }
        if(nextBuildings.isEmpty()) {
            count += i
        }
        else {
            count += i - nextBuildings.last()[1]
        }
    }

    println(count)
}
