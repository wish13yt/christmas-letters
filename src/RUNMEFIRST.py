print("merry christmas woooo ")
print("this will put your bot token in a token.txt")
print("if you are too lazy to run this program just put your bot token in token.txt (in the folder where your app.py is)")
token = input("what is your bot token? make one at https://discord.com/developers/applications: ")
with open("token.txt", "w") as f:
    f.write(token)
print("ok its been written real well i used my typewriter")
print("now run app.py to start your cool christmas bot")