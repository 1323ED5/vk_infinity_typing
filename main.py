import time
from getpass import getpass

import vk_api


# inputs
login = input("login: ")
password = getpass()
target_peer = input("peer_id: ")
prunk_type = "typing"

if input("audiomessage? (y/n): ").lower() == "y":
    prunk_type = "audiomessage"

print(f"\nprunktype: {prunk_type}")


# authorisation
vk_session = vk_api.VkApi(login, password, app_id=2685278)  # KateMobile app
vk_session.auth()
vk = vk_session.get_api()


print("\nI'm working")

while True:
    vk.account.setOnline()
    vk.messages.markAsRead(peer_id=target_peer)
    vk.messages.setActivity(peer_id=target_peer, type="typing")
    time.sleep(5)
