fun main() {
    var count: Int = 1
    while(true) {
        var input = readLine().toString()
        if(input == "0") {
            break
        }

        if(checkWood(input)) {
            println("${count++}. VALID")
        } else {
            println("${count++}. NOT")
        }

    }
}

fun checkWood(input: String): Boolean {
    var wood = input.split("").slice(1..input.length).map{ it.toInt() }
    if(wood[0] != 1 || wood[wood.size - 1] != 2) {
        return false
    } else {
        val woodMap = hashMapOf(1 to arrayListOf(4, 5), 2 to arrayListOf(0),
                            3 to arrayListOf(4, 5), 4 to arrayListOf(2, 3),
                            5 to arrayListOf(8), 6 to arrayListOf(2, 3),
                            7 to arrayListOf(8), 8 to arrayListOf(6, 7))

        var check: Boolean = true
        for (i in 0..wood.size - 2) {
            check = woodMap[wood[i]]!!.contains(wood[i + 1])
            if(!check) { break }
        }
        return check
    }
}
