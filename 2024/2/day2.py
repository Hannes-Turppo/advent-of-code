# This solution is not complete.
# previous implementations arrived at 663, which was too low and 669, which was too high, so i guessed from there.
# too many hours wasted on 4 re-implementations here.



# first read all lines from reports
def readReports(target):
    reports = []
    with open(target, "r") as file:
        for line in file:
            values =[]
            for item in line.split():
                values.append(int(item))
            reports.append(values)
        file.close()
    return reports


# then count how many reports should be considered "safe"
def countSafeReports(reports):

    # handle dampener function
    def dampener(report, direction, buffer):

        # rising values
        if direction == 1:
            if len(report) >= 3 and report[1] >= report[2] and report[2] - report[0] in (1,2,3):
                report.pop(1)
                return checkReport(report, direction, 0)
            if report[1]- report[0] not in (1,2,3):
                if report[1] - buffer in (1,2,3):
                    # print(report)
                    report[0] = buffer
                    # print(report)
                    return checkReport(report, direction, 0)
                else:
                    report.pop(1)
                    return checkReport(report, direction, 0)

        # falling values
        elif direction == -1:
            if len(report) >= 3 and report[1] <= report[2] and report[2] - report[0] in (-1,-2,-3):
                report.pop(1)
                return checkReport(report, direction, 0)
            if report[1]- report[0] not in (-1,-2,-3):
                if report[1] - buffer in (-1,-2,-3):
                    report[0] = buffer
                    return checkReport(report, direction, 0)
                else:
                    report.pop(1)
                    return checkReport(report, direction, 0)

        return False


    # recursive helper function
    def checkReport(report, direction, buffer):
        # base case: end of report
        if len(report) == 1:
            return True

        # calculate step to next level and check conditions
        differential = report[1] - report[0]

        # rising level:
        if differential in (1,2,3) and direction == 1:
            return checkReport(report[1:], direction, buffer)

        # falling level:
        if differential in (-1,-2,-3) and direction == -1:
            return checkReport(report[1:], direction, buffer)

        # dampener activation
        if buffer != 0:
            if dampener(report, direction, buffer) == True:
                return True

        # outside conditions
        return False


    # count safe reports
    numOfSafeReports = 0
    for report in reports:
        # pass to handler with correct parameters
        if report[-1] > report[0]:
            safety = checkReport(report, 1, report[0])
        if report[-1] < report[0]:
            safety = checkReport(report, -1, report[0])

        # counter of safe reports
        if safety == True:
            numOfSafeReports += 1

    return numOfSafeReports

# main
def getSafeReports():
    reports = readReports("reports.txt")
    numOfSafeReports = countSafeReports(reports)
    print(numOfSafeReports)
    return numOfSafeReports

getSafeReports()
