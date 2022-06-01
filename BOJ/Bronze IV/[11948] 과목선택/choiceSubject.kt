fun main() {
    val science = ArrayList<Int>()
    for (i in 1..4) {
        science.add(readLine()!!.toInt())
    }
    science.sort()
    science.reverse()

    val social = ArrayList<Int>()
    for (i in 1..2) {
        social.add(readLine()!!.toInt())
    }
    social.sort()
    social.reverse()

    println(science.subList(0, 3).sum() + social[0])
}
