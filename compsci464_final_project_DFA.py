#FILE FOR TESTING DFA
#Euan House
#Compsci 464 final project
#due may 3


#change file path here to the testing nfa or dfa file

#file = open("C:\\Users\\house\\Desktop\\compsci464_project\\examples\\dfadesc.txt" , "r") 
#C:\Users\house\Desktop\compsci464_project\examples\dfadesc.txt
#C:\Users\house\Desktop\compsci464_project\examples\dfarot.txt

input_string = ''

print("What is the filepath for the DFA's txt file? of the form ex:\" C:\\a\\b\\c\\dfadesc.txt \"")
try:
    path = input()
    file = open(path,"r")
except:
    print("opening the path's text file resulted in error")
    print("program was given path :",path)

print("what is the input string for the DFA?")
try:
    input_string = input()
except:
    print("input string resulted in error")

lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].replace("\n","")
print(lines) #inputed file


#RETRIEVING AUTOMATA DATA FROM FILE
#and storing into vars

alphabet = []
for i in range(0,len(lines[0])):
    alphabet.append(lines[0][i])

number_of_states = int(lines[1])

list_of_states = []
for i in range(0,number_of_states):
    list_of_states.append(lines[2+i])

#add number_of_states to get current file index
start_state = lines[2+number_of_states]
number_of_accept_states = int(lines[3+number_of_states])

accept_states = []
for i in range(0, number_of_accept_states):
    accept_states.append(lines[4+number_of_states])

#add number_of_states and number_of_accept states to get current file line index
number_of_transitions = int(lines[4 + number_of_states + number_of_accept_states])

list_of_transitions = []
for i in range(0, number_of_transitions):
    list_of_transitions.append(lines[5 + number_of_states + number_of_accept_states + i].split(","))


print("\n")
print("AUTOMATA INFORMATION ------------------------------------")
print("Alphabet is :",alphabet)
print("Number of states is :",number_of_states)
print("List of states is :",list_of_states)
print("Start state is :",start_state)
print("Number of accept states is :",number_of_accept_states)
print("Accept states is :",accept_states)
print("Number of transitions is :",number_of_transitions)
print("List of transitions is :",list_of_transitions)
print("---------------------------------------------------------\n\n")




#assumes it already has global vars from file, can update later easily
def find_next_transition(current_state, input_char):
    next_state_found = False
    r_next_states = []

    for i in range(0, number_of_transitions):
        if(list_of_transitions[i][0] == current_state and input_char == list_of_transitions[i][2]): #checks that transition's source is same as current state to 'use' transition

            next_state_found = True
            print("at state ",current_state," , nextstate at transition:", list_of_transitions[i],sep='')
            r_next_states.append(list_of_transitions[i][1])
            
    #check if next state was found, used later when in final state
    if next_state_found == False: 
        print("NO NEXT STATE FOUND",sep='')
        r_next_states = [None]

    return r_next_states



current_state = start_state

#THIS IS WHERE TO CHANGE INPUT STRING AND TEST

input_index = 0


while (input_index < len(input_string)+1): #+1 to allow for the FINAL iteration (checks if its in the accept state)
    
    #the input char needs to be NONE on the last iteration so that way it checks if there are any next states.
    if(input_index < len(input_string)):
        input_char = input_string[input_index]
    else:
        input_char = None

    
    #returns next state that is possible to go to
    next_state = None
    print("index:",input_index,end=' | ')
    next_state = find_next_transition(current_state, input_char)[0]

    
    #checks if string accepted by checking index, current state/accept_state, and that there is no next state
    if(input_index == len(input_string)) : print("\nlast index, checking if in accept states.........\n")
    if(input_index == len(input_string) and current_state in accept_states and next_state == None):
        print("INPUT STRING ACCEPTED!!!!!!!!!!!!!!")
        print("current accepted state is :",current_state)
        print("next state is :",next_state,)
    elif(input_index == len(input_string)):
        print("INPUT STRING FAILED")

    current_state = next_state

    input_index += 1


    











    
