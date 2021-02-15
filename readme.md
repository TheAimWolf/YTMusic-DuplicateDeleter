# **YTMusic-DuplicateDeleter**
YTMusic-DuplicateDeleter deletes all duplicate songs of a YT-Music playlist you own, so you can clean your favorite playlists.
### **What does this do?**
You log into your YT-Music Account, than you can pick a playlist the script should scan for duplicates. Then you see all
duplicate songs and you get asked if you want to delete all duplicates. If you say yes, the script will clean the provided playlist.

### **Prerequisites**
- You have to own the playlist that you want to clean!
- You need Python 3.5 or higher (Because the API says so). I used Python 3.7
- You need to pip install ytmusicapi with the following command: `pip install ytmusicapi`
- The script should be in a directory where it has permissions to write files (It creates a headers_auth.json
at the first startup, the token to access YT-Music. You shouldn't share this file with anyone!)

### **How to use it?**
- Start the script (for example: `python main.py` when you are in the directory of the script)
- The script will ask you to enter some stuff. It will provide you a website, which shows you where to find this "stuff"
- After you entered this, you just press `enter ctrl+z enter` and the script will start is procedure
- Now you just type the name of the playlist you want to clean. If you don't know the name of the playlist just leave emtpy
The script will then show you all the playlists that you own.
- The script then scans for duplicates and will list each duplicate. If you have a song 3 times your playlist, the song will
be listed two times (because there are 2 duplicates)
    - If there are no duplicates in your playlist, the script will tell you that and will exit
- Now you just confirm you want to delete all duplicates by typing `y` and pressing `enter`
- All done! You can check if there are any duplicates left by running the script again

### **Known issues**
- If you have two different songs which are named the same, the script will most likely identify them as duplicates (In work)
- Sometimes the script throws errors even there are no errors. This is because I messed up the recursion :P (In work)

### **Thanks to sigma67 (https://github.com/sigma67)**
He developed the YT-Music API I am using, so all credits go to him (API-repository: https://github.com/sigma67/ytmusicapi).

### **Licensing**
You can do whatever you want with this script, please just don't say that it is yours ;)
