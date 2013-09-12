import sys;

allow_event_header = "unsigned int NumberOfOutcomes[ALL_WINS+ALL_FEATURES] = {";

key_pairs  = {};
count = 0;

key = "";
value = 0;

with open('OutComes.h', 'r') as f:
    for line in f:
        if line.startswith("unsigned"):
            key = line;
        else:
            if line.find("}};") == -1:
                count += 1;  
            else:
                value = count;
                print value;
                count = 0;

