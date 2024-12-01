package day01

import java.io.File
import java.util.Collections
import java.util.regex.Pattern
import kotlin.math.abs

val left = ArrayList<Int>()
val right = ArrayList<Int>()

fun main(args: Array<String>) {
    val filePath = "./src/main/kotlin/day01/input.txt"
    val lines = File(filePath).readLines()

    for (line in lines) {
        val split = line.split(Pattern.compile(" +"))
        left.add(split[0].toInt())
        right.add(split[1].toInt())
    }

    firstPart()
    secondPart()
}

fun secondPart(): Int {
    var sum = 0
    val freqMap = mutableMapOf<Int, Int>()

    for (value in left.distinct()) {
        freqMap[value] = Collections.frequency(right, value)
        sum += value * freqMap[value]!!
    }

    return sum
}

fun firstPart(): Int {
    var sum = 0

    left.sort()
    right.sort()
    for (idx in 0..<left.size) {
        sum += abs(left[idx] - right[idx])
    }

    return sum
}

