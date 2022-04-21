import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'), 
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        
        input_value = values['-INPUT-']
        
        if input_value.isnumeric():
            
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.621371, 2)
                    output_msg = f'{input_value} km is {output} miles'

                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_msg = f'{input_value} kg is {output} pounds.'

                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_msg = f'{input_value} sec is {output} min.'
                    
            window['-OUTPUT-'].update(output_msg)

window.close()
                