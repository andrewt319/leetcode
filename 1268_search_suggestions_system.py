import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        sol = []
        curr = ''

        for c in searchWord:
            curr += c

            idx = bisect.bisect_left(products, curr)
            currProds = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i].startswith(curr):
                    currProds.append(products[i])
                else:
                    break
            sol.append(currProds)
        return sol

