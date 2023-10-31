if len(untracked_files[0]):
    for untracked_file in untracked_files:
        repo.git.add(untracked_file[0])
        logging.info(f"added: {untracked_file[0]}")
        problem_name = input("Enter the name of the problem: ")
        problem_number = input("Enter the number of the problem: ")
        problem_difficulty = input("Enter difficulty level: ")
        problem_link = input("Enter problem link: ")
        platform = input("Enter plaform: ")
        readme.write(
            f"| {problem_number}. | [{problem_name}]({problem_link}) | {problem_difficulty} | | {platform}| ||[{'Python' if 'py' in untracked_file[0] else 'C++' }](./{untracked_file[0]})|"
        )
        problem_status = input("Enter problem status: ")
        repo.git.commit(m=f"solved: {problem_name}")
readme.close()
repo.git.add("README.md")
repo.git.commit(m="updated: readme.md")