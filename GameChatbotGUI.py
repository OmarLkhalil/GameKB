# The GUI has the following features:
#
# A window with the title "Game Chatbot". A label that prompts the user to enter a game name. An entry field where
# the user can enter the name of a game. A "Show Info" button that the user can click to display information about
# the entered game. A textbox where the information about the game is displayed. When the user enters a game name and
# clicks the "Show Info" button, the program gets information about the game from the GameKB and displays it in the
# textbox. If the entered game name is not found in the GameKB, the program displays a message indicating that it
# does not have information about that game.
#
# Overall, this GUI provides a simple and user-friendly way for users to interact with the Game Chatbot and get
# information about video games.


import tkinter as tk
from main import GameKB
# from main import GameChatbot

# Simple ChatBot Gui Using the Game Knowledge Base


class GameChatbotGUI:

    def __init__(self, master):
        self.master = master
        master.title("Game Chatbot")
        self.kb = GameKB()

        self.label = tk.Label(master, text="Enter any game name `for example Fortnite` :")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Show Info", command=self.get_info)
        self.button.pack()

        self.textbox = tk.Text(master, height=5, width=40)
        self.textbox.pack()

    def get_info(self):
        game_name = self.entry.get()
        if game_name in self.kb.games:
            game = self.kb.games[game_name]
            info = f" {game_name} is a {game['type']} game released on {game['platform']} in {game['release_year']} with a rating of {game['rating']}."
        else:
            info = f"I don't have information about {game_name}."
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", info)


if __name__ == '__main__':
    root = tk.Tk()
    game_chatbot_gui = GameChatbotGUI(root)
    root.mainloop()
