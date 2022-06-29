import PySimpleGUI as sg

sg.theme('DarkGreen6')  # For importing the theme used for window


def bmiWindow():
    sg.theme('green')  # For importing the theme used for window

    title="BMI CALCULATOR"
    layout=[
                [sg.Text('BMI is used to categorize whether a person is')],
                [sg.Text("Under Weight       <  18.5")],
                [sg.Text("Normal            18.5  -  24.9")],
                [sg.Text("Over Weight     24.9  -  29.9")],
                [sg.Text("Obesity              >  29.9")],
                [   sg.Text("Height:"),sg.Input(key='HEIGHT',size=(5,1)) ,  
                    sg.Text("Weight:"),sg.Input(key='WEIGHT',size=(5,1)) 
                ],
                
                [   sg.Button('Calculate',key='-CALCULATE-'),sg.Button('Clear',key='-CLEAR-') ],

        ]

    window = sg.Window(title,layout)

    def clear_input():   # To clear the input in the window
        for key in values:
            window[key]('')
        return None

    while(True):
        event , values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == '-CLEAR-':
            clear_input()

        if event == '-CALCULATE-':
            height= values['HEIGHT']
            weight= values['WEIGHT']

            try:
                if (type(float(height)) == float) and (type(float(weight)) == float):
                    
                    heightsq=pow(float(height)/100,2)
                    output = round(float(weight)/float(heightsq), 2)  # for rounding off to two digits
                    output_string= f'Your BMI is {output} '
                    if(float(output)<18.5):
                        result_string=f'UNDER WEIGHT'
                    elif(float(output)>=18.5 and float(output)<=24.9):
                        result_string='HEALTHY'
                    elif(float(output)>24.9 and float(output)<=29.9):
                        result_string=f'OVER WEIGHT'
                    else:
                        result_string=f'OBESITY'
    
                    sg.popup('Hello\n',output_string,result_string)

            except:
                sg.popup('INVALID INPUT','\t !!!')



    window.close()


###########################################################################################################################



def bmrWindow():
    sg.theme('PythonPlus')  # For importing the theme used for window

    title="BMR CALCULATOR"
    layout=[
                [sg.Text('The BMR is measured under very restrictive circumstances while awake.')],
                [sg.Text('An accurate BMR measurement requires that a persons sympathetic nervous system is inactive')],
                [sg.Text('Which means the person must be completely rested\n')],
                [sg.Text('The daily caloric need is the BMR value multiplied by a factor')],
                [sg.Text('with a value between 1.2 and 1.9, depending on activity level.')],

                [   sg.Text("Height:"),sg.Input(key='HEIGHT',size=(5,1)) ,  
                    sg.Text("Weight:"),sg.Input(key='WEIGHT',size=(5,1)) ,
                    sg.Text("Age:"),sg.Input(key='-AGE-',size=(5,1))      
                ],

                [   sg.Text("Gender:"), sg.Radio('Male','-GENDER-',default=True, key='-MALE-'),
                    sg.Radio('Female','-GENDER-',default=False,key='-FEMALE-')],
                
                [    sg.Button('Calculate',key='-CALCULATE-'),  sg.Button('Clear',key='-CLEAR-') ],

        ]
    window = sg.Window(title,layout)

    def clear_input():   # To clear the input in the window
        for key in values:
            window[key]('')
        return None

    while(True):
        event , values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-CLEAR-':
            clear_input()
        
        if event == '-CALCULATE-':
            height= values['HEIGHT']
            weight= values['WEIGHT']
            age=values['-AGE-']
            
            try:
                if (type(float(height)) == float) and (type(float(weight)) == float) and type(float(age) == float):
                    
                    if(values['-MALE-']==True):
                        output=round(8.362+(13.397*float(weight)+(4.799*float(height))-(5.677*float(age))),3)
                        output_string= f'Your BMR is {output} Calories/day'
                        if(float(output)>1600 and float(output)<1800):
                            result_string='Calories burned at average rate'
                        else:
                            result_string='Doing Good'
                        
                    else:
                        output=round(447.593+(9.247*float(weight)+(3.098*float(height))-(4.330*float(age))),3)
                        output_string= f'Your BMR is {output} Calories/day'
                        result_string=f'WORKING HARD'
                        if(float(output)>1500 and float(output)<1600):
                            result_string='Calories burned at average rate'
                        else:
                            result_string='Doing Good'
                
                sg.popup('Hello\n',output_string,result_string) 

            except:
                sg.popup('INVALID INPUT','\t !!!')


    window.close()



##############################################################################################################################


def HomeWindow():
    titleHome="Welcome Page"
    layoutH=[
                [sg.Text('Check How Healthy You Are')],
                [sg.Text('Body mass index (BMI)')],
                [sg.Text('It is a measure of body fat based on height and weight that applies to adult men and women.')],
                [sg.Button('BMI',key='-BMI-')],
                [sg.Text('Your Basal Metabolic Rate (BMR)')],
                [sg.Text('It is the number of calories you burn as your body performs basic (basal) life-sustaining function.')],
                [sg.Text('Commonly also termed as Resting Metabolic Rate (RMR)')],
                [sg.Button('BMR',key='-BMR-')]
           ]
    window=sg.Window(titleHome,layoutH)
    while(True):
        event , values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == '-BMI-':
            bmiWindow()
        else:
            bmrWindow()
    window.close()

##########################################################################################################################

HomeWindow()