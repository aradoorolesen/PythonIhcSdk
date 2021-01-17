def main():
    from datetime import datetime

    from ihcsdk.ihccontroller import IHCController

    ihc = IHCController('http://192.168.0.90', 'curl', 'hygger')
    if not ihc.authenticate():
        print("Authenticate failed")
        exit()

    print("Authenticate succeeded\r\n")

    runtimevalue = ihc.get_runtime_value(0x2d2e0c)
    print("Runtime value: " + str(runtimevalue))

    resourceIds = { "Oliefyr": 2960908 }
    print(resourceIds['Oliefyr'])
    runtimevalues = ihc.get_runtime_values([resourceIds['Oliefyr'], 2973463, 2999575, 3195927, 11687947, 11700235, 13081099, 13084685, 8308498 ])
    print("Runtime values: " + str(runtimevalues))

    print("Oliefyr: " + str(runtimevalues[resourceIds['Oliefyr']]))
 
    """  
    result = ihc.cycle_bool_value(8307473)
    print(str(result))
    """

main()






