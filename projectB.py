import pyfiglet, socket, sys, datetime

now = datetime.datetime.now().strftime("%A %d %B %Y %H:%M:%S")
print(pyfiglet.figlet_format("Port Scanner", justify="center"))
print(now)
scan_file=open("Luisa_Bowie_Ports_Scanner_Result.txt,", "w") #creating the text file
scan_file.write("Today is: {}\n".format(now)) # write into the file the current date and time
targt = input("\nEnter a target host: ")
strt = datetime.datetime.now() #start of code execution
scan_file.write("Target host is: {}\n".format(targt))
scan_file.write("Port Scanning starts at: {}\n\n".format(strt))

try:
    target_host = socket.gethostbyname(targt)
    scan_file.write("\t*** OPEN PORTS LIST ***\n\n")
    scan_file.write("\tPORT\tSTATE\tService\n\n")
    print("\nScanning target: ", target_host)

    for port in range(1, 1026):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.0000001) #speed up the port scanning.
        response = sock.connect_ex((target_host, port))
        print("Port: {} status Code: {}".format(port, response))
        if response == 0:
            port_by_name = socket.getservbyport(port)
            scan_file.write("\t{}\t\topen\t{}\n".format(port, port_by_name))
            port += 1
        sock.close() #close the connection
# handling error for invalid name and address of the target host
except socket.error:
    print("Host name could not be resolved!")
    print("Host is not available!")
    scan_file.write("\nhost name could not be resolved!\n")
    scan_file.write("host is not available!\n")
    sys.exit()

except KeyboardInterrupt:
    print("opss!process interrupted! Exiting.. \n")
    scan_file.write("Opss!process interrupted! Exiting..")
    sys.exit()

finally:
    print("Thanks for using our Code :) ")

end = datetime.datetime.now() #end of code execution
total_time = end - strt  #total time of port scanner execution
scan_file.write("\n\nFinished executing at: {}\n".format(end)) #record end time
scan_file.write("\nTotal time of execution: {}".format(total_time)) #record total time  of port scanning








