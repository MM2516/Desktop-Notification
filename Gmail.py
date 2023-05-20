import tkinter as tk
import imaplib
import email
import time
import webbrowser
from tkinter import messagebox

def get_unread_msgs(username, password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select("inbox")
    _, data = imap.search(None, "UNSEEN")
    msg_nums = data[0].split()
    unread_msgs = len(msg_nums)
    latest_sender = None
    if (unread_msgs > 0) & (len(msg_nums) != k)  :
        latest_email = msg_nums[-1]
        _, msg_data = imap.fetch(latest_email, "(RFC822)")
        email_body = msg_data[0][1]
        message = email.message_from_bytes(email_body)
        latest_sender = message["From"]
    imap.close()
    imap.logout()
    return unread_msgs, latest_sender if latest_sender else None


def check_for_new_email(username, password):
    root = tk.Tk()
    root.withdraw()
    root.geometry("+1900+1700") 
    gmail_url = "https://mail.google.com"
    gmail_tab_open = False
    while True:
        # Check for new email every 30 seconds
        unread_msgs, latest_sender = get_unread_msgs(username, password)
        if unread_msgs > 0:
            notification_text = f"New msg from {latest_sender} \n {unread_msgs} unread emails\n "
            root = tk.Tk()
            root.withdraw()
            root.geometry("+{}+{}".format(root.winfo_screenwidth()-300, root.winfo_screenheight()-100))
            root.attributes('-topmost', True)
            root.after(5000, lambda: root.destroy())

            root.after(0, lambda: root.bell())
            root.after(5000, root.destroy)
            if not gmail_tab_open:
                # Open Gmail in a new tab if it's not already open
                webbrowser.open_new(gmail_url)
                gmail_tab_open = True
            tk.messagebox.showinfo(title="New Email", message=notification_text)
        elif gmail_tab_open:
            # Close the Gmail tab if there are no unread emails
            for tab in webbrowser.get().tabbed_browser.tabs:
                if gmail_url in tab.url:
                    tab.close()
                    gmail_tab_open = False
        time.sleep(5)


if __name__ == "__main__":
    check_for_new_email("sreenivasulu.yenugondu@gmail.com", "sphmiiqzkkwromvk")
