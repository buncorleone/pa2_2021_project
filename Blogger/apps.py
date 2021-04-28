from django.apps import AppConfig
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import requests, json


class BloggerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blogger'


# class CreatePost:
#
#     pass
#
#
# class Home:
#
#     pass
#
#
# class ShowPosts:
#
#     pass
#
#
# class ShowCategories:
#
#     pass
#

class GUI:
    def __init__(self, parent, title_text):
        # from . import views

        self.title_text = title_text
        self.parent = parent

        self.parent.title('Blogger')

        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)

        self.top_frame = ttk.Frame(parent, padding=10)
        self.top_frame.grid(row=0, column=0, sticky=W + E)

        self.top_frame.columnconfigure(0, weight=1)

        # self.title_text = StringVar()

        self.top_label = Label(self.top_frame, text=title_text, font=("Calibri",
                                                                      15))
        self.top_label.grid(row=0, sticky=W)

        self.post_nav_btn = Button(self.top_frame, text="Posts")
        self.post_nav_btn.grid(row=0, column=4, sticky=E)
        self.categories_nav_btn = Button(self.top_frame, text="Categories")
        self.categories_nav_btn.grid(row=0, column=5, sticky=E)
        self.profile_button = Button(self.top_frame, text="Profile")
        self.profile_button.grid(row=0, column=6, sticky=E)

        self.body_frame = ttk.Frame(parent, padding=10)
        self.body_frame.grid(row=1, column=0)

        self.body_text = tk.scrolledtext.ScrolledText(self.body_frame, width=80, height=20, font=("Calibri", 12),
                                                      wrap=WORD)
        self.body_text.configure(state="disabled")
        self.body_text.grid(row=1, column=0, sticky=W + E, columnspan=6)

        # Populate posts into main text field and only show bottom frame on Posts screen
        if title_text == "Posts":
            self.body_text.configure(state="normal")
            b = requests.get('http://localhost:8000/posts')
            b_dict = b.json()
            for p in b_dict['posts']:
                for k, v in p.items():
                    self.body_text.insert(tk.INSERT, f"{k}: {v}\n")
                self.body_text.insert(tk.INSERT, f"{'-'*80}\n")
            self.body_text.configure(state="disabled")

            self.bottom_frame = ttk.Frame(parent, padding=10)
            self.bottom_frame.grid(row=2, column=0, sticky=W + E)

            # self.bottom_frame.columnconfigure(0, weight=1)

            self.bottom_label = Label(self.bottom_frame, text="Create new post", font=("Calibri bold", 12))
            self.bottom_label.grid(row=2, column=0, columnspan=4, sticky=W + E)

            def capture_post():
                post_title = self.new_title.get()
                post_category = self.new_category.get()
                post_text = self.post_box.get('1.0', 'end')
                # post_dict = {"Title": post_title, "Category": post_category, "Body": post_text, "Author": "TBC"}
                # test = requests.post('http://localhost:8000/posts/', data=post_dict)
                # print(test.text)

                self.body_text.configure(state="normal")
                self.body_text.insert(tk.INSERT, f"title: {post_title}\ncategory: {post_category}\nbody: {post_text[:-1]}\n{'-'*80}")
                self.body_text.configure(state="disabled")
                self.post_box.delete('1.0', 'end')

                post_dict = {"Title": post_title, "Category": post_category, "Body": post_text[0:-1]}
                print(post_dict)

            self.new_title_label = Label(self.bottom_frame, text="Title:", font=("Calibri", 11))
            self.new_title_label.grid(row=3, column=0, sticky=W)

            self.new_title = Entry(self.bottom_frame)
            self.new_title.grid(row=3, column=1, sticky=W)

            self.new_cat_label = Label(self.bottom_frame, text="Category:", font=("Calibri", 11))
            self.new_cat_label.grid(row=3, column=2, sticky=W)

            self.new_category = Entry(self.bottom_frame)
            self.new_category.grid(row=3, column=3, sticky=W)

            self.new_post_label = Label(self.bottom_frame, text="Post body:", font=("Calibri", 11))
            self.new_post_label.grid(row=4, column=0, columnspan=2, sticky=W)

            self.post_box = scrolledtext.ScrolledText(self.bottom_frame, height=4, width=60)
            self.post_box.grid(row=5, column=0, columnspan=4, sticky=W)

            self.post_button = Button(self.bottom_frame, padx=5, pady=5, text="Post", font=("Calibri", 15), bg="green",
                                      fg="white", width=14, height=3, command=capture_post)
            self.post_button.grid(row=3, column=5, sticky=E, rowspan=4)

    def populate_posts(self):


        pass

    def populate_categories(self):
        pass

    def close_window(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.parent.destroy()


def main():
    root = tk.Tk()
    GUI(root, "Posts")
    root.mainloop()


if __name__ == "__main__":
    main()
