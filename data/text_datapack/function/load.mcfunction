############# Formation Command Block Data Pack ############

scoreboard objectives add LEVEL dummy

############ --- LVL_0 --- ############ 

scoreboard objectives add lvl0 dummy
scoreboard players set step lvl0 0
scoreboard players set CRunning lvl0 0
scoreboard players set validate lvl0 0
scoreboard players set timeTesting lvl0 0
scoreboard players set modulo lvl0 1
scoreboard players set temp lvl0 1

############ --- LVL_1 --- ############

scoreboard objectives add lvl1 dummy
scoreboard players set step lvl1 0
scoreboard players set CRunning lvl1 0
scoreboard players set validate lvl1 0
scoreboard players set timeTesting lvl1 0
scoreboard players set modulo lvl1 1
scoreboard players set temp lvl1 1

############ --- LVL_2 --- ############

scoreboard objectives add lvl2 dummy
scoreboard players set step lvl2 0
scoreboard players set CRunning lvl2 0
scoreboard players set validate lvl2 0
scoreboard players set timeTesting lvl2 0
scoreboard players set modulo lvl2 1
scoreboard players set temp lvl2 1


tellraw @a {"text": "Formation command block data pack loaded!", "color": "gold"}