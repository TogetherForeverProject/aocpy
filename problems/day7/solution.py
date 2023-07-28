from utils import advent

advent.setup(7)

class Directory:
    def __init__(self, name: str):
        # Initialize a directory with its name, list of files, total files size,
        # dictionary of subdirectories, and total size of the directory.
        self.name: str = name
        self.files: list[str] = []
        self.files_size: int = 0
        self.subdirectories: dict[str, Directory] = {}
        self.total_size = 0

    def add_file(self, filename: str, size: int) -> None:
        # Add a file to the current directory and update its total files size.
        self.files_size += size
        self.files.append(filename)

    def add_dir(self, directory: "Directory") -> None:
        # Add a subdirectory to the current directory.
        self.subdirectories[directory.name] = directory

    def get_subdirectory(self, name: str) -> "Directory":
        # Get a subdirectory by its name from the current directory.
        return self.subdirectories[name]

class FilesystemNavigator:
    def __init__(self, root):
        # Initialize the FilesystemNavigator with a root directory,
        # a list to store all directories, and a directory stack to keep track of the current path.
        self.all_directories : list[Directory] = []
        self.directory_stack : list[Directory] = []
        self.root: Directory = root
        self.current_directory: Directory = root

    def cd(self, argument: str) -> None:
        # Change the current directory based on the argument.
        # Supported arguments: '..', '/', directory_name.
        match argument:
            case '..':
                return self._cd_back()
            case '/':
                return self._cd_root()
            case _:
                return self._cd_directory(argument)

    def _cd_directory(self, directory_name: str) -> None:
        # Change to the specified subdirectory.
        directory = self.current_directory.get_subdirectory(directory_name)
        self.current_directory = directory
        self.directory_stack.append(directory)
        self.all_directories.append(directory)

    def _cd_root(self) -> None:
        # Change to the root directory.
        self.current_directory = self.root
        self.directory_stack = [self.root]
        self.all_directories.append(self.root)

    def _cd_back(self) -> None:
        # Change back to the parent directory.
        self.directory_stack.pop()
        self.current_directory = self.directory_stack[-1]

def compute_directories_size(current: Directory) -> int:
    # Recursively compute the total size of the current directory and its subdirectories.
    directories_size = 0
    for d in current.subdirectories.values():
        directories_size += compute_directories_size(d)
    current.total_size = current.files_size + directories_size
    return current.total_size

def compute_total_sizes_below_threshold(directory_collection: list[Directory], threshold: int) -> int:
    # Compute the total sizes of directories in the collection that are below the threshold.
    return sum(d.total_size for d in directory_collection if d.total_size < threshold)

def compute_smallest_directory_above_threshold(directory_collection: list[Directory], threshold: int) -> int:
    # Find the smallest directory size in the collection that is above the threshold.
    return min([d.total_size for d in directory_collection if d.total_size >= threshold])

def process_input_and_find_sum_part_one(input_data) -> int:
    # Process input data and find the sum of total sizes of directories below 100,000.
    root = Directory('/')
    fsn = FilesystemNavigator(root)

    for line in input_data:
        match line.strip().split():
            case "$", "ls":
                # Ignore this command for the purpose of this task.
                pass
            case "$", "cd", argument:
                # Change the current directory based on the argument.
                fsn.cd(argument)
            case "dir", dirname:
                # Create a new subdirectory and add it to the current directory.
                directory = Directory(dirname)
                fsn.current_directory.add_dir(directory)
            case size, filename:
                # Add a file to the current directory with the given size.
                fsn.current_directory.add_file(filename, int(size))
            case other:
                # Raise an exception for any unexpected line in the input data.
                raise Exception('Unexpected line ', other)

    # Compute the total sizes of all directories in the file system.
    compute_directories_size(fsn.root)
    # Find the sum of total sizes of directories below 100,000.
    total_sum = compute_total_sizes_below_threshold(fsn.all_directories, 100_000)
    return total_sum

def process_input_and_find_smallest_directory_part_two(input_data) -> int:
    # Process input data and find the total size of the smallest directory above the required threshold.
    root = Directory('/')
    fsn = FilesystemNavigator(root)

    for line in input_data:
        match line.strip().split():
            case "$", "ls":
                # Ignore this command for the purpose of this task.
                pass
            case "$", "cd", argument:
                # Change the current directory based on the argument.
                fsn.cd(argument)
            case "dir", dirname:
                # Create a new subdirectory and add it to the current directory.
                directory = Directory(dirname)
                fsn.current_directory.add_dir(directory)
            case size, filename:
                # Add a file to the current directory with the given size.
                fsn.current_directory.add_file(filename, int(size))
            case other:
                # Raise an exception for any unexpected line in the input data.
                raise Exception('Unexpected line ', other)

    # Compute the total sizes of all directories in the file system.
    compute_directories_size(fsn.root)
    total_space_available = 70_000_000
    free_space = total_space_available - fsn.root.total_size
    space_required = 30_000_000
    additional_space_required = space_required - free_space

    # Find the total size of the smallest directory above the required threshold.
    smallest = compute_smallest_directory_above_threshold(fsn.all_directories, additional_space_required)
    return smallest

def main():
    input_data = advent.get_input()
    result_part_one = process_input_and_find_sum_part_one(input_data)
    result_part_two = process_input_and_find_smallest_directory_part_two(input_data)
    advent.print_answer(1, f"Sum of total sizes is {result_part_one}")
    advent.print_answer(2, f"Total size of smallest directory to free enough space: {result_part_two}")
