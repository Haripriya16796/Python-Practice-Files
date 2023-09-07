from multiprocessing import Process

def print_hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    names = ["king", "queen", "minister", "soldier"]

    processes = []

    for name in names:    
        process = Process(target = print_hello, args = (name,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()