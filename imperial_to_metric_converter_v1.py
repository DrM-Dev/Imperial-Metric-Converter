#Metric & Imperial Converter v01 by Dr.M-DEV

#==================imports:
from tkinter import *
from numpy.ma.core import size


print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print("**** WELCOME to Metric & Imperial Converter v1    -by-    Dr.M-Dev ****")
#______________________________________________________________


#\\\\\\GLOBAL CONSTANTS
#---------
RESALT = 0
INPUT_system = "Mile"#Mile as default "Mile" or "Km"
OUTPUT_system = "Km"
#note: make a condition that makes them switch, and never the same at a given time!

#==================Base:
window = Tk()
window.minsize(500,300)
window.maxsize(530,300)
window.config(padx=20, pady=20)
window.title("Metric & Imperial Converter v1")
#
#==================window icons:
#___________ICONS
#PROGRAM ICON------------------
program_icon = PhotoImage(file="images/Conversion Icon.png")
############
prog_icon_label = Label(window, image=program_icon)
prog_icon_label.place(x=-21.5, y=150)

#INFO-SCREEN-------------------
info_screen_img = PhotoImage(file="images/info_screen2.png")
info_screen_label = Label(window,image=info_screen_img)
info_screen_label.place(x=250, y=-10)

#CONVERSION-COMPLETE ICON------------
complete_img = PhotoImage(file="images/Complete.png")
complete_img_label = Label(window, image=complete_img)
complete_img_label.place(x=10000, y=10000) #->out of bounds
#
#With Text ++
conversion_done_txt = Label(text="✅Conversion Complete")
conversion_done_txt.place(x=10000, y=10000) #->out of bounds

#INPUT WARNING ICON------------
is_warning_on = False #default
#
warning_img = PhotoImage(file="images/Warning.png")
warning_img_label = Label(window, image=warning_img)
warning_img_label.place(x=10000, y=10000) #->out of bounds
#
#With Text ++
input_warning = Label(text="⚠️INPUT ERROR")
input_warning2 = Label(text="-Please try typing numbers only!")

#PROCESSING STATE BUTTON-LIGHT------------
processing_lights_x = 452
processing_lights_y = 249
#====
processing_light_g_img = PhotoImage(file="images/green_state.png")
processing_light_g = Label(window, image=processing_light_g_img)
processing_light_g.place(x=processing_lights_x,y=processing_lights_y)
#====
processing_light_r_img = PhotoImage(file="images/red_state.png")
processing_light_r = Label(window, image=processing_light_r_img)
processing_light_r.place(x=10000,y=10000)

##==============================================================================================Conversion SETS
CONVERSION_SETS = ["mile to kilometer", "fahrenheit to celsius", "pound to kilogram", "gallon to liter"]
#                        set 0                   set 1                  set 2               set 3
CURRENT_SET = CONVERSION_SETS[0]
#
#icons:


#-----------------------------------Change_SET_Commands:
def update_labels():
    global INPUT_system
    global OUTPUT_system
    ##################
    # ------------------------UPDATING LABELS\\
    # INPUT SYSTEM Label
    input_measur_sys.config(text=f"{INPUT_system}")
    #        &
    # OUTPUT SYSTEM Label
    output_measur_sys.config(text=f"{OUTPUT_system}")

########################
def mile_to_km():
    global CONVERSION_SETS
    global CURRENT_SET
    global RESALT
    global INPUT_system
    global OUTPUT_system
    ##################
    CURRENT_SET = CONVERSION_SETS[0]
    RESALT = 0
    INPUT_system = "Mile"  # Mile as default "Mile" or "Km"
    OUTPUT_system = "Km"
    #
    update_labels()

#~~~~~~~~~~~~~~~~~~~~~~~
def f_c():
    global CONVERSION_SETS
    global CURRENT_SET
    global RESALT
    global INPUT_system
    global OUTPUT_system
    ##################
    CURRENT_SET = CONVERSION_SETS[1]
    RESALT = 0
    INPUT_system = "F"  # F as default
    OUTPUT_system = "C"
    #
    update_labels()

#~~~~~~~~~~~~~~~~~~~~~~~
def lb_kg():
    global CONVERSION_SETS
    global CURRENT_SET
    global RESALT
    global INPUT_system
    global OUTPUT_system
    ##################
    CURRENT_SET = CONVERSION_SETS[2]
    RESALT = 0
    INPUT_system = "Lb"  # Lb as default
    OUTPUT_system = "Kg"
    #
    update_labels()

