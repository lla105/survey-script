import os

# from tkinter import *
import tkinter as tk
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Provide spreasheet ID
# from URL: https://docs.google.com/spreadsheets/d/1c6rXLc6UssMPLbFuDlyvBgYVeEd5PFrcUdyQIv9DDIU/edit#gid=0
TransactionSheet = "1c6rXLc6UssMPLbFuDlyvBgYVeEd5PFrcUdyQIv9DDIU"
# global_credential = None

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")
        self.root.geometry("800x500")
        self.button = tk.Button(self.root, 
                        text="Add Transactions", 
                        command=self.open_popup,
                        padx = 50,
                        pady = 20)
        self.button.place(relx=0.65, rely=0.2)
    def open_popup(self):
        popup_window = ViewTransactions(self.root)
class ViewTransactions:
    def __init__(self, parent):
        global SheetDataList

        self.popup = tk.Toplevel(parent)
        self.popup.title("View Transactions")

        self.text_widget = tk.Text(self.popup, wrap=tk.WORD, width=80, height=50)
        self.text_widget.pack()
        # self.entry = tk.Entry(self.popup)
        # self.entry.pack()
        self.submit_button = tk.Button(self.popup, 
                                       text="Query August", 
                                       command=self.ShowTransaction)
        self.submit_button.pack()
    def ShowTransaction(self):
        SheetDataList = PullData()
        self.text_widget.delete(1.0, tk.END)
        column_widths = [max(len(str(item)) for item in column) for column in zip(*SheetDataList)]
        for eachTransaction in SheetDataList:
            formatted_row = '  '.join(f"{item:<{width}}" for item, width in zip(eachTransaction, column_widths)) + '\n'
            self.text_widget.insert(tk.END, formatted_row)



def PullData():
    sheet_name = "August"
    start_cell = "A2"
    end_cell = "F190"
    range_string = f"{sheet_name}!{start_cell}:{end_cell}"

    service = build("sheets", "v4", credentials=global_credential)
    sheets = service.spreadsheets()
    SheetData = sheets.values().get(spreadsheetId=TransactionSheet, 
                                    range=range_string).execute()
    SheetDataList = SheetData['values']
    return SheetDataList


global_crendential = None
def testt():
    print(global_credential)
def main():
    # call_tk()
    credentials = None
    if os.path.exists("token.json"): # if this file exists
        # Loading credentials from token file, which will be created when we use the credentials file
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:  # if credentials not valid
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request()) # refresh them here
        else:
            # Load credential files, authenticate ourselves.
            # flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            # Create the token json file.
            token.write(credentials.to_json())

    try:
        global global_credential
        global_credential = credentials 
        print(credentials)
        print(global_credential)

        
        root = tk.Tk()
        app = MainApplication(root)
        root.mainloop()
        # rowcount = this.mService.spreadsheets().values().get(spreadsheetId=TransactionSheet, range).execute().getValues().size()
        # last_row = len(values)+1

 
    except HttpError as error:
        print(error)
    
if __name__ == "__main__":
    main()