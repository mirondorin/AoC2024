package day03

import java.io.File

fun main() {
    val filePath = "./src/main/kotlin/day03/input.txt"
    val lines = File(filePath).readLines()
    val pattern = Regex("mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)")

    for (line in lines) {
        val matches: Sequence<MatchResult> = pattern.findAll(line)

        println(solve(matches, true))
        println(solve(matches, false))
    }
}

fun solve(
    matches: Sequence<MatchResult>,
    ignoreEnabled: Boolean
): Int {
    var enabled = true
    var sum = 0
    for (match in matches) {
        if (match.value == "do()") {
            enabled = true
        } else if (match.value == "don't()") {
            enabled = false
        } else {
            val groups = match.groupValues
            val numbers = Pair(groups[1].toInt(), groups[2].toInt())
            if (enabled || ignoreEnabled) {
                sum += numbers.first * numbers.second
            }
        }
    }
    return sum
}