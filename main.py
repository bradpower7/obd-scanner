import obd


def parse_command():
    rawMode = input("Please select operation mode:");

    if rawMode not in ['1','2','3','4','6','7']:
        print("Invalid mode selected.")
        return
    
    mode = int(rawMode);

    rawPid = input("Please enter command PID (Dec):");
    try:
        pid = int(rawPid);
    except:
        print("Invalid PID format - please type a decimal integer.");
        return;


    if 0 <= pid < len(obd.commands[mode]):
        cmd = obd.commands[mode][pid];

        print("Selected command name:")
        print(cmd);

        return cmd;
    else:    
        print ("Invalid PID for the specified mode.")
        return


#Operations:

# Scan current status
# Scan freeze frame

obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.OBD("/dev/rfcomm0") # create connection with USB 0

print("Supported Commands:")
print(connection.supported_commands)

#connection = obd.OBD();
while(1 == 1):
    cmd = parse_command();

    if(cmd != None):
        response = connection.query(cmd);
        print("Response:")
        print(response)
        print("----------------")