
import game_logic as gl

print('\n\nPLEASE USE SMALL CAPS')

choice=input('\nIF YOU WANT TOO START THE GAME TYPE start \nIF NOT PLEASE TYPE stop\nYOUR CHOICE:')#inputing choice from the user

if choice == 'start':
    print('\n\t\t\tOK THEN LETS INTO THE GAME\n')
    gl.play()
elif choice == 'stop':
    print('\n\t\t\tOK THE GAME ENDED ')
else:
    print('\n\t\t\tYOU ARE AN IDIOT WHO DONT EVEN KNOW HOW TO READ')