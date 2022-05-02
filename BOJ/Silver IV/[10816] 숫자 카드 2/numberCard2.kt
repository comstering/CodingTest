import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine()!!
    val cards = br.readLine()!!.split(" ").map { it.toInt() }

    val cardMap = mutableMapOf<Int, Int>()
    cards.forEach {
        cardMap[it] = cardMap.getOrDefault(it, 0) + 1
    }
    val m = br.readLine()!!
    val queries = br.readLine()!!.split(" ").map { it.toInt() }

    val bw = BufferedWriter(OutputStreamWriter(System.out))

    for (i in queries) {
        bw.write("${cardMap[i]?:0} ")
    }
    bw.flush()

    br.close()
    bw.close()
}
