# 1 Create a program capable of displaying questions to the user like KBC.
# 2 Use the List data type to store the questions and their correct answers.
# 3 Display the final amount the person is taking home after playing the game.

print("answer format: A, B, C or D\n")

Questions = [[
  "1. What is part of a database that holds only one type of information?",
  "Report", "Field", "Record", "File", "B"
],
             [
               "2. 'OS' computer abbreviation usually means ?",
               "Order of Significance", "Open Software", "Operating System",
               "Optical Sensor", "C"
             ],
             [
               "3. Who created Pretty Good Privacy (PGP)?", "Phil Zimmermann",
               "Tim Berners-Lee", "Marc Andreessen", "Ken Thompson", "A"
             ],
             [
               "4. '.TXT' extension refers usually to what kind of file?",
               "Text File", "Image file", "Audio file", "Adobe Acrobat file",
               "A"
             ],
             [
               "5. '.JPG' extension refers usually to what kind of file?",
               "System file", "Animation/movie file", "MS Encarta document",
               "Image file", "D"
             ]]

Prize = [100, 200, 300, 500, 600]


#This que() Function Is For Questions
#But Now Comes The Problem That These Questions Are Not Repeating!
#So Now What Should I Do Next, How To Solve This Problem?
def que():
  for k in range(len(Questions)):
    Question = Questions[k]
    print(Question[k])
    print(f"\nA. {Question[1]}          B. {Question[2]}")
    print(f"C. {Question[3]}          D. {Question[4]}")
    ask = input("\nEnter Your Answer - ")
    # Check If User Following The Format Or Not!
    if ask == ask.upper():
      if ask == Question[-1]:
        # Increase The Price Every time User Give Right Answer
        print(
          f"\nCongratulations, Your Answer is Correct.\nYou have won Rs. {Prize[k]} \n"
        )
      else:
        # Ask user If They Want To Continue OR Exit(C/E)
        c = input(
          "Sorry, Your Answer is Wrong.\n\nYou Want To Play Again(Y/N) - ")
        y = "y"
        if c == y:
          print("\n")
          que()
        else:
          quit()
    else:
      print("\nFollow The Format!")
      quit()


que()
