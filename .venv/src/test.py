
from encodings.punycode import selective_len

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
import mysql.connector


Builder.load_file('test.kv')
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ilovenepal",
    database="psql"
)
mycursor = conn.cursor()



class mainGrid(Widget):
    all_tables_for_selected_databse = [];
    selected_table = ""


    def press(self, instance):
        text_to_add+=("press\n")


    def databases_display_request(self, instance):
        # Query to display Database
        text_to_add="All the databases you are looking for are "
        text_to_add+=("Here\n")
        all_database_name="dba,dbb,dbc,dbd,ded"
        self.ids.right_text_label.text=all_database_name


    def database_selection(self,instance):
        givendatabase = self.ids.select_database_input.text
        text_to_add = f"Selected database is {givendatabase}"
        text_to_add += "\n"
        # Code to show all the tables : .......................
        mycursor.execute("SHOW TABLES")
        results = mycursor.fetchall()
        all_tables = results;
        all_tables_for_selected_databse = all_tables
        for at in all_tables_for_selected_databse:
            text_to_add += at
            text_to_add += "\n"


        self.ids.right_text_label.text = text_to_add
        self.ids.select_database_input.text =""




    def table_selection(self,instance):
        selected_table = self.ids.select_table_input.text
        text_to_add = f"Selected table is {selected_table}"
        text_to_add += "\n"
        text_to_add+=self.show_selected_table(self)
        self.ids.right_text_label.text = text_to_add




    def show_selected_table(self,instance):
        # Code to show the table.............................................
        text_to_add = "------------------------\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "|                            |\n"
        text_to_add += "------------------------\n"

        return text_to_add



    def data_insertion(self,instance): # (a1,a2,a3,a4)
        input_request = self.ids.insert_data_input.text
        text_to_add = "Data inserted."
        self.ids.right_text_label.text = text_to_add

    def data_deletion(self, instance):  # (a1= smth, a2 =smth)
        delete_request = self.ids.insert_data_input.text
        text_to_add = "Data deleted."
        self.ids.right_text_label.text = text_to_add




class lolApp(App): # app class i guess?
    def build(self):
        return mainGrid()

if __name__ == "__main__":
    lolApp().run()
