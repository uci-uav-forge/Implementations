from rrtplanner import perlin_occupancygrid, RRTStar, random_point_og, plot_rrt_lines, plot_path, plot_og, plot_start_goal
import matplotlib.pyplot as plt
og = perlin_occupancygrid(200, 200, 0.4)
n = 2000
r_rewire = 80
rrts = RRTStar(og, n, r_rewire)

xstart = random_point_og(og)
xgoal = random_point_og(og)
T, gv = rrts.plan(xstart, xgoal)

totalDistance = 0

for e1, e2 in T.edges():
    totalDistance += T.edges[e1, e2]["cost"]

path = rrts.route2gv(T, gv)
path_pts = rrts.vertices_as_ndarray(T, path)

fig = plt.figure()
ax = fig.add_subplot()

plot_og(ax, og)
plot_start_goal(ax, xstart, xgoal)
plot_rrt_lines(ax, T)
plot_path(ax, path_pts)

f = open("fatJigglyAss.txt", "w")

f.write(str(xstart) + ",")
f.write(str(xgoal) + ",")

for row in og:
	for number in row:
		f.write(str(number))
	f.write(",")
	
f.close()

print("Total Distance: " + str(totalDistance))

plt.show()