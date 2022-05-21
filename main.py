import tkinter as tk
import random
import keyboard
from datetime import datetime

data = list({"Купил мужик шляпу, а она ему как раз."})
string = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,.:?! '


class Trainer:

    def __init__(self):
        global data, string
        self.phrases = data
        self.string = string

    def start(self):
        self.root = tk.Tk()
        self.root.title("Клавиатурный тренажер на Python")
        self.root.geometry("601x401")
        self.main_menu()
        self.root.mainloop()

    def main_menu(self):

        self.btn_start = tk.Button(text='Старт', height=2, width=10, command=self.end_main_menu)
        self.btn_start.place(relheight=0.08, relwidth=0.2, relx=0.4, rely=0.3)

    def end_main_menu(self):

        self.btn_start.destroy()
        self.process()

    def process(self):

        sentence = random.choice(self.phrases)

        self.lbl_text = tk.Label(text=sentence)
        self.lbl_text.place(relheight=0.08, relwidth=0.8, relx=0.1, rely=0.3)

        self.root.update()

        '''
        аккуратно, длинные предложения делать плохо, автоматического перехода строки не происходит, это доп. функция:

        def reformat_text(text):
            L = 70
            words = '\n'.join(' '.join(text))
            new_text = ''
            n = 0
            for w in words:
                if n + len(w) > L:
                    new_text += '\n' + w
                    n = len(w)
                else:
                    new_text += ' ' + w
                    n += len(w) + 1
            return new_text
        '''

        T = datetime.now()

        for index in range(len(sentence)):
            symbol = sentence[index] if sentence[index] != ' ' else '_'
            self.lbl_current_letter = tk.Label(text=symbol)
            self.lbl_current_letter.place(relheight=0.08, relwidth=0.8, relx=0.1, rely=0.5)

            self.root.update()

            try:
                while True:
                    if self.try_litter(sentence, index):
                        self.lbl_current_letter.destroy()
                        break
                    else:
                        self.lbl_current_letter.config(fg='red')
                        self.root.update()
            except:
                self.lbl_text.destroy()
                self.lbl_current_letter.destroy()
                self.main_menu()

        self.lbl_text.destroy()
        self.get_time(datetime.now() - T)

    def get_time(self, time):

        self.lbl_time = tk.Label(text=str(time))
        self.lbl_time.place(relheight=0.08, relwidth=0.2, relx=0.1, rely=0.3)

        self.btn_exit = tk.Button(text='Выйти', command=self.end_time)
        self.btn_exit.place(relheight=0.08, relwidth=0.2, relx=0.4, rely=0.5)

    def end_time(self):

        self.lbl_time.destroy()
        self.btn_exit.destroy()

        self.main_menu()

    def try_litter(self, sentence, index):

        input_symbol = input('Введите букву: ')

        if input_symbol == 'esc':
            raise Exception('ESCAPE!!!')
        if input_symbol in self.string:
            return input_symbol == sentence[index]


if __name__ == '__main__':
    T = Trainer()
    T.start()
