import java.util.Queue
import java.util.LinkedList

fun main() {
    // 노드의 개수
    val node: Int = readLine()!!.toInt()
    // 연결 간선 개수
    val edges: Int = readLine()!!.toInt()

    // 노드의 연결 그래프
    val graph: ArrayList<ArrayList<Int>> = ArrayList<ArrayList<Int>>()
    // 노드의 탐색 여부 리스트
    val visited: ArrayList<Boolean> = ArrayList<Boolean>()

    // 그래프, 탐색 여부 리스트 초기화
    for (i in 0..node) {
        graph.add(ArrayList<Int>())
        visited.add(false)
    }

    // 간선을 입력받아 그래프에 기록
    for (i in 1..edges) {
        val (n1, n2) = readLine()!!.split(" ").map { it.toInt() }
        graph[n1].add(n2)
        graph[n2].add(n1)
    }

    val queue: Queue<Int> = LinkedList<Int>()
    // 큐에 시작 노드인 1 추가
    queue.add(1)
    // 1 노드 탐색 완료 표시
    visited[1] = true

    // 큐가 빌 때까지 반복
    while (queue.isNotEmpty()) {
        val n = queue.poll()
        // 현재 노드와 연결된 다른 노드들을 탐색
        for (i in graph[n]) {
            if (!visited[i]) {
                queue.add(i)
                visited[i] = true
            }
        }
    }

    // 1을 제외한 노드 중 탐색 완료된 노드의 개수 출력
    println(visited.count { it } - 1)
}
