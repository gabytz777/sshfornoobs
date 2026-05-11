import paramiko

def run_ssh_commands(host, username, password):
    commands = {
        "hostname": "hostname",
        "uptime": "uptime",
        "cpu": "cat /proc/loadavg",
        "ram": "free -m",
        "disk": "df -h",
        "os": "uname -a"
    }

    results = {}

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=host, username=username, password=password, timeout=5)

    for key, cmd in commands.items():
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode().strip()
        err = stderr.read().decode().strip()

        results[key] = output if output else err

    client.close()
    return results
