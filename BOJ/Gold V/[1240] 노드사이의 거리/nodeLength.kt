class Graph(var n: Int) {
    var graph: MutableMap<Int, Node>
    var visited: ArrayList<Boolean>

    init {
        graph = mutableMapOf()
        for (i in 1..n) {
            graph[i] = Node()
        }
        visited = ArrayList<Boolean>()
        for (i in 0..n) {
            visited.add(false)
        }
    }

    fun clearVisited(start: Int) {
        for (i in 0..n) {
            visited[i] = false
        }
        visited[start] = true
    }

    fun getLength(start: Int, end: Int): Int {
        if(start == end) return 0
        val startNode = graph[start]

        var length = 0
        for((nextV, nextW) in startNode!!.edge) {
            if(!visited[nextV]) {
                visited[nextV] = true
                var tmp = getLength(nextV, end)
                if(tmp != -1) {
                    length = tmp + nextW
                }
                visited[nextV] = false
            }
        }
        if(length == 0) {
            return -1
        }
        return length
    }
}

class Node() {
    var edge: MutableMap<Int, Int> = mutableMapOf()

    fun addEdge(v: Int, w: Int) {
        edge[v] = w
    }
}

fun main() {
    var nm = readLine()!!.split(" ").map { it.toInt() }
    var g = Graph(nm[0])
    for(i in 1 until nm[0]) {
        var input = readLine()!!.split(" ").map { it.toInt() }
        g.graph[input[0]]!!.addEdge(input[1], input[2])
        g.graph[input[1]]!!.addEdge(input[0], input[2])
    }
    for(i in 1..nm[1]) {
        var nodes = readLine()!!.split(" ").map { it.toInt() }
        g.clearVisited(nodes[0])
        println(g.getLength(nodes[0], nodes[1]))
    }
}
