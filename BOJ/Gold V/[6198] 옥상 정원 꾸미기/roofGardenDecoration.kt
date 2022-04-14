fun main() {
    var n: Long = readLine()!!.toLong()

    val buildings: ArrayList<Long> = ArrayList<Long>()

    for(i in 0 until n) {
        buildings.add(readLine()!!.toLong())
    }

    // 비교할 대상의 빌딩 리스트
    val nextBuildings: ArrayList<Array<Long>> = ArrayList<Array<Long>>()
    var count: Long = 0

    for(i in 1 until n) {
        // 비교 대상 빌딩 리스트에 현재 빌딩 리스트의 마지막 빌딩 빼서 넣기
        nextBuildings.add(arrayOf(buildings.removeAt(buildings.size - 1), i))
        // 비교할 빌딩이 없을 때까지 반복
        // 비교 대상 빌딩 리스트의 마지막 빌딩과 현재 빌딩 리스트의 마지막 빌딩 비교
        while(nextBuildings.isNotEmpty() && nextBuildings.last()[0] < buildings.last()) {
            // 비교 대상 빌딩이 더 작으면 비교 대상 빌딩 리스트에서 빼기
            nextBuildings.removeAt(nextBuildings.size - 1)
        }

        count += when(nextBuildings.isEmpty()) {
            // 비교할 빌딩이 남아있지 않다면 현재의 인덱스 더하기
            true -> i
            // 비교할 빌딩이 남아있으면 현재 인덱스에서 남아있는 비교 빌딩의 리스트 인덱스 뺀 값 더하기
            false -> i - nextBuildings.last()[1]
        }
    }

    println(count)
}
