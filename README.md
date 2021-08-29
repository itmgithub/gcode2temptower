# gcode2temptower

## Intro
Turn any gcode file into a termperature tower. Just slice your file as normal with CURA and then pass it through gcode2temptower.py. 

## Features
- Reads any gcode file sliced with CURA and add M104 and M109 temperature lines to it so that it turns the gcode file into a temperature tower.

## Status
gcode2temptower is still considered: testing. First results have been proven reliable but I would still consider this beta due to its limited testing scenario’s. It has succesfully been tested with Linux, FreeBSD and WSL (Windows Subsystem for Linux).

## Configuration
gcode2temptower.py uses four commandline parameters,
| Parameter      | Description                                                                                     |
| :------------- | :---------------------------------------------------------------------------------------------- |
| start layer    | The first layer to start changing the temperatures from; could also be considered "skip layers" |
| layer step     | After the first layer skip # number of layers before decreasing the temperature                 |
| start temp     | Starting temperature in celcius                                                                 |
| temp decrement | Decrease the temperature by # degrees celcius for the next layer                                |

### Example use
```
cat SmartTemperatureTower_PLA_180-225.gcode | ./gcode2temptower.py 57 50 225 5 > SmartTemperatureTower_PLA_180-225-result.gcode
```

## TODO:
- Make a non "cat" version

## Credits
Eventhough gcode2temptower is released under the 3-Clause BSD license, the accompanying temperature tower STL's are not. They are released under the also very permissive Creative Commons Share Alike license 3.0. The Smart compact temperature calibration tower by gaaZolee was retrieved from [Thingiverse](http://www.thingiverse.com/thing:2729076).
  
