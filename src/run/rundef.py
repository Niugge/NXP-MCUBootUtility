import sys, os

kUartSpeed_Blhost = ['4800', '9600', '19200', '57600', '115200']
kUartSpeed_Sdphost = ['115200']

kBootDeviceMemId_SemcNor      = 0x8
kBootDeviceMemId_FlexspiNor   = 0x9
kBootDeviceMemId_SemcNand     = 0x100
kBootDeviceMemId_FlexspiNand  = 0x101
kBootDeviceMemId_LpspiNor     = 0x110
kBootDeviceMemId_UsdhcSd      = 0x120
kBootDeviceMemId_UsdhcMmc     = 0x121

kBootDeviceMemBase_SemcNor      = 0x90000000
kBootDeviceMemBase_FlexspiNor   = 0x60000000
kBootDeviceMemBase_SemcNand     = 0x0
kBootDeviceMemBase_FlexspiNand  = 0x0
kBootDeviceMemBase_LpspiNor     = 0x0
kBootDeviceMemBase_UsdhcSd      = 0x0
kBootDeviceMemBase_UsdhcMmc     = 0x0

kRamFreeSpaceStart_LoadCommOpt        = 0x00002000
kRamFreeSpaceStart_LoadDekData        = 0x00002100
kRamFreeSpaceStart_LoadKeyBlobContext = 0x00002200
kRamFreeSpaceStart_LoadKeyBlobData    = 0x00002300
kRamFreeSpaceStart_LoadCfgBlock       = 0x00003000
kRamFreeSpaceStart_LoadPrdbOpt        = 0x00004000

kRamFreeSpaceStep_LoadKeyBlobData    = 0x100

kRamFreeSpaceStart_Rom         = 0x20208000

kKeyBlobMaxSize = 512

