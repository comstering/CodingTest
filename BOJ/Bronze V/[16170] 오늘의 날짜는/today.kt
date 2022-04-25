import java.time.LocalDate

fun main() {
    val now = LocalDate.now()
    println(now.year)
    println(String.format("%02d", now.monthValue))
    println(String.format("%02d", now.dayOfMonth))
}
