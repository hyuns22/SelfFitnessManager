import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Graph((250, 280), (0, 0), (250, 280), key='logo')],
          [sg.Text('모드 선택'), sg.Radio('트레이닝', 1), sg.Radio('테스트', 1)]]

window = sg.Window('인터페이스', layout, finalize=True)
window['logo'].draw_image(filename='logo1.png', location=(6.5, 270))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered', values[0])

window.close()