import time
import sys
from Report import Report


if __name__ == '__main__':
    rpt = Report()

    if len(sys.argv) < 2:
        print("Usage: src/main.py DATA_DIRECTORY")
    else:

        print("Reading the databases...", file=sys.stderr)
        before = time.time()

        areaTitlesDict = {}
        areaTitlesObj = open(str(sys.argv[1] + "/area_titles.csv"))
        areaTitlesObj.readline()
        for line in areaTitlesObj:
            line = line.strip()
            fips, title = line.split(",")
            if fips.isnumeric() and not fips.endswith("000"):
                areaTitlesDict[fips] = title

        dataObj = open(str(sys.argv[1] + "2019.annual.singlefile.csv"))

        allNumAreas = 0
        allTotWages = 0
        allMaxWage = 0
        allMaxWageArea = ""
        allTotEstab = 0
        allMaxEstab = 0
        allMaxEstabArea = ""
        allTotEmp = 0
        allMaxEmp = 0
        allMaxEmpArea = ""

        softNumAreas = 0
        softTotWages = 0
        softMaxWage = 0
        softMaxWageArea = ""
        softTotEstab = 0
        softMaxEstab = 0
        softMaxEstabArea = ""
        softTotEmp = 0
        softMaxEmp = 0
        softMaxEmpArea = ""

        print("TODO: Collect information from 'sys.argv[1]/2019.annual.singlefile.csv', place into the Report object rpt")  # DELETE ME

        for line in dataObj:
            lineList = line.split(",", maxsplit=11)
            lineList.remove(lineList[12])
            if lineList[0] in areaTitlesDict:

                # For all industries
                if lineList[1] == "0" and lineList[2] == "10":
                    allNumAreas += 1
                    allTotEstab += int(lineList[9])
                    allTotEmp += int(lineList[10])
                    allTotWages += int(lineList[11])

                    # Update max values for all industry
                    if int(lineList[9]) > allMaxEstab:
                        allMaxEstab = int(lineList[9])
                        allMaxEstabArea = areaTitlesDict[lineList[0]]
                    if int(lineList[10]) > allMaxEmp:
                        allMaxEmp = int(lineList[10])
                        allMaxEmpArea = areaTitlesDict[lineList[0]]
                    if int(lineList[11]) > allMaxWage:
                        allMaxWage = int(lineList[11])
                        allMaxWageArea = areaTitlesDict[lineList[0]]

                # For software industry only
                if lineList[1] == "5" and lineList[2] == "5112":
                    softNumAreas += 1
                    softTotEstab += int(lineList[9])
                    softTotEmp += int(lineList[10])
                    softTotWages += int(lineList[11])

                    # Update max values for software industry
                    if int(lineList[9]) > allMaxEstab:
                        softMaxEstab = int(lineList[9])
                        softMaxEstabArea = areaTitlesDict[lineList[0]]
                    if int(lineList[10]) > allMaxEmp:
                        softMaxEmp = int(lineList[10])
                        softMaxEmpArea = areaTitlesDict[lineList[0]]
                    if int(lineList[11]) > allMaxWage:
                        softMaxWage = int(lineList[11])
                        softMaxWageArea = areaTitlesDict[lineList[0]]

        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

        print("TODO: Fill in the report for all industries")  # DELETE ME
        rpt.all.num_areas           = allNumAreas

        rpt.all.total_annual_wages  = allTotWages
        rpt.all.max_annual_wage     = (allMaxWageArea, allMaxWage)

        rpt.all.total_estab         = allTotEstab
        rpt.all.max_estab           = (allMaxEstabArea, allMaxEstab)

        rpt.all.total_empl          = allTotEmp
        rpt.all.max_empl            = (allMaxEmpArea, allMaxEmp)


        print("TODO: Fill in the report for the software publishing industry")  # DELETE ME
        rpt.soft.num_areas          = softNumAreas

        rpt.soft.total_annual_wages = softTotWages
        rpt.soft.max_annual_wage    = (softMaxWageArea, softMaxWage)

        rpt.soft.total_estab        = softTotEstab
        rpt.soft.max_estab          = (softMaxEstabArea, softMaxEstab)

        rpt.soft.total_empl         = softTotEmp
        rpt.soft.max_empl           = (softMaxEmpArea, softMaxEmp)


        # Print the completed report
        print(rpt)

        print("\n\nTODO: did you delete all of these TODO messages?")  # DELETE ME
