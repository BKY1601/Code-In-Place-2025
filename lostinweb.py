import time

def slow_print(text, delay=1.5):
    print(text)
    time.sleep(delay)

def quiz_question_1():
    print("\n🧠 QUIZ TIME!")
    print("What year is Zen from?")
    print("A) 2094")
    print("B) 2255")
    print("C) 1994")
    print("D) 2050")

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == "B":
        print("✅ Correct!\n")
    else:
        print("❌ Wrong. The correct answer is B) 2255\n")

def quiz_question_2():
    print("\n🧠 QUIZ TIME!")
    print("Why is Zen trying to stop the crawler?")
    print("A) It became self-aware")
    print("B) It causes cat videos to disappear")
    print("C) It is destroying the web after merging levels")
    print("D) It steals information")

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == "C":
        print("✅ Correct!\n")
    else:
        print("❌ Wrong. The correct answer is C) It is destroying the web\n")

def quiz_question_3():
    print("\n🧠 QUIZ TIME!")
    print("What is the full word? Crawler will a_ _ _ _")
    print("A) alive")
    print("B) alone")
    print("C) allow")

    answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == "A":
        print()
        #print("✅ Correct!\n")
    else:
        print("❌ Wrong. The correct answer is A) alive\n")

def quiz_question_4():
    print("\n🧠 FINAL QUIZ!")
    print("Did Zen crack the code and save the future?")
    print("A) Yes")
    print("B) No")

    answer = input("Your answer (A/B): ").strip().upper()

    if answer == "A":
        print("✅ Correct!\n")
    else:
        print("❌ Wrong. Zen Crack the code. The correct answer is A) Yes\n")

def tell_story():
    slow_print("🎮 Welcome to 'LOST IN WEB' — An Interactive Story + Quiz Game!\n", delay=1.5)
    print()
    slow_print(r"""
    
  _      ____   _____ _______      _____ _   _    __          ________ ____  
 | |    / __ \ / ____|__   __|    |_   _| \ | |   \ \        / /  ____|  _ \ 
 | |   | |  | | (___    | |         | | |  \| |    \ \  /\  / /| |__  | |_) |
 | |   | |  | |\___ \   | |         | | | . ` |     \ \/  \/ / |  __| |  _ < 
 | |___| |__| |____) |  | |        _| |_| |\  |      \  /\  /  | |____| |_) |
 |______\____/|_____/   |_|       |_____|_| \_|       \/  \/   |______|____/ 
                                                                             
    """, 2)

    slow_print("🧍 Zen arrives at Mr. B's house, the creator of the world's first web crawler in 1994.")

    slow_print(r"""
         ____________
        |   [Mr. B]  |
        |____________|
         |   ||   |
         |___||___|
    """)

    slow_print("Zen: Hi Mr. B!")
    print()
    slow_print("Mr. B: Wow, beautiful jacket and cool hat!")
    print()
    slow_print("Zen: It's 3D printed. Listen, I need something from you. We have very little time.")
    print()
    slow_print("Mr. B: What do you need?")
    print()
    slow_print("Zen: Something vital... to save the future.")
    print()
    slow_print("Mr. B: Save the future?")
    print()
    slow_print("Zen: You made crawlers to index the web, right?")
    print()
    slow_print("Mr. B: Right. Seamless web search was the goal.")
    print()
    slow_print("Zen: That technology evolved... and in the future, it’s destroying everything.")
    print()
    slow_print("Zen: I'm from 2255. We now have Quantum AI and time travel.")
    print()
    slow_print("Zen: But the web exploded—Surface, all level(Surface, Deep) of web got merged.")
    print()
    slow_print("Zen: Your first crawler, the Master Crawler, turned rogue. It’s devouring everything.")

    quiz_question_1()
    quiz_question_2()

    slow_print("Mr. B: Alright. Show me what needs to be done.")
    print()
    slow_print("Zen: There’s a shutdown command — only you can enter it.")
    print()
    slow_print("Mr. B: I’ll do it... wait, I need my goggles.")
    print()
    slow_print(r"""
   (O_o) ... footsteps ...
    | |     
   /   \  
    """)

    slow_print("Zen: Mr. B? Mr. B?!")
    print()
    slow_print("Zen looks around... but Mr. B is suddenly gone.")
    print()
    slow_print("...like he was taken. Silently. Swiftly. A faint energy ripple lingers in the air...")

    print()
    slow_print("On the screen, something flickers...")

    slow_print(r"""
  +-------------------------------+
  | ENTER FINAL 4 LETTERS:       |
  | CRAWLER WILL A_ _ _ _        |
  +-------------------------------+
    """, delay=2)

    slow_print("Zen sees the first part typed by Mr. B: 'Crawler will a'")
    print()
    slow_print("He must guess the final 4 letters... fast.\n")

    print("⏳ 30 seconds left...\n")
    time.sleep(1)
    print("⏳ 20 seconds left...\n")
    time.sleep(1)
    print("⏳ 10 seconds left...\n")
    time.sleep(1)

    quiz_question_3()
    quiz_question_4()

    slow_print("The Final code is Crawler will alive")
    slow_print("Zen saved the world 🌍. The web is safe... for now.")
    print()
    slow_print("🌐 END OF CHAPTER: LOST IN WEB 🌐", 2)

if __name__ == "__main__":
    tell_story()
