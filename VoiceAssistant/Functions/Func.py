

#CMD Size
def cmd_size():
    print(os.system(G))
    width = "150"
    height = "30"
    os.system("mode con cols="+width+"lines="+height)

#GameOne
def game_one():
    sub.Popen([control_input.openGameOne])
#gameTwo
def game_two():
    sub.Popen([control_input.openGameTwo])
#ShowIP
def my_ip():
    sub.call(["ipconfig"])      


def JarvisStartSpeak():           
    starting_sounds = ["Hello, system is starting","The system is starting","loading system","preparing system","system is being edited"]
    mix2 = random.choice(starting_sounds)
    speak(mix2)


def MyAssistan():
    print(f.renderText('TOKYO'))
    print(f.renderText('the daughter of the computer :)'))
    print(G+""" 

===============================================================================================================================================
                                                        
                                                        COMMANDS

** BROWSER **                                                       ** SYSTEM **
                        
- Google                   ==> [+] ör: (Open google...vb)           - Terminal (cmd)        ==> [+] ör: (Show terminal...vb)
- Facebook                 ==> [+] ör: (Open facebook...vb)         - Close                 ==> [+] ör: (Close: Tokyo is closed...vb)
- Auto Login Your Facebook ==> [+] ör: (Open My facebook...vb)      - shut down computer    ==> [+] ör: (shut down my computer...vb)
- Youtube                  ==> [+] ör: (Open youtube...vb)          - Create folder         ==> [+] ör: (Folder Created...vb)   
- Default Page             ==> [+] ör: (Open (my page name)...vb)   - Clear                 ==> [+] ör: (Clear terminal...vb)
- Youtube mp3 dowload Page ==> [+] ör: (Open youtube mp3...vb)      - Size                  ==> [+] ör: (My screen size...vb)
- Search google            ==> [+] ör: (Search google...vb)         - Ip                    ==> [+] ör: (My ip...vb)


________________________________________________________________________________________________________________________________________________

** PROPERTİES **                                                    ** DEFAULT **

- Time  ==> [+] ör: (What Time is it...vb)                         - how are you expressions  ==> [+] ör: (How are you...vb)
- Mail  ==> [+] ör: (Send Mail...vb)                               - Your Name                ==> [+] ör: (What is your name...vb)
- Word  ==> [+] ör: (Open Word...vb)                               - personality              ==> [+] ör: (hi,who is you...vb)
- Music ==> [+] ör: (Open Music...vb)
- Game  ==> [+] ör: (Open my game or My game...vb)
- Wifi  ==> [+] ör: (Show Wifi Password...vb)
- SS    ==> [+] ör: (Screenshot..vb)
- Find  ==> [+] ör: (Where is canada...vb)
               
=================================================================================================================================================

            """)
