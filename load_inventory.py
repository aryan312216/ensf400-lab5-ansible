from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

# Initialize a DataLoader
loader = DataLoader()

# Initialize an InventoryManager with the DataLoader
inventory = InventoryManager(loader=loader, sources='/workspaces/ensf400-lab5-ansible/load_inventory.py')

# Print the names, IP addresses, and group names of all hosts
for host in inventory.get_hosts():
    print(f"Name: {host.name}, IP: {host.vars['ansible_host']}, Groups: {[g.name for g in host.groups]}")

# Ping all hosts
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play import Play

# Create a play
play_source = dict(
    name="Ansible Play",
    hosts='all',
    gather_facts='no',
    tasks=[
        dict(action=dict(module='ping'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)

# Run the play
tqm = TaskQueueManager(
    inventory=inventory,
    loader=loader,
    
)
result = tqm.run(Play().load(play_source, loader=loader))