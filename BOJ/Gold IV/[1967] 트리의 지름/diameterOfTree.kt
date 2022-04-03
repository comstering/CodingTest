class Tree(var n: Int) {
    private var graph: ArrayList<ArrayList<ArrayList<Int>>> = ArrayList<ArrayList<ArrayList<Int>>>()
    private var visited: ArrayList<Boolean> = ArrayList<Boolean>()
    private var leafNode: ArrayList<Int> = ArrayList<Int>()

    init {
        for(i in 0..this.n) {
            this.graph.add(ArrayList<ArrayList<Int>>())
            this.visited.add(false)
        }
        makeTree()
    }

    //  트리 만들기
    private fun makeTree() {
        for(i in 1 until this.n) {
            var nodeWeight = readLine()!!.split(" ").map{ it.toInt() }
            // 부모노드에 (자식노드, 가중치) 저장
            var edge = arrayListOf(nodeWeight[1], nodeWeight[2])
            this.graph[nodeWeight[0]].add(edge)
            // 자식노드에 (부모노드, 가중치) 저장
            edge = arrayListOf(nodeWeight[0], nodeWeight[2])
            this.graph[nodeWeight[1]].add(edge)
        }
        
        // leafNode 만들기
        for(i in 1..this.n) {
            if(this.graph[i].size == 1) {
                this.leafNode.add(i)
            }
        }
    }

    // 노드의 가장 먼 노드까지의 길이 구하기
    private fun lineLength(node: ArrayList<Int>): Int {
        // 현재 노드 방문 처리
        this.visited[node[0]] = true
        var length = 0
        // 깊이 우선 탐색
        for (i in this.graph[node[0]]) {
            if(!this.visited[i[0]]) {
                var tmp = i[1] + lineLength(i)
                // 현재 구해진 길이보다 길다면 tmp 값으로 변경
                length = if(length < tmp) tmp else length
            }
        }
        return length
    }

    // 결과 구하기
    fun getAnswer() {
        var answer = 0
        for(idx in this.leafNode) {
            // 방문 처리 리스트
            for(i in 0..this.n) {
                this.visited[i] = false
            }
            // 시작노드 방문 처리
            this.visited[idx] = true

            // 시작노드에 연결된 노드 방향으로 길이 구하기
            var length = graph[idx][0][1] + lineLength(graph[idx][0])
            // 이전 길이보다 길경우 answer 값 변경
            answer = if(answer < length) length else answer
        }
        println(answer)
    }

}

fun main() {
    var n: Int = readLine()!!.toInt()
    var tree = Tree(n)
    tree.getAnswer()
}
