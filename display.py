import pygal

dates = ["2016-07-13 12:45:12", "2016-07-14 09:14:36"]
data = [[12,9,2],[4,3,7],[2,5,8]]

def displayGraph():

    rolls = []
    for i in range(len(data)):
        rolls.append(data[i][0])

    pitches = []
    for i in range(len(data)):
        pitches.append(data[i][1])

    yaws = []
    for i in range(len(data)):
        yaws.append(data[i][2])

    line_chart = pygal.Line()


    line_chart.add("Roll", rolls)
    line_chart.add("Pitch", pitches)
    line_chart.add("Yaw", yaws)

    line_chart.render_to_file("line_chart.svg")
