class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        final_collection = {}
        final_collection_list = []
        for domain_visits in cpdomains:
            visits, domain = domain_visits.split()
            domain_names = domain.split('.')
            if domain not in final_collection.keys():
                final_collection[domain] = int(visits)
            else:
                final_collection[domain] += int(visits)
            for i in range(domain.count('.')):
                dot_index = domain.index('.')
                domain = domain[dot_index+1:]
                if domain not in final_collection.keys():
                    final_collection[domain] = int(visits)
                else:
                    final_collection[domain] += int(visits)
        
        for keys, values in final_collection.items():
            final_collection_list.append(str(values) + " " + keys)
        return final_collection_list
