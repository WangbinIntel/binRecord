import git

def merge_branch_into_main(repo_path, branch_name):
    try:
        # 打开Git仓库
        repo = git.Repo(repo_path)
        repo.git.checkout('main')
        repo.remotes.origin.pull()
        # 切换到main分支
        if branch_name not in [b.name for b in repo.branches]:
            repo.create_head(branch_name)
        repo.git.checkout(branch_name)
        repo.index.add(['/home/sys_tcsbios/binRecord/chart5.png'])
        repo.index.commit("Add new images")
        repo.remote().push(branch_name)
        # 获取要合并的分支
        repo.git.checkout('main')
        branch_to_merge = repo.branches[branch_name]
        repo.git.merge(branch_to_merge)
        repo.git.branch("-d", branch_name)
        repo.git.push()
        repo.git.push("origin", "--delete", branch_name)


        print(f'Successfully merged {branch_name} into main.')

    except git.GitCommandError as e:
        import logging
        logging.exception(f'Error merging branches: {e}')

if __name__ == "__main__":
    repo_path = "/home/sys_tcsbios/binRecord"  # 替换成你的Git仓库路径
    branch_to_merge = "test_checkout"  # 替换成要合并的分支名称
    merge_branch_into_main(repo_path, branch_to_merge)
