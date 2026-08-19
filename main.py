class Process:
    BLOCKED = "blocked"
    READY = "ready"
    RUNNING = "running"

    def __init__(self, pid, start_addr, mem_alloc):
        self.pid = pid
        self.start_addr = start_addr
        self.mem_alloc = mem_alloc
        self.status = self.READY

class Kernel:
    def __init__(self):
        self.processes = []
        self.pid_counter = 0

    def create_process(self, start_addr, mem_alloc):
        self.pid_counter += 1
        process = Process(self.pid_counter, start_addr, mem_alloc)
        self.processes.append(process)
        return process

    def run_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                if process.status == Process.READY:
                    process.status = Process.RUNNING
                    return f"Process {pid} běží."
                else:
                    return f"Process {pid} nelze spustit - status {process.status}"
        return f"Process {pid} nenalezen."

    def stop_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                process.status = Process.BLOCKED
                return f"Process {pid} zastaven se stavem 'blocked'"
        return f"Process {pid} nenalezen"

    def remove_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                if process.status == Process.RUNNING:
                    return f"Process {pid} běží a nemůže být odstraněn"
                else:
                    self.processes.remove(process)
                    return f"Process {pid} byl odstraněn"
        return f"Process {pid} nenalezen"

def main():
    kernel = Kernel()
    p1 = kernel.create_process(0x1000, 256)
    p2 = kernel.create_process(0x2000, 512)
    a = kernel.run_process(p1.pid)
    print(a)
    b = kernel.run_process(p1.pid)
    print(b)

main()
