import tkinter as tk
from src.utils import *
from src.profileframe.utils import *


class ProfileFrame(tk.Frame):
    """Frame responsable for displaying the user stored accounts

    Attributes:
    Connection(sqlite3.Connection): Database of the app
    master(tk.frame): Frame where this frame will be loaded
    window(tk.Tk): Window of the app
    """
    def __init__(self, connection: sqlite3.Connection, master: tk.Frame, window: tk.Tk):
        tk.Frame.__init__(self, master, bg = BG_APP)

        # Placeholder
        self.user = [None, "UserNickname", None, "UserPassword", None]

        widgets_holder = tk.Frame(self,
                                  bg = BG_APP)
        widgets_holder.pack(fill = "both",
                            expand = True)

        header_holder = tk.Frame(widgets_holder,
                                 bg = BG_APP,
                                 border = 1)
        header_holder.pack(anchor = "center",
                           fill = "x")
        header_holder.columnconfigure(1, weight = 1)

        header = tk.Label(header_holder,
                          text = self.user[1],
                          font = PROFILE_HEADER_FONT,
                          fg = FG,
                          bg = BG_APP)
        header.grid(row = 0,
                    column = 0, columnspan = 4,
                    sticky = "nsew")
        self.header_update = lambda: header.configure(text = self.user[1])
        
        logoff_image = treat_image_file("assets/Logoff.png", (40, 40))

        logoff = tk.Button(header_holder,
                           image = logoff_image,
                           bg = BG_APP,
                           command = lambda: self.logoff(window))
        logoff.image = logoff_image
        logoff.configure(relief = tk.FLAT)
        logoff.grid(row = 0,
                    column = 0,
                    sticky = "w")

        change_image = treat_image_file("assets/Change_Password.png", (40, 40))

        change_password_button = tk.Button(header_holder,
                                    image = change_image,
                                    bg = BG_APP,
                                    command = lambda: change_password(self, self.user, window, connection))
        change_password_button.image = change_image
        change_password_button.configure(relief = tk.FLAT)
        change_password_button.grid(row = 0,
                             column = 2,
                             sticky = "w")

        delete_image = treat_image_file("assets/Delete.png", (40, 40))

        delete_user = tk.Button(header_holder,
                                image = delete_image,
                                bg = BG_APP,
                                command = lambda: delete_current_user(self, self.user, window, connection))
        delete_user.image = delete_image
        delete_user.configure(relief = tk.FLAT)
        delete_user.grid(row = 0,
                         column = 3,
                         sticky = "w")

        header_separator = create_separator(widgets_holder)
        header_separator.pack(anchor = "center",
                              fill = "x")

        accounts = create_scrollbar_zone(widgets_holder, window)
        
        self.accounts_loader = lambda: populate_accounts(accounts, self.user[0], self.user[4], window, connection)
        self.accounts_holder = self.accounts_loader()

        footer_separator = create_separator(widgets_holder)
        footer_separator.pack(anchor = "center",
                              fill = "x")

        add_image = treat_image_file("assets/Plus_Icon.png", (50, 50))

        add = tk.Button(widgets_holder,
                        image = add_image,
                        bg = BUTTONS_BG,
                        command = lambda: add_account(self, window, connection))
        add.image = add_image
        add.pack(anchor = "center",
                 pady = 10)

    def reload(self, changing_user: bool = False) -> None:
        """Reloads the header and accounts of the Profile frame
        
        Parameters:
        changing_user(bool): Only turned to true when changing the logged used
        """
        if changing_user:
            self.header_update()
        
        if self.accounts_holder != None:
            self.accounts_holder.destroy()

        self.accounts_holder = self.accounts_loader()
        return

    def logoff(self, window):
        """Clears the user info and the frame with the loaded accounts"""
        self.user = [None, "UserNickname", None, "UserPassword", None]

        self.accounts_holder.destroy()
        self.accounts_holder = None

        window.change_frame("LoginFrame")

        return