#~~~~~~~~~~~~~~~~~~~~~~
def gal_li():
    global CONVERSION_SETS
    global CURRENT_SET
    global RESALT
    global INPUT_system
    global OUTPUT_system
    ##################
    CURRENT_SET = CONVERSION_SETS[3]
    RESALT = 0
    INPUT_system = "Gal"  # Gal as default
    OUTPUT_system = "L"
    #
    update_labels()


#___________________________________SET - Buttons
mile_km_set_button = Button(text="Mile\n&\nKilometer", font=("Arial",10,"bold"), fg="black", bg="white", background="orange", width=9, height=4, command=mile_to_km)
mile_km_set_button.place(x=100,y=163)
#
f_c_set_button = Button(text="Fahrenheit\n&\nCelsius", font=("Arial",10,"bold"), fg="black", bg="white", background="orange", width=9, height=4, command=f_c)
f_c_set_button.place(x=185,y=163)
#
bdl_kg_set_button = Button(text="Pound\n&\nKilogram", font=("Arial",10,"bold"), fg="black", bg="white", background="orange", width=9, height=4, command=lb_kg)
bdl_kg_set_button.place(x=185+85,y=163)
#
gal_l_set_button = Button(text="Gallon\n&\nLiter", font=("Arial",10,"bold"), fg="black", bg="white", background="orange", width=9, height=4, command=gal_li)
gal_l_set_button.place(x=185+85*2,y=163)




##===================================================================CodeBody Mile-Km (Startup):
#--------INPUT Entry
user_text_input = Entry(width=20)
user_text_input.insert(END, string="Enter a number")
user_text_input.grid(column=3,row=6)
user_text_input.grid(padx=(10, 10), pady=(0, 0))
#
user_input_num_label = Label(text="Input")
user_input_num_label.grid(column=2,row=6)
#TO GET INPUT:
# user_text_input.get()



#___________________________________________________________EXTRA LABELS/STUFF:
#Equal to label
qual_note1 = Label(text="Is Equal To:")
qual_note1.grid(column=2,row=7)


#INPUT SYSTEM Label
input_measur_sys = Label(text=f"{INPUT_system}")
input_measur_sys.grid(column=4,row=6)
#TO UPDATE INPUT_system:
# input_measur_sys.config(text=f"{INPUT_system}")

#OUTPUT SYSTEM Label
output_measur_sys = Label(text=f"{OUTPUT_system}")
output_measur_sys.grid(column=4,row=7)
#TO UPDATE INPUT_system:
# input_measur_sys.config(text=f"{INPUT_system}")



#___________________________________________________________Error Check Update:
def error_check_update(x1,y1,x2,y2):
    global is_warning_on
    #-------------------
    if not is_warning_on:
        # just sending them out of bounds 7-7
        warning_img_label.place(x=10000, y=10000)
        input_warning.place(x=10000, y=10000)
        input_warning2.place(x=10000, y=10000)
        # -then mark the deactivation
        #
        # showing that the conversion was complete:
        complete_img_label.place(x=x1, y=y1)
        conversion_done_txt.place(x=x2, y=y2)
        #
        # processing-light
        processing_light_g.place(x=processing_lights_x, y=processing_lights_y)  # -removed
        processing_light_r.place(x=10000, y=10000)
    else:
        ####remove-conversion-check-mark
        complete_img_label.place(x=10000, y=10000)
        conversion_done_txt.place(x=10000, y=10000)
        #
        # processing-light
        processing_light_g.place(x=10000, y=10000)  # -removed
        processing_light_r.place(x=processing_lights_x, y=processing_lights_y)

