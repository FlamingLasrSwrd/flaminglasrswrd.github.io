#!/bin/bash

 
# Script needs to run as sudo for nvidia-smi settings to take effect.
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

export DISPLAY=:0 export XAUTHORITY=/var/run/lightdm/root/:0

# Memory frequency
equihashMemoryOffset="400"
ethashMemoryOffset="800"
# Core frequency
equihashCoreOffset="300" 
ethashCoreOffset="100" 

# Enable nvidia-smi settings so they are persistent the whole time the system is on.
nvidia-smi -pm 1
#Power limit for all cards in watts
PL="110"
# Set the power limit for each card (note this value is in watts, not percent!
nvidia-smi -i 0 -pl $PL
nvidia-smi -i 1 -pl $PL
nvidia-smi -i 2 -pl $PL

## Apply overclocking settings to each GPU

memoryOffset=$equihashMemoryOffset
coreOffset=$equihashCoreOffset

nvidia-settings -a [gpu:0]/GpuPowerMizerMode=1
nvidia-settings -a [gpu:0]/GPUMemoryTransferRateOffset[2]=$memoryOffset
nvidia-settings -a [gpu:0]/GPUGraphicsClockOffset[2]=$coreOffset
nvidia-settings -a [gpu:1]/GpuPowerMizerMode=1
nvidia-settings -a [gpu:1]/GPUMemoryTransferRateOffset[2]=$memoryOffset
nvidia-settings -a [gpu:1]/GPUGraphicsClockOffset[2]=$coreOffset

memoryOffset=$ethashMemoryOffset
coreOffset=$ethashCoreOffset

nvidia-settings -a [gpu:2]/GpuPowerMizerMode=1
nvidia-settings -a [gpu:2]/GPUMemoryTransferRateOffset[2]=$memoryOffset
nvidia-settings -a [gpu:2]/GPUGraphicsClockOffset[2]=$coreOffset

# Turn off light
nvidia-settings --assign GPULogoBrightness=0

# Fan Control
fanControl="no"
fanSpeed="85"

if [ $fanControl="yes" ]
then
#nvidia-settings -a [gpu:0]/GPUFanControlState=1
#nvidia-settings -a [gpu:1]/GPUFanControlState=1
#nvidia-settings -a [gpu:2]/GPUFanControlState=1
#nvidia-settings -a [fan:0]/GPUTargetFanSpeed=$fanSpeed
#nvidia-settings -a [fan:1]/GPUTargetFanSpeed=$fanSpeed
#nvidia-settings -a [fan:2]/GPUTargetFanSpeed=$fanSpeed
fi
