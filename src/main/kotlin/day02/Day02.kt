package day02

import java.io.File
import kotlin.math.abs

fun main() {
    val filePath = "./src/main/kotlin/day02/input.txt"
    val lines = File(filePath).readLines()
    var safeReports = 0
    var safeReportsWithAtMostOneIssue = 0

    for (line in lines) {
        val report: List<Int> = line.split(" ")
            .map { it.toInt() }
        if (isSafeReport(report)) {
            safeReports++
        }
        if (isSafeReportAtMostOneIssue(report)) {
            safeReportsWithAtMostOneIssue++
        }
    }

    println(safeReports)
    println(safeReportsWithAtMostOneIssue)
}

fun isSafeReport(report: List<Int>): Boolean {
    // disgusting but necessary
    val isSorted: Boolean = report == report.sorted() || report == report.sortedDescending()
    if (!isSorted) return false

    var leftNumber = report[0]
    var index = 1

    while (index < report.size) {
        val rightNumber = report[index]
        val absDifference = abs(leftNumber - rightNumber)
        if (absDifference !in 1..3) {
            return false
        }
        leftNumber = rightNumber
        index++
    }

    return true
}

fun isSafeReportAtMostOneIssue(report: List<Int>): Boolean {
    for (idx in report.indices) {
        val choppedReport = report.toMutableList()
        choppedReport.removeAt(idx)
        if (isSafeReport(choppedReport)) {
            return true
        }
    }

    return false
}
