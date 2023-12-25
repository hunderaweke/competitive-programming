class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = defaultdict(int)
        for domain in cpdomains:
            visit,url = domain.split()
            subdomains = url.split('.')
            for i in range(len(subdomains)):
                visits['.'.join(subdomains[i:])] += int(visit)
        return [f"{key} {value}" for value,key in visits.items()]