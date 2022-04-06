import kotlin.math.abs

fun main() {
    // n, m 입력
    var nm = readLine()!!.split(" ").map { it.toInt() }
    // 책 위치 입력
    var bookList = readLine()!!.split(" ").map { it.toInt() }.sorted()
    // 책을 가져다 놓은 거리 리스트
    var lengthList = ArrayList<Int>()
    // +, - 변하는 인덱스 찾기
    var idx = 0
    for(i in bookList) {
        if(i > 0) { break }
        idx++
    }
    // 음수 거리 책 리스트
    var negativeList = bookList.subList(0, idx).toMutableList()
    // 양수 거리 책 리스트
    var positiveList = bookList.subList(idx, bookList.size).reversed().toMutableList()
    // 한 번에 가져갈 수 있는 책의 배수 만큼만 반복
    var loopCount = negativeList.size - (negativeList.size % nm[1])
    for(i in 0 until loopCount) {
        if(i % nm[1] == 0) {
            lengthList.add(abs(negativeList[0]))
        }
        negativeList.removeFirst()
    }
    // 만약 한 번에 가져갈 수 있는 책보다 적은 양의 책이 남는 다면 남은 책 중 가장 큰 값 거리 리스트에 추가
    if(!negativeList.isEmpty()) {
        lengthList.add(abs(negativeList[0]))
    }
    // 한 번에 가져갈 수 있는 책의 배수 만큼만 반복
    loopCount = positiveList.size - (positiveList.size % nm[1])
    for(i in 0 until loopCount) {
        if(i % nm[1] == 0) {
            lengthList.add(abs(positiveList[0]))
        }
        positiveList.removeFirst()
    }
    // 만약 한 번에 가져갈 수 있는 책보다 적은 양의 책이 남는 다면 남은 책 중 가장 큰 값 거리 리스트에 추가
    if(!positiveList.isEmpty()) {
        lengthList.add(abs(positiveList[0]))
    }
    // 가장 먼 거리의 책은 한 번만 이동
    var result: Int = lengthList.maxOrNull()!!
    lengthList.remove(result)
    // 가장 먼 거리를 제외한 다른 책들의 합X2
    result += lengthList.sum() * 2
    println(result)
}
