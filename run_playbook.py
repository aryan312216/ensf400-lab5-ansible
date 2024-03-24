from ansible.executor.playbook_executor import PlaybookExecutor

# Initialize a PlaybookExecutor
playbook = PlaybookExecutor(
    playbooks=['/workspaces/ensf400-lab5-ansible/hello.yml'],
    inventory=inventory,
    loader=loader,
    
)

# Run the playbook
result = playbook.run()

# Print the results
print(result)