import digitalocean
from time import sleep
import os

TIME_TO_WAIT=20

TOKEN=os.environ.get('DO_TOKEN')

manager = digitalocean.Manager(token=TOKEN)
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    droplet.power_on()
    print(f"Powered on {droplet.name} at {droplet.ip_address}")
    print('Waiting for box to come up...')
    for x in range(TIME_TO_WAIT, 0, -1):
        print(f'Time Remaining: {x} seconds', end='\r', flush=True)
        sleep(1)


my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    print(f'Droplet status is: {droplet.status}')

