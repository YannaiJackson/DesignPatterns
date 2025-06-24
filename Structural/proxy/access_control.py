
class FileManager:
    def delete_file(self, filename: str):
        print(f"'{filename}' file deleted.")


class FileManagerProxy:
    def __init__(self, user_role: str):
        self._user_role = user_role
        self._manager = FileManager()

    def delete_file(self, filename: str):
        if self._user_role != "admin":
            print("Access denied. Only admins can delete file.")
        else:
            self._manager.delete_file(filename=filename)


# Usage
if __name__ == "__main__":
    proxy = FileManagerProxy("admin")
    proxy.delete_file("example.txt")
