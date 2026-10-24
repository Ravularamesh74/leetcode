/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    const daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Helper function to convert "MM-DD" into day of the year (1 to 365)
    const getDayOfYear = (dateStr) => {
        const [month, day] = dateStr.split('-').map(Number);
        let totalDays = day;
        for (let i = 0; i < month - 1; i++) {
            totalDays += daysInMonths[i];
        }
        return totalDays;
    };

    const aliceArrival = getDayOfYear(arriveAlice);
    const aliceLeave = getDayOfYear(leaveAlice);
    const bobArrival = getDayOfYear(arriveBob);
    const bobLeave = getDayOfYear(leaveBob);

    // Find the latest arrival and earliest leave
    const startOverlap = Math.max(aliceArrival, bobArrival);
    const endOverlap = Math.min(aliceLeave, bobLeave);

    // Calculate overlapping days
    return Math.max(0, endOverlap - startOverlap + 1);
};