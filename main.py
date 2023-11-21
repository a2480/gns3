import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.ultima_modificacao = {}

    def on_modified(self, event):
        if event.is_directory or self.ignorar_arquivo(event.src_path):
            return
        self.processar_evento(event.src_path, 'modificado')

    def on_created(self, event):
        if event.is_directory or self.ignorar_arquivo(event.src_path):
            return
        self.processar_evento(event.src_path, 'criado')

    def on_deleted(self, event):
        if event.is_directory or self.ignorar_arquivo(event.src_path):
            return
        self.processar_evento(event.src_path, 'excluído')

    def ignorar_arquivo(self, arquivo):
        return arquivo.endswith(".swp")

    def processar_evento(self, arquivo, acao):
        tempo_atual = time.time()
        ultima_modificacao = self.ultima_modificacao.get(arquivo, 0)

        if tempo_atual - ultima_modificacao > 1:
            self.ultima_modificacao[arquivo] = tempo_atual
            git_commit_and_push()
            print(f'Arquivo {arquivo} foi {acao}.')

def git_commit_and_push():
    try:
        # Specify the 'gns3' directory
        directory = 'gns3'

        # Navigate to the 'gns3' directory
        current_dir = os.path.dirname(os.path.realpath(directory))
        os.chdir(current_dir)

        # Check if the directory is a Git repository
        if os.path.exists(os.path.join(current_dir, '.git')):
            print("Git repository found in the 'gns3' directory.")
        else:
            # If not a Git repository, initialize one
            subprocess.run(['git', 'init'],cwd=directory)
            print("Initialized a new Git repository in the 'gns3' directory.")

        # Add all files to the staging area
        subprocess.run(['git', 'add', '.'],cwd=directory)

        # Commit changes with a default commit message
        subprocess.run(['git', 'commit', '-m', 'Automated commit'],cwd=directory)

        # Push to the default remote repository (you may need to set it up)
        subprocess.run(['git', 'push', 'origin', 'main'],cwd=directory)
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def monitorar_pasta(pasta):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, pasta, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    pasta_monitorada = "gns3"
    monitorar_pasta(pasta_monitorada)