#___________________________________________________________CONVERSION
def convertion():
    global CURRENT_SET
    #
    global INPUT_system
    global RESALT
    #==================
    global is_warning_on
    #
    default_warning_img_x = 330
    default_warning_img_y = 5
    #
    default_warning_label_x = 260
    #==================
    default_completed_img_x = 330
    default_completed_img_y = 5
    #
    default_completed_text_x = 263
    default_completed_text_y = 62

    #=============================================================================SETS:
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++MILE-Km
    if CURRENT_SET == CONVERSION_SETS[0]:#"mile to kilometer"
        if INPUT_system == "Mile":
            try:
                input_in_miles = float(user_text_input.get()) #INPUT
                #
                RESALT = round(input_in_miles * 1.6, 2 )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False

                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        if INPUT_system == "Km":
            try:
                input_in_km = float(user_text_input.get()) #INPUT
                #
                RESALT = round(input_in_km / 1.6, 2 )
                output_num.config(text=f"{RESALT}")
                # XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True

        #####################################-ERROR-CHECK
        error_check_update(default_completed_img_x,default_completed_img_y,default_completed_text_x,default_completed_text_y)


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++F-C
    if CURRENT_SET == CONVERSION_SETS[1]:#"fahrenheit to celsius"
        if INPUT_system == "F":  # F and C
            try:
                input_in_f = float(user_text_input.get()) #INPUT
                #
                RESALT = round( (input_in_f - 32) * 0.56, 2  )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        if INPUT_system == "C":  # F and C
            try:
                input_in_c = float(user_text_input.get()) #INPUT
                #
                RESALT = round( input_in_c * 1.8 + 32, 2  )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        #####################################-ERROR-CHECK
        error_check_update(default_completed_img_x,default_completed_img_y,default_completed_text_x,default_completed_text_y)



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Lb-Kg
    if CURRENT_SET == CONVERSION_SETS[2]:#"pound to kilogram"
        if INPUT_system == "Lb":  # Lb and Kg
            try:
                input_in_lb = float(user_text_input.get()) #INPUT
                #
                RESALT = round( input_in_lb * 0.45, 2  )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        if INPUT_system == "Kg":  # Lb and Kg
            try:
                input_in_kg = float(user_text_input.get()) #INPUT
                #
                RESALT = round( input_in_kg / 0.45, 2  )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        #####################################-ERROR-CHECK
        error_check_update(default_completed_img_x, default_completed_img_y, default_completed_text_x,default_completed_text_y)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Gal-L
    if CURRENT_SET == CONVERSION_SETS[3]:#"gallon to liter"
        if INPUT_system == "Gal":  # Gal and L
            try:
                input_in_gal = float(user_text_input.get()) #INPUT
                #
                RESALT = round( input_in_gal * 3.785, 2  )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        if INPUT_system == "L":  # Gal and L
            try:
                input_in_li = float(user_text_input.get()) #INPUT
                #
                RESALT = round( input_in_li / 3.785, 2 )
                output_num.config(text=f"{RESALT}")
                #XXXX
                # removing-warning after typing numbers:
                # <!>
                if is_warning_on:
                    is_warning_on = False
                #-----------------
            except ValueError:
                #turn on warning-icon:
                warning_img_label.place(x=default_warning_img_x, y=default_warning_img_y)
                #############
                add_pad = 9
                input_warning.place(x=default_warning_label_x, y=50 + add_pad)
                input_warning2.place(x=default_warning_label_x, y=70 + add_pad)
                # <!>
                is_warning_on = True
        #####################################-ERROR-CHECK
        error_check_update(default_completed_img_x, default_completed_img_y, default_completed_text_x,default_completed_text_y)








#XXXXXXXXXXXXX__________________________________________________________________Conversion Button:
conver_button = Button(text="convert!", fg="black", bg="white", command=convertion)
conver_button.grid(column=3,row=9)
conver_button.focus_set() #< important



#______________________#______________________CONVERSION SWITCH
def conv_switch():
    global INPUT_system
    global OUTPUT_system
    #===============
    if CURRENT_SET == CONVERSION_SETS[0]:
        if INPUT_system == "Mile":
            INPUT_system = "Km"
            OUTPUT_system = "Mile"
        else:
            INPUT_system = "Mile"
            OUTPUT_system = "Km"
    ####
    elif CURRENT_SET == CONVERSION_SETS[1]:
        if INPUT_system == "F":
            INPUT_system = "C"
            OUTPUT_system = "F"
        else:
            INPUT_system = "F"
            OUTPUT_system = "C"
    ####
    elif CURRENT_SET == CONVERSION_SETS[2]:
        if INPUT_system == "Lb":
            INPUT_system = "Kg"
            OUTPUT_system = "Lb"
        else:
            INPUT_system = "Lb"
            OUTPUT_system = "Kg"
    ####
    elif CURRENT_SET == CONVERSION_SETS[3]:
        if INPUT_system == "Gal":
            INPUT_system = "L"
            OUTPUT_system = "Gal"
        else:
            INPUT_system = "Gal"
            OUTPUT_system = "L"
    ####

    #------------------------
    # INPUT SYSTEM Label
    input_measur_sys.config(text=f"{INPUT_system}")
    #        &
    # OUTPUT SYSTEM Label
    output_measur_sys.config(text=f"{OUTPUT_system}")

#______________________#______________________
#XXXXXXXXXXXXX-Conversion-SWITCH Button:
switch_conversion_type = Button(text="switch conversion", fg="blue", bg="white", command=conv_switch )
switch_conversion_type.grid(column=3,row=11)




#___________________________________________________________OUTPUT
output_num = Label(text="0")
#output_num.config(text=f"{RESALT}")
output_num.grid(column=3,row=7)

#=======================
#====================END
window.mainloop()
