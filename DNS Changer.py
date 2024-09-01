import os

Quit = ''
while not (Quit == 'Q' or Quit == 'q'):
    Repeat = 0
    while Repeat == 0:
        try:
            DNS = ['1.1.1.1', '8.8.4.4', '10.202.10.10', '78.157.42.100', '10.202.10.102', 'Automatically', 'Other']
            DNS2 = ['1.0.0.1', '8.8.8.8', '10.202.10.11', '78.157.42.101', '10.202.10.202', 'Automatically', 'Other']
            Interface = ['Ethernet', '"WI-FI"', 'Other']
            print("\n(Note: If you wanna set your DNS to Automatically, must select both DNS to Automatically.)")
            Quest = int(input(f'\n{DNS}\nPlease select your primary DNS between 1-7: '))
            if Quest == 1:
                DNS = DNS[0]
            elif Quest == 2:
                DNS = DNS[1]
            elif Quest == 3:
                DNS = DNS[2]
            elif Quest == 4:
                DNS = DNS[3]
            elif Quest == 5:
                DNS = DNS[4]
            elif Quest == 6:
                DNS = 'dhcp'
            elif Quest == 7:
                DNS = input('Please enter your primary DNS: ')
            else:
                print("Invalid primary DNS.")
                Repeat = "Base" + 1

            Quest = int(input(f'\n{DNS2}\nPlease select your secondary DNS between 1-7: '))
            if Quest == 1:
                DNS2 = DNS2[0]
            elif Quest == 2:
                DNS2 = DNS2[1]
            elif Quest == 3:
                DNS2 = DNS2[2]
            elif Quest == 4:
                DNS2 = DNS2[3]
            elif Quest == 5:
                DNS2 = DNS2[4]
            elif Quest == 6:
                DNS2 = 'dhcp'
            elif Quest == 7:
                DNS2 = input('Please enter your secondary DNS server: ')
            else:
                print("Invalid secondary DNS.")
                Repeat = "Base" + 1

            Quest = int(input(f'\n{Interface}\nPlease select your interface between 1-3: '))
            if Quest == 1:
                Interface = Interface[0]
            elif Quest == 2:
                Interface = Interface[1]
            elif Quest == 3:
                Interface = input('Please enter your interface: ')
            else:
                print("Invalid Interface.")
                Repeat = "Base" + 1

            if DNS != 'dhcp' and DNS2 != 'dhcp':
                os.system(f'netsh interface ip set dns name={Interface} static {DNS}')
                os.system(f'netsh interface ip add dns name={Interface} {DNS2} index=2')
            elif DNS == 'dhcp' and DNS2 == 'dhcp':
                os.system(f'netsh interface ip set dns name={Interface} dhcp')
            else:
                print("Invalid DNS or DNS2.")
                Repeat = "Base" + 1
            print("Done!")
            Quit = input("If you wanna quit, please type (Q), otherwise press enter: ")
            if Quit == 'Q' or Quit == 'q':
                Repeat = 1
            else:
                continue
        except ValueError:
            print("Value Error, please try again.")
            Repeat = 1
        except TypeError:
            print("Please try again.")
            Repeat = 1
