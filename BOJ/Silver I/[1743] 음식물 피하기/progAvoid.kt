fun main() {
    var nmk = readLine()!!.split(" ").map { it.toInt() }
    // 음식물 지도 만들기
    var progMap = ArrayList<ArrayList<Boolean>>()
    for(i in 1..nmk[0]) {
        var subArray = ArrayList<Boolean>()
        for(j in 1..nmk[1]) {
            subArray.add(false)
        }
        progMap.add(subArray)
    }
    // 음식물 지도에 음식물 정보 입력
    for(i in 1..nmk[2]) {
        var rc = readLine()!!.split(" ").map { it.toInt() }
        progMap[rc[0] - 1][rc[1] - 1] = true
    }

    // 지도의 모든 위치를 돌면서 가장 많은 음식물 개수 구하기
    var answer: Int = 0
    for(i in 0 until nmk[0]) {
        for(j in 0 until nmk[1]) {
            // j, i 위치에서 인접한 음식물 쓰레기 개수 구하기
            val prog = getProg(progMap, i, j, nmk[0], nmk[1])
            // 기존의 쓰레기 개수보다 많다면 결과 변경
            answer = if(answer > prog) answer else prog
        }
    }
    println(answer)
}

fun getProg(progMap: ArrayList<ArrayList<Boolean>>, r: Int, c: Int, n: Int, m: Int): Int {
    // 지도 밖이면 0 반환, 지도 안의 index일 때만 진행
    // result는 0 or a값
    val result = if(r < 0 || c < 0 || r >= n || c >= m) 0 else {
        var a = 0
        if(progMap[r][c]) {
            // 현재 위치 도착처리
            progMap[r][c] = false
            // 개수 +1
            ++a
            // 상하좌우 인접한 쓰레기 개수 구하기
            a += getProg(progMap, r + 1, c, n, m)
            a += getProg(progMap, r - 1, c, n, m)
            a += getProg(progMap, r, c + 1, n, m)
            a += getProg(progMap, r, c - 1, n, m)
        }
        // 구해진 a 값
        a
    }
    // 결과 반환
    return result
}
