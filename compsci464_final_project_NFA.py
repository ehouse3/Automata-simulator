#FILE FOR TESTING NFA
#Euan House
#Compsci 464 final project
#due may 3


#change file path here to the testing nfa or dfa file
#print("\n")
#file = open("C:\\Users\\house\\Desktop\\compsci464_project\\examples\\nfalarge.txt" , "r")
#C:\Users\house\Desktop\compsci464_project\examples\nfalarge.txt

input_string = ''

print("What is the filepath for the NFA's txt file? of the form ex:\" C:\\a\\b\\c\\nfadesc.txt \"")
try:
    path = input()
    file = open(path)
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
    accept_states.append(lines[4+number_of_states+i])

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



#the plan is simple
#quite simple really


#assumes it already has global vars from file, can update later easily
def find_next_transitions(current_states, input_char):
    
    r_next_states = []
    
    #EPSILON UPDATE
    #immediatly update the current_states list and append the current_states list with outputs of all epsilon transitions
    #the later loop should run correctly because the current states will have all of the current states + epsilon trasition states
    
    #if we find an epsilon transition, we need to reitterate through the list of transitions to check if there is another that leads out of the one just checked
    transition_taken_list = []
    epsilon_transition_found = True
    while(epsilon_transition_found == True):
        epsilon_transition_found = False

        #itterates through list of current states
        for state in range(0, len(current_states)):

            #itterates through list of transition functions
            for i in range(0, number_of_transitions):  

                #checks if transition is epsilon AND if transition before state is a current state
                #to prevent inf loop: whatever is added to current states, also add to another list, if the start state of transition function is in that list, ignore. (no_check_list)
                #no_check_list does not work if for an nfa that would need to go back through that function through another epsilon
                if(list_of_transitions[i][0] == current_states[state] and list_of_transitions[i][2] == 'EPSILON' and list_of_transitions[i] not in transition_taken_list):

                    epsilon_transition_found = True #forces it to reitterate
                    
                    print("on state ",current_states[state]," , found EPSILON state transitions : ", list_of_transitions[i],sep='')
                    #adds new post transition function state to list of current_states
                    current_states.append(list_of_transitions[i][1])
                    transition_taken_list.append(list_of_transitions[i])
    print("current_states :",current_states)




    #itterates through list of alive current states
    for state in range(0, len(current_states)):

        next_state_found = False
        #itterates through list of transition functions
        for i in range(0, number_of_transitions):

            #checks that transition's source is same as current state to 'use' transition
            if(list_of_transitions[i][0] == current_states[state] and input_char == list_of_transitions[i][2]): 
                
                next_state_found = True
                print("on state ",current_states[state]," , found state transitions : ", list_of_transitions[i],sep='')

                #needs to append multiple transitions to next_states[i]
                
                r_next_states.append(list_of_transitions[i][1])
    
            
        

        
        #for removal of a branch: 
        #if, when searching through list of transition functions, does not find path to take, kill branch(pop from list of next state functions and will die)
        if (next_state_found == False and input_char != None): 
            print("no next state found for branch : ",state," | state : ",current_states[state],sep='')
            
        elif (next_state_found == False):
            print("no next state found for branch : ",state," | state : ",current_states[state],sep='')
        

        #print("checked state column")
    
    #returns 2d array of next_states[current state][set of possible state transitions for current state] 
    return r_next_states


current_states = ['']
current_states[0] = start_state


input_index = 0


while (input_index < len(input_string)+1): #+1 to allow for the FINAL iteration (checks if its in the accept state)
    

    #the input char needs to be NONE on the last iteration so that way it checks if there are any next states.
    if(input_index < len(input_string)):
        input_char = input_string[input_index]
    else:
        input_char = None #might become error later

    print()
    
    next_states = None

    #running in parallel to find next state transitions
    print("index:",input_index,end=' | \n')
    next_states = find_next_transitions(current_states, input_char)
    print("current_states :",current_states)
    print("next_states :",next_states)

    #checks if string accepted by checking index, current state/accept_state, and that there is no next state
    
    accepted = False
    
    if(input_index == len(input_string)):
        print("\nlast index, checking if in accept states.........\n")
        state = 0
        accepted_state = []

        
        for state in range(0,len(current_states)):
            
            if(current_states[state] in accept_states):
                accepted = True
                accepted_state.append(current_states[state])
            

        if accepted:
            print("!!!!!!!!!!!!!!  INPUT STRING ACCEPTED  !!!!!!!!!!!!!!")
            print("current accepted state is :",accepted_state)
            print("next state is :",next_states,)   
        else:
            print("INPUT STRING FAILED")


    current_states = []
    for i in range(0,len(next_states)):
        current_states.append(next_states[i])

    input_index += 1


    











    
