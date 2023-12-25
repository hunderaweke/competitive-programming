class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)
        for path in paths:
            directory,*files = path.split()
            for file in files:
                content =file[file.index('(')+1:file.index(')')]
                duplicates[content].append(directory+'/'+file[:file.index('(')])
        return [ _ for _ in duplicates.values() if len(_)>1]