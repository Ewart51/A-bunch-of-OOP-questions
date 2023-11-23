import os
import random
class DadJokes:
    def __init__(self):
        self.__prompt = "" #this is a string
        self.__answer = "" #this is a string
        self.__prompt_list = []
        self.__answer_list = []

    def open_dadjokes(self):
        try:
            i = 1
            with open("DadJokes.txt", "r") as t:
                for lines in t:
                  if i%2 != 0:
                    self.__prompt = lines
                    self.__prompt_list.append(self.__prompt)
                  if i%2 == 0:
                    self.__answer = lines
                    self.__answer_list.append(self.__answer)
                  i += 1



        except OSError:
            print("cant find file, directory is", os.getcwd())

    def PrintRandomJoke(self):
      random_number = random.randint(1, len(self.__prompt_list))
      print("Your joke is:", self.__prompt_list[random_number])
      Ur_answer = input("whats your answer:")
      print("Ur answer:", Ur_answer, "but answer is:",self.__answer_list[random_number])


object = DadJokes()
object.open_dadjokes()
object.PrintRandomJoke()
