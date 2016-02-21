import pygal

def displayGraph(input):
    dates = input[0]
    data = input[1]
    rolls = []
    l = len(data)
    for i in range(0,l):
        rolls.append(int(data[i][0]))

    pitches = []
    for i in range(0,l):
        pitches.append(int(data[i][1]))

    yaws = []
    for i in range(0,l):
        yaws.append(int(data[i][2]))

    line_chart = pygal.Line()

    line_chart.add("Roll", rolls)
    line_chart.add("Pitch", pitches)
    line_chart.add("Yaw", yaws)

    line_chart.render_to_file("line_chart.svg")
