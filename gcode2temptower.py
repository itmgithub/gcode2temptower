#!/usr/bin/python3

import sys
import fileinput

def readgcode(startLayer,layerStep,startTemp,tempDec):
	print(f"{startLayer} {layerStep} {startTemp} {tempDec}")
	layerMatch="LAYER:"+str(startLayer)
	for line in sys.stdin:
		print(line.rstrip())
		if layerMatch in line:
			startTemp-=tempDec
			print(f"M104 S{startTemp}")
			print(f"M109 S{startTemp}")
			startLayer+=layerStep
			layerMatch="LAYER:"+str(startLayer)
		pass
	

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print(f"Usage: {sys.argv[0]} <start layer> <layer step> <start temp> <temp decrement>")
		print(f"Example: cat tower.gcode | {sys.argv[0]} 57 50 225 5 > temptower.gcode")
	else:
		readgcode(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
