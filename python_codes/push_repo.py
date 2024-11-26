import os
from datetime import datetime
import git


def push_repository():
    try:
        # Initialize repo object from current directory
        repo = git.Repo(os.getcwd())

        # Check if there are any untracked or staged changes
        if repo.is_dirty(untracked_files=True):
            # Stage all changes, including untracked files
            repo.git.add(all=True)

            # Create a commit message with timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            commit_message = f"Auto commit at {timestamp}"

            # Commit the changes
            repo.index.commit(commit_message)
            print(f"Committed changes with message: {commit_message}")

        else:
            print("No changes to commit.")

        # Push changes to the remote repository
        try:
            origin = repo.remote(name='origin')
            current_branch = repo.active_branch
            origin.push(current_branch)
            print(f"Successfully pushed changes to branch '{current_branch}'.")
        except git.exc.GitCommandError as e:
            print(f"Failed to push changes: {e}")

    except git.exc.InvalidGitRepositoryError:
        print("Error: The current directory is not a valid Git repository.")
    except git.exc.GitCommandError as e:
        print(f"Git command error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Ensure GitPython is installed
    try:
        import git
    except ImportError:
        print("GitPython not found. Installing...")
        os.system('pip install gitpython')
        import git

    # Call the function to push the repository
    push_repository()
