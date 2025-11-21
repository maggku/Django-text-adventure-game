from django.db import models

# Create your models here.

class Paragraph(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

    def play(self):
        print(self.text)
        for i, choice in enumerate(self.choice_set.all(), 1):
            print(f"{i}. {choice.choice_text}")


class Choice(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='choice_set')
    choice_text = models.CharField(max_length=200)
    leads_to = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='incoming_choices')

    def __str__(self):
        return self.choice_text


class Hero(models.Model):
    name = models.CharField(max_length=100, unique=True)
    current_paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.current_paragraph}"

"""
For the Paragraph class:

Think about what attributes you need: id, content (treść), and choices (opcje wyboru)
For the choices, consider using a dictionary where keys might be the text shown to the player and values are the IDs of paragraphs they lead to
The play() method should use print() to display things nicely - maybe number the choices like "1. Go left", "2. Go right"
To create a Paragraph from data (like from JSON), think about using the __init__ method with parameters, or maybe a @classmethod that takes a dictionary


import json


class Paragraph:
    def __init__(self, id, text, choices):
        self.id = id
        self.text = text
        self.choices = choices


    def play(self):
        print(self.text)
        for choice in self.choices:
            print(" - ", choice)


class Hero:
    def __init__(self, name, current_paragraph):
        self.name = name
        self.current_paragraph = current_paragraph


    def save(self):
        try:
            with open("getout_save_game.json", "r") as file:
                all_heroes = json.load(file)
        except FileNotFoundError:
            all_heroes = {}

        all_heroes[self.name] = {
            "current_paragraph": self.current_paragraph
        }


        with open("getout_save_game.json", "w") as file:
            json.dump(all_heroes, file)

    @classmethod
    def load(cls, name):
        try:
            with open("getout_save_game.json", "r" ) as file:
                all_heroes = json.load(file)
        except FileNotFoundError:
            print("No saved games found")



        if name in all_heroes:
            return all_heroes[name]["current_paragraph"]
        else:
            print("Create your hero")

"""
