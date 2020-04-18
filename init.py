import sys

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except:
    print("Error: Input or Output file is missing")
    sys.exit(1)

try:
    fd_input_file = open(input_file, 'r')
    fd_output_file = open(output_file, 'w') 
except:
    print("Error: Unable to open files")
    sys.exit(1)


fd_output_file.write("attack,\
                        timestamp,\
                        http_status,\
                        http_request,\
                        uri,\
                        remote_addr,\
                        bytes_read,\
                        bytes_uploaded,\
                        upstream_response_time,\
                        upstream_connect_time,\
                        session_duration,\
                        termination_state,\
                        ip_source\
                        \n")
#file1.writelines(L) 

count = 0
Lines = fd_input_file.readlines()
current_id = None

for line in Lines:
    try:
        array_line = line.strip().split(";")
        if current_id is None:
            current_id = array_line[0]
        

        fd_output_file.write("\n")
    except:
        print(current_id)
        continue

    if count>100:
        break


fd_output_file.close()


